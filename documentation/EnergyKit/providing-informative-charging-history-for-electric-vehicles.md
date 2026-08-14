# Providing charging history for electric vehicles

**Framework**: EnergyKit

Track energy consumption and provide people detailed insights into the charging of their electric vehicle.

#### Overview

You can use EnergyKit to optimize electric vehicle (EV) charging based on grid cleanliness and electricity rates, and provide people with insights into their charging sessions. Receive grid forecasts from the framework, make intelligent charging decisions, and submit energy usage data back to the framework.

To display energy usage information, adopt the [`EnergyKit LoadEvents Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.energykit.loadevents-experience). Use the Home app to display activity logs and insights based on the submitted data.

To perform an analysis of energy usage, first gather information:

- Discover energy *venues*, or locations for charging devices, associated with a person’s home or homes.
- Stream electricity guidance that identifies optimal charging times.
- Generate and submit electrical load events that track energy consumption.
- Generate and submit status events that explain charging behavior.
- Enable automatic display of charging data and insights in the Home app.

Gathering this information allows your app to help people reduce their environmental impact and electricity costs, and answer common questions about their charging sessions.

> ❗ **Important**: Energy guidance is only available in the contiguous United States. To use EnergyKit, the system requires your app to have the [`EnergyKit Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.energykit) entitlement with a value of `true`.

#### Retrieve Energy Venues

Energy venues represent physical locations where devices consume or generate electricity. Venues correspond to homes that a person configures in the Home app. Energy guidance, data submission, and insight provision require working with venues. You can retrieve the available venues by calling [`venues()`](energyvenue/venues().md), and store each venue’s identifier for later use, as shown in the example below. You may run into errors when you query for venues; for information on how to address them, see [`EnergyKitError`](energykiterror.md).

```swift
do {
    let venues = try await EnergyVenue.venues()
    for venue in venues {
        // Store venue information for later use.
        print("Found venue: \(venue.name) with ID: \(venue.id)")
    }
} catch { /* Handle errors. */ }
```

> 💡 **Tip**: Consider Swift Data or Core Data to maintain a local database of venues and their associated charging locations.

If your app supports multiple charging locations, allow people to manage them independently. For example, the sample code project [`Optimizing home electricity usage`](optimizing-home-electricity-usage.md) demonstrates an option that toggles clean-energy charging per venue.

#### Stream Electricity Guidance

Electricity guidance provides forecasts that identify when cleaner electricity is available on the grid and when electricity rates are lower. Use the guidance to optimize how your managed devices consume electricity.

To request electricity guidance from the framework, create a query with a suggested action and pass it to the guidance service:

```swift
let query = ElectricityGuidance.Query(suggestedAction: .shift)

for try await currentGuidance in ElectricityGuidance.sharedService.guidance(
    using: query,
    at: venueID
) {
    // Use the guidance to make charging decisions.
    processGuidance(currentGuidance)
}
```

The guidance stream continues indefinitely, providing updated forecasts as they become available. EnergyKit typically delivers new guidance every hour, but updates can occur more often when grid conditions change significantly.

Choose a [`ElectricityGuidance.SuggestedAction`](electricityguidance/suggestedaction-swift.enum.md) for your device to indicate whether, for a given task, the device is flexible on the total amount of energy it consumes, or the time of day that it performs the task.

Each guidance forecast contains an array of [`ElectricityGuidance.Value`](electricityguidance/value.md) instances that cover the next 24 hours. Each value includes a time interval and a rating from 0.0 to 1.0, in which lower ratings indicate cleaner, less expensive electricity.

Store the most recent guidance in an observable property so your app can react to updates and recalculate charging schedules when new forecasts arrive.

Calculating how much energy a vehicle needs and how long its charging takes provides guidance you can use to you can make charging decisions. Calculate a charging schedule by selecting time periods with the lowest rating, which represent the cleanest, least expensive electricity:

```swift
func energyRequiredToFullCharge() -> Double {
    let currentCharge = batteryCapacity * (stateOfCharge / 100)
    let targetCharge = batteryCapacity * (desiredStateOfCharge / 100)
    return max(0, targetCharge - currentCharge)
}

let energyRequired = energyRequiredToFullCharge()
let timeRequiredForCharging = 60 * 60 * (energyRequired / chargingPower)
```

