# CMMovementDisorderManager

**Framework**: Core Motion  
**Kind**: class

A manager for recording and querying movement disorder data.

**Availability**:
- watchOS 5.0+

## Declaration

```swift
class CMMovementDisorderManager
```

## Mentions

- [Getting movement disorder symptom data](getting-movement-disorder-symptom-data.md)

#### Overview

> ❗ **Important**:  Only collect data from patients clinically diagnosed with a movement disorder. This API is not designed to collect data from users who have not been diagnosed with a movement disorder. All medical decisions should be made through the guidance of a licensed clinician. For more information, see [`Adhering to the movement disorder data collection requirements`](adhering-to-the-movement-disorder-data-collection-requirements.md).

 Only collect data from patients clinically diagnosed with a movement disorder. This API is not designed to collect data from users who have not been diagnosed with a movement disorder. All medical decisions should be made through the guidance of a licensed clinician. For more information, see [`Adhering to the movement disorder data collection requirements`](adhering-to-the-movement-disorder-data-collection-requirements.md).

Use `CMMovementDisorderManager` to measure a resting Parkinsonian tremor in the 3-7 Hz range and choreiform dyskinetic symptoms. When collecting data, the user should wear Apple Watch on their most affected arm.

`CMMovementDisorderManager` requires an entitlement from Apple. To apply for the entitlement, see [`Movement Disorder Entitlement Request`](https://developer.apple.comhttps://developer.apple.com/contact/request/movement-disorder-api-entitlement/).

> ❗ **Important**:  To use this API, you must include the [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) key in your app’s `Info.plist` file and provide a usage description string for this key. The usage description appears in the prompt that the user must accept the first time the system asks the user to access motion data for your app. If you don’t include a usage description string, your app crashes when you call this API.

 To use this API, you must include the [`NSMotionUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSMotionUsageDescription) key in your app’s `Info.plist` file and provide a usage description string for this key. The usage description appears in the prompt that the user must accept the first time the system asks the user to access motion data for your app. If you don’t include a usage description string, your app crashes when you call this API.

## Topics

### Checking Availablility
- [class func isAvailable() -> Bool](cmmovementdisordermanager/isavailable.md)
  A Boolean value indicating whether the current device supports the movement disorder manager.
- [class func authorizationStatus() -> CMAuthorizationStatus](cmmovementdisordermanager/authorizationstatus.md)
  A value indicating whether the user has authorized the app to monitor and query for movement disorder data.
- [class func version() -> String?](cmmovementdisordermanager/version.md)
  Returns a string that describes the movement disorder algorithm’s current version.
### Recording Movement Disorders
- [func monitorKinesias(forDuration: TimeInterval)](cmmovementdisordermanager/monitorkinesias(forduration:).md)
  Calculate and store tremor and dyskinetic symptom results for the duration of the specified time interval.
- [func monitorKinesiasExpirationDate() -> Date?](cmmovementdisordermanager/monitorkinesiasexpirationdate.md)
  Returns the expiration date for the most recent monitoring period.
### Querying for Movement Disorders
- [func queryTremor(from: Date, to: Date, withHandler: CMTremorResultHandler)](cmmovementdisordermanager/querytremor(from:to:withhandler:).md)
  Query for tremor results from the provided time interval.
- [typealias CMTremorResultHandler](cmtremorresulthandler.md)
  A completion handler for accessing and processing tremor results.
- [func queryDyskineticSymptom(from: Date, to: Date, withHandler: CMDyskineticSymptomResultHandler)](cmmovementdisordermanager/querydyskineticsymptom(from:to:withhandler:).md)
  Query for dyskinetic symptoms from the provided time interval.
- [typealias CMDyskineticSymptomResultHandler](cmdyskineticsymptomresulthandler.md)
  A completion handler for processing dyskinetic symptom results.
- [func lastProcessedDate() -> Date?](cmmovementdisordermanager/lastprocesseddate.md)
  Returns the date of the most recently calculated results.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Getting movement disorder symptom data](getting-movement-disorder-symptom-data.md)
  Retrieve data from the Apple Watch’s movement disorder manager.
- [Adhering to the movement disorder data collection requirements](adhering-to-the-movement-disorder-data-collection-requirements.md)
  Ensure that your users understand and have control over the data your app collects.
- [Movement disorder algorithm changelog](movement-disorder-algorithm-changelog.md)
  A chronological log of notable changes to the movement disorder algorithm.
- [class CMTremorResult](cmtremorresult.md)
  A result object that contains data about the presence and strength of tremors during a one-minute interval.
- [class CMDyskineticSymptomResult](cmdyskineticsymptomresult.md)
  A result object that contains data about the likely presence of dyskinetic symptoms during a one-minute interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmovementdisordermanager)*