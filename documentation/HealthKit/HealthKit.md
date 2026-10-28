# HealthKit

**Framework**: HealthKit  
**Kind**: module  
**Role**: Framework

Access and share health and fitness data while maintaining the user’s privacy and control.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 2.0+

## Overview

HealthKit provides a central repository for health and fitness data on iPhone and Apple Watch. With the user’s permission, apps communicate with the HealthKit store to access and share this data.

![An image showing the Health app summary screen.](https://developer.apple.com/tutorials/images/com.apple.healthkit/health-summary@2x.png)

Creating a complete, personalized health and fitness experience includes a variety of tasks:

- Collecting and storing health and fitness data
- Analyzing and visualizing the data
- Enabling social interactions

HealthKit apps take a collaborative approach to building this experience. Your app doesn’t need to provide all of these features. Instead, you can focus just on the subset of tasks that most interests you.

For example, users can select their favorite weight-tracking, step-counting, and health challenge app, each calibrated to their personal needs. Because HealthKit apps freely exchange data (with user permission), the combined suite provides a more customized experience than any single app on its own. For example, when a group of friends joins a daily step-counting challenge, each person can use their preferred hardware device and app to track their steps, while everyone in the group uses the same social app for the challenge.

HealthKit is also designed to manage and merge data from multiple sources. For example, users can view and manage all of their data in the Health App, including adding data, deleting data, and changing an app’s permissions. Therefore, your app needs to handle these changes, even when they occur outside your app.

> **Note**:  Because health data may contain sensitive, personal information, apps must receive permission from the user to read data from or write data to the HealthKit store. They must also take steps to protect that data at all times. For more information, see [Protecting user privacy](./protecting-user-privacy.md).

## Topics

### Essentials
- [About the HealthKit framework](./about-the-healthkit-framework.md)
  Learn about the architecture and design of the HealthKit framework.
- [Setting up HealthKit](./setting-up-healthkit.md)
  Set up and configure your HealthKit store.
- [Authorizing access to health data](./authorizing-access-to-health-data.md)
  Request permission to read and share data in your app.
- [Protecting user privacy](./protecting-user-privacy.md)
  Respect and safeguard your user’s privacy.
- [HealthKit updates](../Updates/healthkit.md)
  Learn about important changes to HealthKit.
- [HealthKitUI](../HealthKitUI/HealthKitUI.md)
  Display user interface that enables a person to view and interact with their health data.
### Health data
- [Saving data to HealthKit](./saving-data-to-healthkit.md)
  Create and share HealthKit samples.
- [Reading data from HealthKit](./reading-data-from-healthkit.md)
  Use queries to request sample data from HealthKit.
- [class HKHealthStore](./hkhealthstore.md)
  The access point for all data managed by HealthKit.
- [Creating a Mobility Health App](./creating-a-mobility-health-app.md)
  Create a health app that allows a clinical care team to send and receive mobility data.
- [Data types](./data-types.md)
  Specify the kind of data used in HealthKit.
- [Samples](./samples.md)
  Create and save health and fitness samples.
- [Queries](./queries.md)
  Query health and fitness data.
- [Visualizing HealthKit State of Mind in visionOS](./visualizing-healthkit-state-of-mind-in-visionos.md)
  Incorporate HealthKit State of Mind into your app and visualize the data in visionOS.
- [Logging symptoms associated with a medication](./logging-symptoms-associated-with-a-medication.md)
  Fetch medications and dose events from the HealthKit store, and create symptom samples to associate with them.
### Workout data
- [Workouts and activity rings](./workouts-and-activity-rings.md)
  Manage workouts, workout sessions, and activity summaries.
### Errors
- [struct HKError](./hkerror.md)
  An error returned from a HealthKit method.
- [let HKErrorDomain: String](./hkerrordomain.md)
  The domain for all HealthKit errors.
- [HKError.Code](./hkerror/code.md)
  Error codes returned by HealthKit.
### Reference
- [HealthKit Enumerations](./healthkit-enumerations.md)
- [HealthKit Classes](./healthkit-classes.md)
- [HealthKit Constants](./healthkit-constants.md)
- [HealthKit Data Types](./healthkit-data-types.md)
- [HealthKit Functions](./healthkit-functions.md)
- [Macros](./healthkit-macros.md)
- [HealthKit Variables](./healthkit-variables.md)
### Variables
- [HKHealthConceptDomainMedication](./hkhealthconceptdomain/medication.md)
  The domain that represents medication concepts.
- [HKMedicationGeneralFormCapsule](./hkmedicationgeneralform/capsule.md)
  The medication comes in capsule form, such as a hard-shell capsule or softgel.
- [HKMedicationGeneralFormCream](./hkmedicationgeneralform/cream.md)
  The medication is applied as a cream.
- [HKMedicationGeneralFormDevice](./hkmedicationgeneralform/device.md)
  The medication is administered through a device, such as an infusion pump for controlled fluid delivery.
- [HKMedicationGeneralFormDrops](./hkmedicationgeneralform/drops.md)
  The medication is taken as drops, for example eye drops or ear drops.
- [HKMedicationGeneralFormFoam](./hkmedicationgeneralform/foam.md)
  The medication is applied as a foam.
- [HKMedicationGeneralFormGel](./hkmedicationgeneralform/gel.md)
  The medication is applied as a gel.
- [HKMedicationGeneralFormInhaler](./hkmedicationgeneralform/inhaler.md)
  The medication is delivered through an inhaler.
- [HKMedicationGeneralFormInjection](./hkmedicationgeneralform/injection.md)
  The medication is given as an injection.
- [HKMedicationGeneralFormLiquid](./hkmedicationgeneralform/liquid.md)
  The medication is taken as a liquid, such as a syrup.
- [HKMedicationGeneralFormLotion](./hkmedicationgeneralform/lotion.md)
  The medication is applied as a lotion.
- [HKMedicationGeneralFormOintment](./hkmedicationgeneralform/ointment.md)
  The medication is applied as an ointment.
- [HKMedicationGeneralFormPatch](./hkmedicationgeneralform/patch.md)
  The medication is applied as a patch worn on the skin.
- [HKMedicationGeneralFormPowder](./hkmedicationgeneralform/powder.md)
  The medication is taken as a powder.
- [HKMedicationGeneralFormSpray](./hkmedicationgeneralform/spray.md)
  The medication is delivered as a spray, for example a nasal spray or throat spray.
- [HKMedicationGeneralFormSuppository](./hkmedicationgeneralform/suppository.md)
  The medication is delivered as a suppository.
- [HKMedicationGeneralFormTablet](./hkmedicationgeneralform/tablet.md)
  The medication comes in tablet form, such as a pill or caplet.
- [HKMedicationGeneralFormTopical](./hkmedicationgeneralform/topical.md)
  The medication is applied topically in a form that wasn’t specified.
- [HKMedicationGeneralFormUnknown](./hkmedicationgeneralform/unknown.md)
  The system doesn’t know the general form of the medication.
- [HKQuantityTypeIdentifierHeartRateVariabilityRMSSD](./hkquantitytypeidentifier/heartratevariabilityrmssd.md)
### Enumerations
- [HKMedicationDoseEventLogStatus](./hkmedicationdoseevent/logstatus-swift.enum.md)
  The statuses the system assigns to a logged medication dose event.
- [HKMedicationDoseEventScheduleType](./hkmedicationdoseevent/scheduletype-swift.enum.md)
  The kind of schedule the system associates with a logged medication dose event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/HealthKit)*