There’s no opportunity for optimization if the charging time exceeds the available window. In this situation, begin charging immediately. If optimization is an option, select the cleanest time periods that provide enough charging time:

```swift
func selectCleanestChargingIntervals(
    chargeTimeRequired: Double,
    guidance: ElectricityGuidance,
    chargeWindow: DateInterval
) -> [DateInterval] {
    let sortedGuidance = guidance.values.sorted { $0.rating < $1.rating }
    var chosenIntervals: [DateInterval] = []
    var totalTimeSelected = 0.0
    
    for value in sortedGuidance where totalTimeSelected < chargeTimeRequired {
        if value.interval.start >= chargeWindow.start 
            && value.interval.start < chargeWindow.end {
            chosenIntervals.append(value.interval)
            totalTimeSelected += value.interval.duration
        }
    }
    return chosenIntervals.sorted { $0.start < $1.start }
}
```

This approach prioritizes the cleanest available electricity while ensuring the vehicle reaches its target state of charge before the person needs it.

#### Generate Electrical Load Events

Load events track energy consumption during charging sessions. They follow a session-based model; each session has a unique identifier, and progresses through three states that convey continuity: the beginning, active state, and ending.

Create a device identifier using [`ElectricalLoadDevice`](electricalloaddevice.md) to provide type-safe device information:

```swift
let device = ElectricalLoadDevice(
    id: "C621E1F8-A36B-495A-93FC-0C247A3E6F5E",
    name: "My Electric Vehicle",
    type: .electricVehicle
)
```

