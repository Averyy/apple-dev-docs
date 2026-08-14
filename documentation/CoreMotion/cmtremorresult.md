# CMTremorResult

**Framework**: Core Motion  
**Kind**: class

A result object that contains data about the presence and strength of tremors during a one-minute interval.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class CMTremorResult
```

## Mentions

- [Getting movement disorder symptom data](getting-movement-disorder-symptom-data.md)

#### Overview

The following equation is always true: [`percentUnknown`](cmtremorresult/percentunknown.md) `+` [`percentNone`](cmtremorresult/percentnone.md) `+` [`percentSlight`](cmtremorresult/percentslight.md) `+` [`percentMild`](cmtremorresult/percentmild.md) `+` [`percentModerate`](cmtremorresult/percentmoderate.md) `+` [`percentStrong`](cmtremorresult/percentstrong.md) `= 1.0`.

## Topics

### Reading the Time Interval
- [var startDate: Date](cmtremorresult/startdate.md)
  The result’s start time and date.
- [var endDate: Date](cmtremorresult/enddate.md)
  The result’s end time and date.
### Accessing Tremor Data
- [var percentUnknown: Float](cmtremorresult/percentunknown.md)
  The percentage of time when the algorithm couldn’t make a determination.
- [var percentNone: Float](cmtremorresult/percentnone.md)
  The percentage of time when no tremor was detected.
- [var percentSlight: Float](cmtremorresult/percentslight.md)
  The percentage of time when a tremor was likely, and the displacement amplitude was slight.
- [var percentMild: Float](cmtremorresult/percentmild.md)
  The percentage of time when a tremor was likely, and the displacement amplitude was mild.
- [var percentModerate: Float](cmtremorresult/percentmoderate.md)
  The percentage of time when a tremor was likely, and the displacement amplitude was moderate.
- [var percentStrong: Float](cmtremorresult/percentstrong.md)
  The percentage of time when a tremor was likely, and the displacement amplitude was strong.
### Initializers
- [init?(coder: NSCoder)](cmtremorresult/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [Getting movement disorder symptom data](getting-movement-disorder-symptom-data.md)
  Retrieve data from the Apple Watch’s movement disorder manager.
- [Adhering to the movement disorder data collection requirements](adhering-to-the-movement-disorder-data-collection-requirements.md)
  Ensure that your users understand and have control over the data your app collects.
- [Movement disorder algorithm changelog](movement-disorder-algorithm-changelog.md)
  A chronological log of notable changes to the movement disorder algorithm.
- [class CMMovementDisorderManager](cmmovementdisordermanager.md)
  A manager for recording and querying movement disorder data.
- [class CMDyskineticSymptomResult](cmdyskineticsymptomresult.md)
  A result object that contains data about the likely presence of dyskinetic symptoms during a one-minute interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmtremorresult)*