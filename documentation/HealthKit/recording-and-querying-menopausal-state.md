# Recording and querying menopausal state

**Framework**: HealthKit

Personalize someone’s experience on a health app by tracking the information they record on menopausal state.

#### Overview

Apps that support reproductive health tracking can use HealthKit to record and query information about whether a person reports a menopausal or nonmenopausal state. Each sample represents an entry that records the state that applies at a specific date: menopause, perimenopause, or neither.

Unlike other health data that spans durations, menopausal state samples are point-in-time records. The framework requires that the start date and end date of each sample be identical. Your app can query these samples and interpret them to determine state transitions, active periods, and current menopausal state.

#### Ask for Permission

To begin reading menopausal state data, request authorization from the person. Create an [`HKCategoryType`](hkcategorytype.md) instance using the [`menopausalState`](hkcategorytypeidentifier/menopausalstate.md) identifier, then request the appropriate permissions.

```swift
import HealthKit

let store = HKHealthStore()
let menopausalStateType = HKCategoryType(.menopausalState)

// Request read and write access.
try await store.requestAuthorization(
    toShare: [menopausalStateType], 
    read: [menopausalStateType]
)
```

If your app only needs to read existing menopausal state data without saving new samples, request read-only access by passing an empty set to the `toShare` parameter.

#### Save a Menopausal State Entry

Create an [`HKCategorySample`](hkcategorysample.md) instance with a [`HKCategoryValueMenopausalState`](hkcategoryvaluemenopausalstate.md) value. Set both the start date and end date to the same date to create a point-in-time entry.

```swift
let date = Date()
let sample = HKCategorySample(
    type: menopausalStateType,
    value: HKCategoryValueMenopausalState.perimenopause.rawValue,
    start: date,
    end: date
)

try await store.save(sample)
```

The framework validates that the start and end dates are identical. An error results if you attempt to save a sample that contains different dates.

#### Record a Nonmenopausal State

Use the [`HKCategoryValueMenopausalState.none`](hkcategoryvaluemenopausalstate/none.md) value to record when someone confirms that they have neither menopause nor perimenopause at a specific date. This value doesn’t represent unknown or missing data.

```swift
let confirmationDate = Date()
let sample = HKCategorySample(
    type: menopausalStateType,
    value: HKCategoryValueMenopausalState.none.rawValue,
    start: confirmationDate,
    end: confirmationDate
)

try await store.save(sample)
```

Record the confirmed nonmenopausal state to complete the timeline and distinguish between dates when someone actively indicates no menopausal state versus dates that lack recorded information.

#### Query Menopausal State Samples

Query menopausal state samples using the query APIs; create a predicate filter for a date range and sort the results by the start date.

```swift
let calendar = Calendar.current
let startDate = calendar.date(from: DateComponents(year: 2026, month: 1, day: 1))!
let endDate = calendar.date(from: DateComponents(year: 2027, month: 1, day: 1))!

let predicate = HKQuery.predicateForSamples(
    withStart: startDate,
    end: endDate,
    options: .strictStartDate
)

let descriptor = HKSampleQueryDescriptor(
    predicates: [.categorySample(type: menopausalStateType, predicate: predicate)],
    sortDescriptors: [SortDescriptor(\.startDate, order: .forward)]
)

let samples = try await descriptor.result(for: store)
```

The query returns an array of [`HKCategorySample`](hkcategorysample.md) instances ordered by date. Each sample contains a point-in-time menopausal state value.

#### Interpret the Timeline

Apps derive higher-level interpretations from the ordered samples. For example, consider a timeline with the following samples:

- [`HKCategoryValueMenopausalState.perimenopause`](hkcategoryvaluemenopausalstate/perimenopause.md) on January 1, 2026
- [`HKCategoryValueMenopausalState.none`](hkcategoryvaluemenopausalstate/none.md) on March 1, 2026
- [`HKCategoryValueMenopausalState.menopause`](hkcategoryvaluemenopausalstate/menopause.md) on June 1, 2026

One interpretation is that perimenopause applied from January 1 until March 1, no menopausal state applied from March 1 until June 1, and menopause began on June 1.

```swift
// Interpret samples to determine active periods.
for (index, sample) in samples.enumerated() {
    guard let value = HKCategoryValueMenopausalState(rawValue: sample.value) else {
        continue
    }
    
    let startDate = sample.startDate
    let endDate = index < samples.count - 1 ? samples[index + 1].startDate : Date()
    
    switch value {
    case .perimenopause:
        // Perimenopause was active from startDate to endDate.
        print("Perimenopause: \(startDate) to \(endDate)")
        
    case .menopause:
        // Menopause was active from startDate to endDate.
        print("Menopause: \(startDate) to \(endDate)")
        
    case .none:
        // No menopausal state from startDate to endDate.
        print("No menopausal state: \(startDate) to \(endDate)")
        
    @unknown default:
        break
    }
}
```

#### Handle Conflicting Samples

In some cases, multiple apps might record different menopausal state values on the same date. When presenting this data, consider prioritizing samples in the following order to match the Health app’s behavior: menopause, then perimenopause, then none. This hierarchy ensures that when conflicts occur, the app displays the most clinically significant state.

```swift
// Group samples by date and select the most significant value.
let samplesByDate = Dictionary(grouping: samples) { sample in
    Calendar.current.startOfDay(for: sample.startDate)
}

for (date, samplesOnDate) in samplesByDate.sorted(by: { $0.key < $1.key }) {
    let prioritizedSample = samplesOnDate.max { lhs, rhs in
        // Menopause (1) > Perimenopause (2) > None (3).
        lhs.value > rhs.value
    }
    
    // Use the prioritized sample for this date.
    if let sample = prioritizedSample {
        // Display or process the most significant state.
    }
}
```

#### React to Changes in Menopausal State

Apps can use menopausal state information to personalize someone’s experience. For example, when someone enters menopause, an app might disable menstrual cycle predictions, hide fertility tracking features, and emphasize symptom-logging related to menopause.

```swift
// Determine the current menopausal state.
let mostRecentSample = samples.last
let currentState = mostRecentSample.flatMap { 
    HKCategoryValueMenopausalState(rawValue: $0.value) 
}

switch currentState {
case .menopause:
    // Disable cycle predictions and notifications.
    // Emphasize menopause-related symptom tracking.
    break
    
case .perimenopause:
    // Adjust cycle predictions for variability.
    // Surface perimenopause-specific health information.
    break
    
case .none, nil:
    // Continue standard reproductive health tracking.
    break
    
@unknown default:
    break
}
```

## See Also

- [static let menopausalState: HKCategoryTypeIdentifier](hkcategorytypeidentifier/menopausalstate.md)
  An identifier for samples that record a person’s menopausal state.
- [static let bleedingAfterMenopause: HKCategoryTypeIdentifier](hkcategorytypeidentifier/bleedingaftermenopause.md)
  An identifier for samples that record bleeding after menopause.
- [enum HKCategoryValueMenopausalState](hkcategoryvaluemenopausalstate.md)
  A value that indicates the menopausal state at a recorded point in time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/recording-and-querying-menopausal-state)*