The device name appears in the Home app when you adopt the [`EnergyKit LoadEvents Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.energykit.loadevents-experience), so choose a name that’s meaningful to the person using your app.

When charging begins, start a new charging session. Create a load event with the [`ElectricVehicleLoadEvent.Session.State.begin`](electricvehicleloadevent/session-swift.struct/state-swift.enum/begin.md) state:

```swift
let session = ElectricVehicleLoadEvent.Session(
    id: UUID(),
    state: .begin,
    guidanceState: .init(
        wasFollowingGuidance: true,
        guidanceToken: currentGuidance.guidanceToken
    )
)

let beginEvent = ElectricVehicleLoadEvent(
    timestamp: Date.now,
    measurement: ElectricVehicleLoadEvent.ElectricalMeasurement(
        stateOfCharge: 43,
        direction: .imported,
        power: Measurement(value: 0, unit: .milliwatts),
        energy: Measurement(value: 0, unit: .EnergyKit.milliwattHours),
        performanceMetrics: ElectricVehicleLoadEvent.ElectricalMeasurement.PerformanceMetrics(
            estimatedRange: Measurement(value: 120, unit: .miles),
            batteryTemperature: Measurement(value: 25, unit: .celsius)
        )
    ),
    session: session,
    device: device
)
```

The [`ElectricVehicleLoadEvent.Session.State.begin`](electricvehicleloadevent/session-swift.struct/state-swift.enum/begin.md) event requires zero energy and zero power because charging hasn’t started. Include the [`guidanceToken`](electricityguidance/guidancetoken.md) from your current guidance forecast to allow the framework to attribute this charging session to specific grid conditions.

The load event requires you to report active charging. Create additional events with the [`ElectricVehicleLoadEvent.Session.State.active`](electricvehicleloadevent/session-swift.struct/state-swift.enum/active.md) state approximately every 15 minutes when charging is active:

```swift
let activeSession = ElectricVehicleLoadEvent.Session(
    id: session.id,  // The same ID as the begin event.
    state: .active,
    guidanceState: session.guidanceState
)

let activeEvent = ElectricVehicleLoadEvent(
    timestamp: Date.now,
    measurement: ElectricVehicleLoadEvent.ElectricalMeasurement(
        stateOfCharge: 55,
        direction: .imported,
        power: Measurement(value: 7_000_000, unit: .milliwatts),
        energy: Measurement(value: 3_500_000, unit: .EnergyKit.milliwattHours),
        performanceMetrics: performanceMetrics
    ),
    session: activeSession,
    device: device
)
```

The energy value in active events represents cumulative energy consumed since the session began. This accumulator resets when you end the session. Create active events at 15-minute intervals (0, 15, 30, and 45 minutes past the hour), or when significant changes occur, such as power level fluctuations or actions initiated by a person.

When charging completes, end the session by creating a final event with the [`ElectricVehicleLoadEvent.Session.State.end`](electricvehicleloadevent/session-swift.struct/state-swift.enum/end.md) state:

```swift
let endSession = ElectricVehicleLoadEvent.Session(
    id: session.id,
    state: .end,
    guidanceState: session.guidanceState
)

let endEvent = ElectricVehicleLoadEvent(
    timestamp: Date.now,
    measurement: ElectricVehicleLoadEvent.ElectricalMeasurement(
        stateOfCharge: 98,
        direction: .imported,
        power: Measurement(value: 0, unit: .milliwatts),
        energy: Measurement(value: 35_000_000, unit: .EnergyKit.milliwattHours),
        performanceMetrics: performanceMetrics
    ),
    session: endSession,
    device: device
)
```

The [`ElectricVehicleLoadEvent.Session.State.end`](electricvehicleloadevent/session-swift.struct/state-swift.enum/end.md) event needs to have zero power because charging has stopped. The energy value represents the total energy consumed during the entire session.

As an additional assessment of the charging session, add performance metrics to the load event. The metrics include an estimate of how much of the vehicle’s range of driving distance the charge gained, and includes battery temperature when available:

```swift
let performanceMetrics = ElectricVehicleLoadEvent.ElectricalMeasurement.PerformanceMetrics(
    estimatedRange: Measurement(value: 220, unit: .miles),
    batteryTemperature: Measurement(value: 28, unit: .celsius)
)

let measurement = ElectricVehicleLoadEvent.ElectricalMeasurement(
    stateOfCharge: 55,
    direction: .imported,
    power: Measurement(value: 7_000_000, unit: .milliwatts),
    energy: Measurement(value: 3_500_000, unit: .EnergyKit.milliwattHours),
    performanceMetrics: performanceMetrics
)
```

The range derives from the current state of charge and the vehicle’s efficiency. Temperature is important to charging performance because batteries charge more slowly at extreme temperatures.

#### Generate Status Events

Status events add to the information that load events provide by explaining the reasons behind specific charging behavior. While load events track energy consumption, status events answer questions such as why the car isn’t charging, and when charging can begin. The explanations appear in the Home app’s activity log when your app adopts the [`EnergyKit LoadEvents Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.energykit.loadevents-experience).

To report charger connection, create a [`ElectricVehicleStatusEvent.Status.chargerPluggedIn`](electricvehiclestatusevent/status-swift.enum/chargerpluggedin.md) event when a person plugs in their vehicle. This event marks the beginning of a potential charging session and provides the vehicle’s initial state:

```swift
let plugInEvent = ElectricVehicleStatusEvent(
    timestamp: Date.now,
    device: device,
    venueID: venueID,
    status: .chargerPluggedIn,
    stateOfCharge: 43,
    energy: Measurement(value: 25_000_000, unit: .EnergyKit.milliwattHours),
    estimatedRange: Measurement(value: 120, unit: .miles)
)
```

To explain idle periods, create a [`ElectricVehicleStatusEvent.Status.chargingIdle(_:)`](electricvehiclestatusevent/status-swift.enum/chargingidle(_:).md) event that details why, when charging doesn’t start immediately:

```swift
let idleEvent = ElectricVehicleStatusEvent(
    timestamp: Date.now,
    device: device,
    venueID: venueID,
    status: .chargingIdle(.waitingForCleanerEnergy),
    stateOfCharge: 43,
    energy: Measurement(value: 25_000_000, unit: .EnergyKit.milliwattHours),
    estimatedRange: Measurement(value: 120, unit: .miles),
    chargingTarget: ElectricVehicleStatusEvent.ChargingTarget(
        stateOfCharge: 98,
        estimatedCompletionTime: Date.now.addingTimeInterval(4 * 3600),
        scheduledStartTime: Date.now.addingTimeInterval(2 * 3600),
        estimatedRangeAtTarget: Measurement(value: 220, unit: .miles)
    )
)
```

