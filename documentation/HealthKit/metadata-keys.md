# Metadata Keys

**Framework**: HealthKit

Constants used to add metadata to objects stored in HealthKit.

#### Overview

Use these keys to facilitate sharing data between apps. You can also create your own custom keys to give HealthKit objects additional app-specific data.

## Topics

### General Keys
- [let HKMetadataKeyExternalUUID: String](hkmetadatakeyexternaluuid.md)
  A unique identifier for an HKObject that is set by its source.
- [let HKMetadataKeyTimeZone: String](hkmetadatakeytimezone.md)
  The user’s time zone when the HealthKit object was created.
- [let HKMetadataKeyWasUserEntered: String](hkmetadatakeywasuserentered.md)
  A key that indicates whether the sample was entered by the user.
- [let HKMetadataKeyQuantityClampedToLowerBound: String](hkmetadatakeyquantityclampedtolowerbound.md)
- [let HKMetadataKeyQuantityClampedToUpperBound: String](hkmetadatakeyquantityclampedtoupperbound.md)
### Estimate Keys
- [let HKMetadataKeyDateOfEarliestDataUsedForEstimate: String](hkmetadatakeydateofearliestdatausedforestimate.md)
  The earliest date of data used to calculate the sample’s estimated value.
- [let HKMetadataKeySessionEstimate: String](hkmetadatakeysessionestimate.md)
### Device Information Keys
- [let HKMetadataKeyDeviceSerialNumber: String](hkmetadatakeydeviceserialnumber.md)
  The key for the serial number of the device that generated the data.
- [let HKMetadataKeyUDIDeviceIdentifier: String](hkmetadatakeyudideviceidentifier.md)
  The device identifier portion of a device’s UDI (unique device identifier).
- [let HKMetadataKeyUDIProductionIdentifier: String](hkmetadatakeyudiproductionidentifier.md)
  The production identifier portion of a device’s UDI (unique device identifier).
- [let HKMetadataKeyDigitalSignature: String](hkmetadatakeydigitalsignature.md)
  A digital signature that can be used to validate the origin of the HealthKit object.
- [let HKMetadataKeyDeviceName: String](hkmetadatakeydevicename.md)
  The name of the device that took this reading.
- [let HKMetadataKeyDeviceManufacturerName: String](hkmetadatakeydevicemanufacturername.md)
  The name of the manufacturer of the device that took this reading.
- [let HKMetadataKeyDevicePlacementSide: String](hkmetadatakeydeviceplacementside.md)
  The key for metadata indicating the placement of the device that measured a sample.
- [enum HKDevicePlacementSide](hkdeviceplacementside.md)
  Values that indicate the placement of the device that measured a sample.
- [let HKMetadataKeyAppleDeviceCalibrated: String](hkmetadatakeyappledevicecalibrated.md)
  The key for metadata indicating whether the system had data from a sufficient amount of calibrated sensors when recording the sample.
### Sync Keys
- [let HKMetadataKeySyncIdentifier: String](hkmetadatakeysyncidentifier.md)
  A unique string that identifies a piece of data so it can be updated and synced.
- [let HKMetadataKeySyncVersion: String](hkmetadatakeysyncversion.md)
  The version number for a piece of data, used when updating or syncing.
### Lab Keys
- [let HKMetadataKeyWasTakenInLab: String](hkmetadatakeywastakeninlab.md)
  A key that indicates whether the sample was taken in a lab.
- [let HKMetadataKeyReferenceRangeLowerLimit: String](hkmetadatakeyreferencerangelowerlimit.md)
  A key that indicates the lower limit of the reference range for a lab result.
- [let HKMetadataKeyReferenceRangeUpperLimit: String](hkmetadatakeyreferencerangeupperlimit.md)
  A key that indicates the upper limit of the reference range for a lab result.
### Weather Keys
- [let HKMetadataKeyBarometricPressure: String](hkmetadatakeybarometricpressure.md)
  The metadata key for the barometric pressure associated with a sample.
- [let HKMetadataKeyWeatherCondition: String](hkmetadatakeyweathercondition.md)
  A key that represents the weather condition during the sample.
- [let HKMetadataKeyWeatherHumidity: String](hkmetadatakeyweatherhumidity.md)
  A key that represents the weather humidity during the sample.
- [let HKMetadataKeyWeatherTemperature: String](hkmetadatakeyweathertemperature.md)
  A key that represents the weather temperature during the sample.
### Workout Keys
- [Workout Metadata Keys](workout-metadata-keys.md)
  Constants that can be used to add metadata to workouts.
### Cardio Fitness Keys
- [let HKMetadataKeyVO2MaxValue: String](hkmetadatakeyvo2maxvalue.md)
  The maximum oxygen consumption rate during exercise of increasing intensity.
- [let HKMetadataKeyLowCardioFitnessEventThreshold: String](hkmetadatakeylowcardiofitnesseventthreshold.md)
  The VO2 max threshold used to categorize low-level cardio fitness events.
