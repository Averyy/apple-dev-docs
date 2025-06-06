# Getting movement disorder symptom data

**Framework**: Core Motion

Retrieve data from the Apple Watch’s movement disorder manager.

#### Overview

The [`CMMovementDisorderManager`](cmmovementdisordermanager.md) class provides a power-efficient approach for you to continuously measure and record tremors and dyskinetic symptoms for Parkinson’s disease for your app.

> ❗ **Important**:  Apple doesn’t market the movement disorder monitoring as a regulated medical device. Depending on how your app uses the API, you may need to meet additional regulatory obligations. Seek the relevant regulatory advice as needed for your app.

 Apple doesn’t market the movement disorder monitoring as a regulated medical device. Depending on how your app uses the API, you may need to meet additional regulatory obligations. Seek the relevant regulatory advice as needed for your app.

When you begin retrieving data from the movement disorder manager, Apple Watch starts to gather motion data. To preserve battery life, the manager doesn’t perform calculations in real time. Instead, it periodically and opportunistically analyzes the raw data, saving the results on the user’s device. To preserve disk space, the manager only keeps results for seven days. During this time, you can use the manager to query for the results.

For more information about the scientific validation and algorithms behind disorder detection and recording, see [`Smartwatch inertial sensors continuously monitor real-world motor fluctuations in Parkinson’s disease`](https://developer.apple.comhttp://stm.sciencemag.org/cgi/content/full/13/579/eabd7865?ijkey=Md/cIhqXrFvws&keytype=ref&siteid=scitransmed), or download a PDF from [`Science Translational Medicine Magazine`](https://developer.apple.comhttps://stm.sciencemag.org/content/scitransmed/13/579/eabd7865.full.pdf?ijkey=Md/cIhqXrFvws&keytype=ref&siteid=scitransmed).

Apps that use the `CMMovementDisorderManager` must:

- Confirm the user’s diagnosis of Parkinson’s disease.
- Only report on symptoms diagnosed by a clinician or self-reported by the user.
- Remind the user to wear Apple Watch on their most affected arm in order to collect the most useful data.

> ❗ **Important**:  To use the Movement Disorder API, your app must adhere to the Movement Disorder Program Requirements. For more information, see [`Adhering to the movement disorder data collection requirements`](adhering-to-the-movement-disorder-data-collection-requirements.md). Additionally, your app must follow best practices for handling the user’s health data, as defined by the HealthKit guidelines. For more information, see [`Protecting user privacy`](https://developer.apple.com/documentation/HealthKit/protecting-user-privacy).

 To use the Movement Disorder API, your app must adhere to the Movement Disorder Program Requirements. For more information, see [`Adhering to the movement disorder data collection requirements`](adhering-to-the-movement-disorder-data-collection-requirements.md). Additionally, your app must follow best practices for handling the user’s health data, as defined by the HealthKit guidelines. For more information, see [`Protecting user privacy`](https://developer.apple.com/documentation/HealthKit/protecting-user-privacy).

To retrieve Parkinson’s tremors or dyskinetic symptoms data from a watchOS app:

1. Provide a motion usage description in your WatchKit extension’s `Info.plist` file.
2. Instantiate a [`CMMovementDisorderManager`](cmmovementdisordermanager.md) object.
3. Ensure that movement disorder monitoring is available on the current device.
4. Begin monitoring the user.
5. Query for tremors or dyskinetic symptoms.

##### Provide the Motion Usage Description

Your watchOS app must provide an [`NSMotionUsageDescription`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Reference/InfoPlistKeyReference/Articles/CocoaKeys.html#//apple_ref/doc/plist/info/NSMotionUsageDescription) key with a `String` value in the WatchKit extension’s `Info.plist` file. The system displays the motion usage description whenever it asks a user for permission to record their data. The description string appears in the Motion and Fitness authorization prompt.

At a minimum, your description must contain the following text: “In addition, this app would like to access your tremor and dyskinetic symptom data. This is only intended for use in those already diagnosed with Parkinson’s disease.”

You can include additional information explaining why the user should grant your app permission, and what your app intends to do with the data after this text.

##### Monitor and Query for Results

The following example shows how to set up your movement disorder manager, and begin monitoring the user’s symptoms:

```swift
// Check to see if the movement disorder manager is available.
guard CMMovementDisorderManager.isAvailable() else {
    // The movement disorder manager is not availble on this device.
    return
}

// Instantiate the Movement Disorder Manager
movementDisorderManager = CMMovementDisorderManager()

// Start monitoring the user. The maximum duration is seven days.
movementDisorderManager.monitorKinesias(forDuration: 60.0 * 60.0 * 24.0 * 7.0)
```

After you start monitoring, the manager leverages the [`CMSensorRecorder`](cmsensorrecorder.md) to record high-rate accelerometer data passively. When enabled, the [`CMSensorRecorder`](cmsensorrecorder.md) records 100 Hz samples. The movement disorder algorithms then periodically and opportunistically use this data to calculate tremors and dyskinetic symptoms.

The movement disorder manager stores the results of these calculations on the device for seven days. To access the results, use the manager to query for the desired results, as shown in this example:

```swift
// Get the end date for the last batch of results.
guard let endDate = movementDisorderManager.lastProcessedDate() else {
    // The manager has not processed any results yet.
    return
}

// Get the last batch of tremor results.
movementDisorderManager.queryTremor(from: previousDate, to: endDate) { (tremorResults, error) in
    
    // Check for errors.
    if let error = error {
        // Handle the error here.
        print("*** An error occurred: \(error.localizedDescription) ***")
        return
    }
    
    // Do something with the tremor results here.
}

// Get the last batch of dyskinetic symptom results.
movementDisorderManager.queryDyskineticSymptom(from: previousDate, to: endDate) { (dyskineticSymptomResults, error) in
    
    // Check for errors.
    if let error = error {
        // Handle the error here.
        print("*** An error occurred: \(error.localizedDescription) ***")
        return
    }
    
    // Do something with the dyskinetic symptom results here.
}

previousDate = endDate
```

To extend the monitoring past the initial expiration date, call the [`monitorKinesias(forDuration:)`](cmmovementdisordermanager/monitorkinesias(forduration:).md) method again.

##### Understand the Managers Limitations

[`CMMovementDisorderManager`](cmmovementdisordermanager.md) measures resting tremors from Parkinson’s disease in the 3-7 Hz range. It returns metrics about the presence and relative severity of resting tremor as a [`CMTremorResult`](cmtremorresult.md) object. The [`CMMovementDisorderManager`](cmmovementdisordermanager.md) also computes metrics about choreiform dyskinetic symptoms, measuring the likely presence or absence of dyskinetic symptoms as observed at the wrist where the user wears their Apple Watch. It returns the results as [`CMDyskineticSymptomResult`](cmdyskineticsymptomresult.md) objects.

[`CMMovementDisorderManager`](cmmovementdisordermanager.md) operates under the following constraints:

- The user should wear Apple Watch on the most affected arm.
- Employ dyskinetic symptom tracking only for users who have chorea on the affected arm, either self-reported or diagnosed by a clinician.
- There are many types of tremors. The movement disorder manager explicitly tracks resting tremor; it doesn’t track action tremor or postural tremor, and it may not track finger tremor.
- The manager doesn’t explicitly track dystonia.
- The results may include false positives and false negatives. The user’s activity, watch band fit, and concomitant conditions (such as restless legs syndrome and non-Parkinsonian tremor) can affect the quality of the results.

The manager only explicitly measures symptoms from the wrist wearing Apple Watch. However, Apple Watch may sense symptoms transmitted through the body from other affected body parts, possibly resulting in misleading or false metrics.

## See Also

- [Adhering to the movement disorder data collection requirements](adhering-to-the-movement-disorder-data-collection-requirements.md)
  Ensure that your users understand and have control over the data your app collects.
- [Movement disorder algorithm changelog](movement-disorder-algorithm-changelog.md)
  A chronological log of notable changes to the movement disorder algorithm.
- [class CMMovementDisorderManager](cmmovementdisordermanager.md)
  A manager for recording and querying movement disorder data.
- [class CMTremorResult](cmtremorresult.md)
  A result object that contains data about the presence and strength of tremors during a one-minute interval.
- [class CMDyskineticSymptomResult](cmdyskineticsymptomresult.md)
  A result object that contains data about the likely presence of dyskinetic symptoms during a one-minute interval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/getting-movement-disorder-symptom-data)*