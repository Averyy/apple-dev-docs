# Adhering to the movement disorder data collection requirements

**Framework**: Core Motion

Ensure that your users understand and have control over the data your app collects.

#### Overview

When using the movement disorder APIs, it’s critical that your app provides a transparent data collection experience. Your app must display an introductory screen that describes its data use policy. Additionally, some data types require specific disclosures.

> ❗ **Important**:  Apps that offer movement disorders monitoring must adhere to the [`Movement Disorder API Addendum`](https://developer.apple.comhttps://developer.apple.com/contact/request/movement-disorder-api-entitlement/). Note that only Apple Developer Program account holders can access the addendum. In addition, all health-related apps must follow best practices for handling the user’s health data, as defined by the HealthKit guidelines (see [`Protecting user privacy`](https://developer.apple.com/documentation/HealthKit/protecting-user-privacy)).

##### Explain Your Apps Data Use Policy

Apps that perform movement disorder monitoring must display an introduction screen when the user first launches the app. This screen must describe the following:

- The app’s purpose and target audience.
- The data that your app collects during movement disorder monitoring.
- How you plan to use the data.
- Whether your app collects data while running in the background.
- Instructions on how to opt out of data collection in the future.

##### Include Required Disclosures

For some types of data, your app must include additional text in the introduction screen. For each of the following situations, add the specified text:

- **Resting tremor data**: “This app is monitoring and collecting your Parkinsonian resting tremor data, only if you self-report or have been clinically diagnosed with resting tremor, and indicate within the app that this is true.”
- **Choreiform dyskinesia data**: “This app is monitoring and collecting your choreiform dyskinesia data, only if you self-report or have been clinically diagnosed with choreiform dyskinesias, and indicate within the app that this is true.”
- **Movement disorder data in the background**: “This app is able to collect your movement disorder data even when the app is not active, on screen, or responding to your user input.”

## See Also

- [Getting movement disorder symptom data](getting-movement-disorder-symptom-data.md)
  Retrieve data from the Apple Watch’s movement disorder manager.
- [Movement disorder algorithm changelog](movement-disorder-algorithm-changelog.md)
  A chronological log of notable changes to the movement disorder algorithm.
- [class CMMovementDisorderManager](cmmovementdisordermanager.md)
  A manager for recording and querying movement disorder data.
- [class CMTremorResult](cmtremorresult.md)
  A result object that contains data about the presence and strength of tremors during a one-minute interval.
- [class CMDyskineticSymptomResult](cmdyskineticsymptomresult.md)
  A result object that contains data about the likely presence of dyskinetic symptoms during a one-minute interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/adhering-to-the-movement-disorder-data-collection-requirements)*