### Motion Keys
- [let HKMetadataKeyUserMotionContext: String](hkmetadatakeyusermotioncontext.md)
  The person’s motion during the sample’s time period.
### Nutrition Keys
- [let HKMetadataKeyFoodType: String](hkmetadatakeyfoodtype.md)
  The type of food that the HealthKit object represents.
### Vitals Sensors Keys
- [let HKMetadataKeyBodyTemperatureSensorLocation: String](hkmetadatakeybodytemperaturesensorlocation.md)
  The location where a specific body temperature reading was taken.
- [let HKMetadataKeyHeartRateSensorLocation: String](hkmetadatakeyheartratesensorlocation.md)
  The location where a specific heart rate reading was taken.
- [let HKMetadataKeyHeartRateMotionContext: String](hkmetadatakeyheartratemotioncontext.md)
  The user’s activity level when the heart rate sample was measured.
- [let HKPredicateKeyPathAverageHeartRate: String](hkpredicatekeypathaverageheartrate.md)
  The key path for the sample’s average heart rate.
- [let HKMetadataKeyHeartRateRecoveryActivityDuration: String](hkmetadatakeyheartraterecoveryactivityduration.md)
- [let HKMetadataKeyHeartRateRecoveryActivityType: String](hkmetadatakeyheartraterecoveryactivitytype.md)
- [let HKMetadataKeyHeartRateRecoveryMaxObservedRecoveryHeartRate: String](hkmetadatakeyheartraterecoverymaxobservedrecoveryheartrate.md)
- [let HKMetadataKeyHeartRateRecoveryTestType: String](hkmetadatakeyheartraterecoverytesttype.md)
  The type of test that the source used to calculate a person’s heart-rate recovery.
- [let HKMetadataKeyVO2MaxTestType: String](hkmetadatakeyvo2maxtesttype.md)
  The method used to calculate the user’s VO2 max rate.
### Audio Event Keys
- [let HKMetadataKeyAudioExposureLevel: String](hkmetadatakeyaudioexposurelevel.md)
  The audio level associated with an audio event.
- [let HKMetadataKeyAudioExposureDuration: String](hkmetadatakeyaudioexposureduration.md)
  The audio exposure event’s duration.
- [let HKMetadataKeyHeadphoneGain: String](hkmetadatakeyheadphonegain.md)
### Blood Glucose Keys
- [let HKMetadataKeyBloodGlucoseMealTime: String](hkmetadatakeybloodglucosemealtime.md)
  A key that indicates the relative timing of a blood glucose reading to a meal.
- [let HKMetadataKeyInsulinDeliveryReason: String](hkmetadatakeyinsulindeliveryreason.md)
  The medical reason for administering insulin.
### Reproductive Health Keys
- [let HKMetadataKeyMenstrualCycleStart: String](hkmetadatakeymenstrualcyclestart.md)
  A key that indicates whether the sample represents the start of a menstrual cycle. This metadata key is required for [`menstrualFlow`](hkcategorytypeidentifier/menstrualflow.md) category samples.
- [let HKMetadataKeySexualActivityProtectionUsed: String](hkmetadatakeysexualactivityprotectionused.md)
  A key that indicates whether protection was used during sexual activity. This metadata key can be used with [`sexualActivity`](hkcategorytypeidentifier/sexualactivity.md) category samples.
### Algorithm Keys
- [let HKMetadataKeyAlgorithmVersion: String](hkmetadatakeyalgorithmversion.md)
  A key that indicates the version number of the algorithm used to calculate the sample’s value.
- [let HKMetadataKeyAppleECGAlgorithmVersion: String](hkmetadatakeyappleecgalgorithmversion.md)
  A key for metadata indicating the version number of the algorithm Apple Watch uses to generate an ECG reading.
- [enum HKAppleECGAlgorithmVersion](hkappleecgalgorithmversion.md)
  Version numbers for the algorithm Apple Watch uses to generate an ECG reading.
- [let HKPredicateKeyPathECGClassification: String](hkpredicatekeypathecgclassification.md)
  The key path for the sample’s classification.
- [let HKPredicateKeyPathECGSymptomsStatus: String](hkpredicatekeypathecgsymptomsstatus.md)
  The key path for the sample’s symptom status.

## See Also

- [class HKCumulativeQuantitySample](hkcumulativequantitysample.md)
  A sample that represents a cumulative quantity.
- [class HKDiscreteQuantitySample](hkdiscretequantitysample.md)
  A sample that represents a discrete quantity.
- [class HKQuantitySample](hkquantitysample.md)
  A sample that represents a quantity, including the value and the units.
- [class HKCategorySample](hkcategorysample.md)
  A sample with values from a short list of possible values.
- [class HKCorrelation](hkcorrelation.md)
  A sample that groups multiple related samples into a single entry.
- [Units and quantities](units-and-quantities.md)
  Objects used to specify a quantity for a given unit, and to convert between units.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/metadata-keys)*