# Logging symptoms associated with a medication

**Framework**: HealthKit

Fetch medications and dose events from the HealthKit store, and create symptom samples to associate with them.

#### Overview

> **Note**: This sample code project is associated with WWDC25 session 321: [`Meet the HealthKit Medications API`](https://developer.apple.comhttps://developer.apple.com/wwdc25/321/).

##### Configure the Sample Code Project

Before you run the sample code project:

1. Open the sample with the latest version of Xcode.
2. Set the developer team for the project target to let Xcode automatically manage the provisioning profile. For more information, see [`Preparing your app for distribution`](https://developer.apple.com/documentation/Xcode/preparing-your-app-for-distribution) and [`Preparing your app for distribution`](https://developer.apple.com/documentation/Xcode/preparing-your-app-for-distribution).

To play with the sample app:

1. Launch the Health app on your iPhone, select the Browse tab, and tap Medications.
2. In the Medications view, add Acetaminophen 500 mg Oral Capsule, Carbinoxamine Maleate Biphasic Release Oral Capsule (10 mg), or Ciprofloxacin Injection 200 mg/20 mL as a sample medication. The sample app associates symptoms with these three medications using their RxNorm codes by mapping the codes to their symptoms in the `SideEffects` dictionary in `SideEffects.swift`.
3. For each medication, log a dose as  in the As Needed Medications section. The sample app forms a predicate to only look for doses marked as `taken`.
4. Build and run the sample app on the iPhone to see the medication list after providing authorization. Tap a medication to see the most-recent dose event and associated symptoms. When tapping a medication, an additional authorization sheet prompts for authorization to access symptoms data.
5. To add more medications in the Health app and view them in the sample app, add their RxNorm codes to the `SideEffects` dictionary, along with their associated symptoms. For instance, for piroxicam, the RxNorm code is 105929, and the symptoms can be headache, loss of appetite, and nausea. To view the symptoms, modify `SideEffects` by adding the following code:

```None
"105929": [SymptomModel(name: "Headache", categoryID: .headache),
			SymptomModel(name: "Diarrhea", categoryID: .diarrhea),
			SymptomModel(name: "Nausea", categoryID: .nausea)]
```

1. Log doses for medications over time, and observe them in the Charts tab of the sample app.

## See Also

- [Saving data to HealthKit](saving-data-to-healthkit.md)
  Create and share HealthKit samples.
- [Reading data from HealthKit](reading-data-from-healthkit.md)
  Use queries to request sample data from HealthKit.
- [class HKHealthStore](hkhealthstore.md)
  The access point for all data managed by HealthKit.
- [Creating a Mobility Health App](creating-a-mobility-health-app.md)
  Create a health app that allows a clinical care team to send and receive mobility data.
- [Data types](data-types.md)
  Specify the kind of data used in HealthKit.
- [Samples](samples.md)
  Create and save health and fitness samples.
- [Queries](queries.md)
  Query health and fitness data.
- [Visualizing HealthKit State of Mind in visionOS](visualizing-healthkit-state-of-mind-in-visionos.md)
  Incorporate HealthKit State of Mind into your app and visualize the data in visionOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/logging-symptoms-associated-with-a-medication)*