The [`ElectricVehicleChargingReason.IdleReason`](electricvehiclechargingreason/idlereason.md) explains to the person why their vehicle isn’t charging yet, including whether the vehicle is waiting for cleaner grid conditions or lower energy rates.

Include charging target information to show when charging begins and when it completes. This helps people understand the expected charging timeline.

To communicate charging activity, create a [`ElectricVehicleStatusEvent.Status.chargingActive(_:)`](electricvehiclestatusevent/status-swift.enum/chargingactive(_:).md) event when charging starts that explains the situation.

When the person unplugs their vehicle, report it by creating a [`ElectricVehicleStatusEvent.Status.chargerUnplugged`](electricvehiclestatusevent/status-swift.enum/chargerunplugged.md) event:

```swift
let unplugEvent = ElectricVehicleStatusEvent(
    timestamp: Date.now,
    device: device,
    venueID: venueID,
    status: .chargerUnplugged,
    stateOfCharge: 98,
    energy: Measurement(value: 60_000_000, unit: .EnergyKit.milliwattHours),
    estimatedRange: Measurement(value: 220, unit: .miles)
)
```

Charger disconnection marks the end of the session and represents the final charging state. After generating load events and status events, submit them together to EnergyKit. The framework accepts any type that conforms to [`ElectricalLoadEventProtocol`](electricalloadeventprotocol.md), which includes both [`ElectricVehicleLoadEvent`](electricvehicleloadevent.md) and [`ElectricVehicleStatusEvent`](electricvehiclestatusevent.md):

```swift
func submitEvents(
    loadEvents: [ElectricVehicleLoadEvent],
    statusEvents: [ElectricVehicleStatusEvent],
    to venue: EnergyVenue
) async throws {
    let allEvents: [any ElectricalLoadEventProtocol] = loadEvents + statusEvents
    try await venue.submitEvents(allEvents)
}
```

Submit events promptly after they occur rather than batching for long periods. The framework processes events asynchronously and uses them to generate insights and update the Home app display.

The EnergyKit framework validates events before accepting them and throws [`EnergyKitError.invalidLoadEvent`](energykiterror/invalidloadevent.md) if validation fails. Common validation failures include:

- Submitting events for a venue that doesn’t exist.
- Submitting events from a device that didn’t request the corresponding guidance.
- Creating session states in the wrong order (for example, [`ElectricVehicleLoadEvent.Session.State.end`](electricvehicleloadevent/session-swift.struct/state-swift.enum/end.md) before [`ElectricVehicleLoadEvent.Session.State.begin`](electricvehicleloadevent/session-swift.struct/state-swift.enum/begin.md)).
- Providing invalid measurement values (for example, negative energy).

Handle submission errors appropriately and consider retrying failed submissions after a delay:

```swift
do {
    try await venue.submitEvents(allEvents)
    print("Successfully submitted \(allEvents.count) events")
} catch EnergyKitError.invalidLoadEvent {
    print("Event validation failed - check event data")
} catch EnergyKitError.rateLimitExceeded {
    print("Submission rate limit exceeded - retry after delay")
} catch {
    print("Submission failed: \(error.localizedDescription)")
}
```

The framework throws [`EnergyKitError.rateLimitExceeded`](energykiterror/ratelimitexceeded.md) if your app submits events too frequently. Implement appropriate retry logic with exponential backoff by doubling the wait time after each failed retry attempt.

#### Request Historical Insights

After submitting load events, request insights to see how your device performs historically. Insights break down energy consumption by grid cleanliness and tariff periods, helping you verify that your charging algorithm optimizes for the cleanest and least expensive electricity.

Create an insights query that specifies the date range, granularity, and optional breakdowns:

```swift
let startDate = Calendar.current.date(byAdding: .day, value: -30, to: Date.now)!
let query = ElectricityInsightQuery(
    options: [.cleanliness, .tariff],
    range: DateInterval(start: startDate, end: Date.now),
    granularity: .daily,
    flowDirection: .imported
)
```

