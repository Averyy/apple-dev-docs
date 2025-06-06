# Movement disorder algorithm changelog

**Framework**: Core Motion

A chronological log of notable changes to the movement disorder algorithm.

#### Overview

The movement disorder algorithm measures and records tremors and dyskinetic symptoms for Parkinson’s disease. For more information on receiving and using this data, see [`Getting movement disorder symptom data`](getting-movement-disorder-symptom-data.md).

##### Unreleased

- The [`version()`](cmmovementdisordermanager/version().md) method for checking the algorithm’s current version is available in watchOS 9.

##### 100 2018 07 17

###### Added

- Released the algorithm used in watchOS 5 and later.

## See Also

- [Getting movement disorder symptom data](getting-movement-disorder-symptom-data.md)
  Retrieve data from the Apple Watch’s movement disorder manager.
- [Adhering to the movement disorder data collection requirements](adhering-to-the-movement-disorder-data-collection-requirements.md)
  Ensure that your users understand and have control over the data your app collects.
- [class CMMovementDisorderManager](cmmovementdisordermanager.md)
  A manager for recording and querying movement disorder data.
- [class CMTremorResult](cmtremorresult.md)
  A result object that contains data about the presence and strength of tremors during a one-minute interval.
- [class CMDyskineticSymptomResult](cmdyskineticsymptomresult.md)
  A result object that contains data about the likely presence of dyskinetic symptoms during a one-minute interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/movement-disorder-algorithm-changelog)*