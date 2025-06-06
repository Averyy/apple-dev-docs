# CMDyskineticSymptomResult

**Framework**: Core Motion  
**Kind**: class

A result object that contains data about the likely presence of dyskinetic symptoms during a one-minute interval.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- watchOS 5.0+

## Declaration

```swift
class CMDyskineticSymptomResult
```

## Mentions

- [Getting movement disorder symptom data](getting-movement-disorder-symptom-data.md)

#### Overview

Dyskinesias are uncontrolled, involuntary movements that occur as a side effect of taking Levadopa to control Parkinson’s disease. Dyskinesias can manifest in a single body part, such as the arm, leg, or head, or they can affect the entire body. Particular dyskinesias resemble actions like fidgeting, writhing, wriggling, head bobbing, or body swaying. These symptoms tend to occur during the drug’s peak dosage. Dyskinesias typically occur in patients with advanced Parkinson’s disease, who may require higher dosages of Levadopa.

The following equation is always true: [`percentUnlikely`](cmdyskineticsymptomresult/percentunlikely.md) `+` [`percentLikely`](cmdyskineticsymptomresult/percentlikely.md) `= 1.0`.

> ❗ **Important**:  Gather and present data on dyskinetic symptom results only to users with choreiform dyskinesias, either self-reported or diagnosed by a clinician.

 Gather and present data on dyskinetic symptom results only to users with choreiform dyskinesias, either self-reported or diagnosed by a clinician.

## Topics

### Reading the Time Interval
- [var startDate: Date](cmdyskineticsymptomresult/startdate.md)
  The result’s start time and date.
- [var endDate: Date](cmdyskineticsymptomresult/enddate.md)
  The result’s end time and date.
### Accessing Dyskinetic Symptom Data
- [var percentUnlikely: Float](cmdyskineticsymptomresult/percentunlikely.md)
  The percentage of time when dyskinetic symptoms were unlikely.
- [var percentLikely: Float](cmdyskineticsymptomresult/percentlikely.md)
  The percentage of time when dyskinetic symptoms were likely.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Getting movement disorder symptom data](getting-movement-disorder-symptom-data.md)
  Retrieve data from the Apple Watch’s movement disorder manager.
- [Adhering to the movement disorder data collection requirements](adhering-to-the-movement-disorder-data-collection-requirements.md)
  Ensure that your users understand and have control over the data your app collects.
- [Movement disorder algorithm changelog](movement-disorder-algorithm-changelog.md)
  A chronological log of notable changes to the movement disorder algorithm.
- [class CMMovementDisorderManager](cmmovementdisordermanager.md)
  A manager for recording and querying movement disorder data.
- [class CMTremorResult](cmtremorresult.md)
  A result object that contains data about the presence and strength of tremors during a one-minute interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmdyskineticsymptomresult)*