Pass a [`ElectricityInsightQuery.Granularity`](electricityinsightquery/granularity-swift.enum.md) that matches the time window (hourly, daily, weekly) to focus on.

Choose a specific device identifier for which to request insights:

```swift
var records = [ElectricityInsightRecord<Measurement<UnitEnergy>>]()

for await record in try await ElectricityInsightService.shared.energyInsights(
    forDeviceID: vehicleIdentifier,
    using: query,
    atVenue: venueID
) {
    records.append(record)
}
```

Each insight record contains:

- **Total energy**: Total energy consumed during the time period ([`totalEnergy`](electricityinsightrecord/totalenergy.md)).
- **Cleanliness breakdown**: Energy categorized by grid cleanliness ([`dataByGridCleanliness`](electricityinsightrecord/databygridcleanliness.md)).
- **Tariff breakdown**: Energy categorized by tariff periods ([`dataByTariffPeak`](electricityinsightrecord/databytariffpeak.md)).

To distinguish how much energy consumption occurs during clean versus less clean periods, use the cleanliness breakdown:

```swift
for record in records {
    if let cleanliness = record.dataByGridCleanliness {
        let cleanerEnergy = cleanliness.cleaner?.converted(to: .kilowattHours).value ?? 0
        let lessCleanEnergy = cleanliness.lessClean?.converted(to: .kilowattHours).value ?? 0
        
        let totalEnergy = cleanerEnergy + lessCleanEnergy
        if totalEnergy > 0 {
            let cleanPercentage = (cleanerEnergy / totalEnergy) * 100
            print("Charged during clean periods: \(cleanPercentage.formatted())%")
        }
    }
}
```

This analysis helps you verify that your charging algorithm works correctly and provides feedback for refinement.

Use the tariff breakdown to retrieve energy costs when a person connects their utility account:

```swift
for record in records {
    if let tariff = record.dataByTariffPeak {
        let offPeakEnergy = tariff.offPeak?.converted(to: .kilowattHours).value ?? 0
        let onPeakEnergy = tariff.onPeak?.converted(to: .kilowattHours).value ?? 0        
        print("Off-peak: \(offPeakEnergy) kWh")
        print("On-peak: \(onPeakEnergy) kWh")
    }
}
```

The framework provides insights only after you submit load events. Insights derive from historical data, so newly submitted events take time to reflect.

#### Display Energy Data in the Home App

When you adopt the [`EnergyKit LoadEvents Entitlement`](https://developer.apple.com/documentation/bundleresources/entitlements/com.apple.developer.energykit.loadevents-experience), the Home app displays your submitted events in a summarized layout. Add this entitlement to your app target in Xcode to enable Home app integration.

The Home app displays:

- **Activity logs**: A timeline of status events with charging reasons and timestamps that explain what happens during each charging session.
- **Historical charts**: Up to five years of energy consumption data with cleanliness and cost breakdowns.
- **Trend notifications**: Monthly summaries that inform people about their charging patterns and opportunities for improvement.
- **Whole-home overlays**: Correlation between vehicle charging and total home energy consumption when people connect their utility account.

The combination of the information in these displays handles the insights UI on the behalf of your app, while also providing a consistent experience across all energy devices in a person’s home. People can view their vehicle’s charging history alongside thermostat’s energy usage, in addition to whole-home consumption in one place.

The Home app displays device names according to the [`ElectricalLoadDevice`](electricalloaddevice.md) instances your app configures. Choose clear and meaningful names. Status event reasons appear in plain language to help people understand why their vehicle charges at specific times.

## See Also

- [Optimizing home electricity usage](optimizing-home-electricity-usage.md)
  Shift electric vehicle charging schedules to times when the grid is cleaner and potentially less expensive.
- [EnergyKit Entitlement](../bundleresources/entitlements/com.apple.developer.energykit.md)
  The entitlement the system requires for an app to use the EnergyKit framework.
- [EnergyKit LoadEvents Entitlement](../bundleresources/entitlements/com.apple.developer.energykit.loadevents-experience.md)
  An entitlement that works with the EnergyKit framework to share energy data and usage insights in the Home app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/providing-informative-charging-history-for-electric-vehicles)*