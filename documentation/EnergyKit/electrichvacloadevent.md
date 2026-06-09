# ElectricHVACLoadEvent

**Framework**: EnergyKit  
**Kind**: struct

A measurement of the electricity consumed by an HVAC system.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct ElectricHVACLoadEvent
```

#### Overview

Submit events representing electricity consumption to provide insights about electricity usage and your managed devices’ adherence to [`ElectricityGuidance`](electricityguidance.md). These events are data points recorded at specific points in time for a given [`EnergyVenue`](energyvenue.md) that allow the venue to determine when the device used electricity and the electricity’s cleanliness based on historical guidance. The framework can also determine relative cost using the rate plan at the energy venue, if available.

After you submit load events to report the electricity consumption of HVAC devices, you can request insights through [`ElectricityInsightQuery`](electricityinsightquery.md). When you adopt the [`EnergyKit LoadEvents Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.energykit.loadevents-experience), the Home app displays your device’s energy usage with the device name you provide.

> ❗ **Important**: The system stores and syncs the energy data that you provide through load events with end-to-end encryption through the entire process, ensuring the data isn’t accessible to anyone, even Apple. For more information, see [`EnergyKit data security`](https://developer.apple.comhttps://support.apple.com/guide/security/secd0a47c14c).

##### Submit Electrical Hvac Load Events

Save data to the load event when the heating or cooling stage changes. An electric HVAC load event provides information about the state transitions of the HVAC unit when it’s actively consuming energy.

Significant changes may include:

- A person initiated an action
- A pause in power consumption such as going idle
- The heating or cooling stage changed

Idle devices between heating or cooling cycles don’t generate events. The device that requested [`ElectricityGuidance`](electricityguidance.md) must submit the corresponding load events. Load events for an [`EnergyVenue`](energyvenue.md) are accessible to all people that use the Home app.

## Topics

### Creating an electrical load event
- [init(timestamp: Date, measurement: ElectricHVACLoadEvent.ElectricalMeasurement, session: ElectricHVACLoadEvent.Session, device: ElectricalLoadDevice)](electrichvacloadevent/init(timestamp:measurement:session:device:).md)
  Creates an electric HVAC load event.
### Getting load event information
- [let id: UUID](electrichvacloadevent/id.md)
  The unique identifier of the electrical load event.
- [let timestamp: Date](electrichvacloadevent/timestamp.md)
  The timestamp for when the event occurred.
- [let session: ElectricHVACLoadEvent.Session](electrichvacloadevent/session-swift.property.md)
  The session information.
- [ElectricHVACLoadEvent.Session](electrichvacloadevent/session-swift.struct.md)
  A session that tracks the event.
### Getting device information
- [let deviceID: String](electrichvacloadevent/deviceid.md)
  The device’s unique stable identifier.
- [var deviceName: String](electrichvacloadevent/devicename.md)
  A human-readable name for the device.
### Getting electrical measurements
- [let measurement: ElectricHVACLoadEvent.ElectricalMeasurement](electrichvacloadevent/measurement.md)
  The electricity consumption of a device.
- [ElectricHVACLoadEvent.ElectricalMeasurement](electrichvacloadevent/electricalmeasurement.md)
  A description of the electricity consumed by a device.
### Deprecated
- [init(timestamp: Date, measurement: ElectricHVACLoadEvent.ElectricalMeasurement, session: ElectricHVACLoadEvent.Session, deviceID: String)](electrichvacloadevent/init(timestamp:measurement:session:deviceid:).md)
  Creates an electric HVAC load event.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [ElectricalLoadEventProtocol](electricalloadeventprotocol.md)
- [Encodable](../Swift/Encodable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/energykit/electrichvacloadevent)*