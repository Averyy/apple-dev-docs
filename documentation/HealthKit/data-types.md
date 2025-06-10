# Data types

**Framework**: HealthKit

Specify the kind of data used in HealthKit.

#### Overview

HealthKit uses [`HKObjectType`](hkobjecttype.md) subclasses to identify the different types of data stored in HealthKit, from inherent data that doesn’t typically change over time to complex data types that combine multiple samples or compute values over sets of samples.

To create a type object, call the appropriate [`HKObjectType`](hkobjecttype.md) class method, and pass in the desired type identifier.

```swift
let bloodType = HKObjectType.characteristicType(forIdentifier: .bloodType)

let caloriesConsumed = HKObjectType.quantityType(forIdentifier: .dietaryEnergyConsumed)

let sleepAnalysis = HKObjectType.categoryType(forIdentifier: .sleepAnalysis)
```

You can use the resulting object types to request permission to access the data, save new data to the HealthKit store, or read data from the HealthKit store.

## Topics

### Object type subclasses
- [class HKCharacteristicType](hkcharacteristictype.md)
  A type that represents data that doesn’t typically change over time.
- [class HKQuantityType](hkquantitytype.md)
  A type that identifies samples that store numerical values.
- [class HKCategoryType](hkcategorytype.md)
  A type that identifies samples that contain a value from a small set of possible values.
- [class HKCorrelationType](hkcorrelationtype.md)
  A type that identifies samples that group multiple subsamples.
- [class HKActivitySummaryType](hkactivitysummarytype.md)
  A type that identifies activity summary objects.
- [class HKAudiogramSampleType](hkaudiogramsampletype.md)
  A type that identifies samples that contain audiogram data.
- [class HKElectrocardiogramType](hkelectrocardiogramtype.md)
  A type that identifies samples containing electrocardiogram data.
- [class HKSeriesType](hkseriestype.md)
  A type that indicates the data stored in a series sample.
- [class HKClinicalType](hkclinicaltype.md)
  A type that identifies samples that contain clinical record data.
- [class HKWorkoutType](hkworkouttype.md)
  A type that identifies samples that store information about a workout.
- [class HKObjectType](hkobjecttype.md)
  An abstract superclass with subclasses that identify a specific type of data for the HealthKit store.
- [class HKSampleType](hksampletype.md)
  An abstract superclass for all classes that identify a specific type of sample when working with the HealthKit store.
### Characteristic identifiers
- [static let activityMoveMode: HKCharacteristicTypeIdentifier](hkcharacteristictypeidentifier/activitymovemode.md)
  A characteristic identifier for the user’s activity mode.
- [static let biologicalSex: HKCharacteristicTypeIdentifier](hkcharacteristictypeidentifier/biologicalsex.md)
  A characteristic type identifier for the user’s sex.
- [static let bloodType: HKCharacteristicTypeIdentifier](hkcharacteristictypeidentifier/bloodtype.md)
  A characteristic type identifier for the user’s blood type.
- [static let dateOfBirth: HKCharacteristicTypeIdentifier](hkcharacteristictypeidentifier/dateofbirth.md)
  A characteristic type identifier for the user’s date of birth.
- [static let fitzpatrickSkinType: HKCharacteristicTypeIdentifier](hkcharacteristictypeidentifier/fitzpatrickskintype.md)
  A characteristic type identifier for the user’s skin type.
- [static let wheelchairUse: HKCharacteristicTypeIdentifier](hkcharacteristictypeidentifier/wheelchairuse.md)
  A characteristic identifier for the user’s use of a wheelchair.
### Activity
- [static let stepCount: HKQuantityTypeIdentifier](hkquantitytypeidentifier/stepcount.md)
  A quantity sample type that measures the number of steps the user has taken.
- [static let distanceWalkingRunning: HKQuantityTypeIdentifier](hkquantitytypeidentifier/distancewalkingrunning.md)
  A quantity sample type that measures the distance the user has moved by walking or running.
- [static let runningSpeed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/runningspeed.md)
  A quantity sample type that measures the runner’s speed.
- [static let runningStrideLength: HKQuantityTypeIdentifier](hkquantitytypeidentifier/runningstridelength.md)
  A quantity sample type that measures the distance covered by a single step while running.
- [static let runningPower: HKQuantityTypeIdentifier](hkquantitytypeidentifier/runningpower.md)
  A quantity sample type that measures the rate of work required for the runner to maintain their speed.
- [static let runningGroundContactTime: HKQuantityTypeIdentifier](hkquantitytypeidentifier/runninggroundcontacttime.md)
  A quantity sample type that measures the amount of time the runner’s foot is in contact with the ground while running.
- [static let runningVerticalOscillation: HKQuantityTypeIdentifier](hkquantitytypeidentifier/runningverticaloscillation.md)
  A quantity sample type measuring pelvis vertical range of motion during a single running stride.
- [static let distanceCycling: HKQuantityTypeIdentifier](hkquantitytypeidentifier/distancecycling.md)
  A quantity sample type that measures the distance the user has moved by cycling.
- [static let pushCount: HKQuantityTypeIdentifier](hkquantitytypeidentifier/pushcount.md)
  A quantity sample type that measures the number of pushes that the user has performed while using a wheelchair.
- [static let distanceWheelchair: HKQuantityTypeIdentifier](hkquantitytypeidentifier/distancewheelchair.md)
  A quantity sample type that measures the distance the user has moved using a wheelchair.
- [static let swimmingStrokeCount: HKQuantityTypeIdentifier](hkquantitytypeidentifier/swimmingstrokecount.md)
  A quantity sample type that measures the number of strokes performed while swimming.
- [static let distanceSwimming: HKQuantityTypeIdentifier](hkquantitytypeidentifier/distanceswimming.md)
  A quantity sample type that measures the distance the user has moved while swimming.
- [static let distanceDownhillSnowSports: HKQuantityTypeIdentifier](hkquantitytypeidentifier/distancedownhillsnowsports.md)
  A quantity sample type that measures the distance the user has traveled while skiing or snowboarding.
- [static let basalEnergyBurned: HKQuantityTypeIdentifier](hkquantitytypeidentifier/basalenergyburned.md)
  A quantity sample type that measures the resting energy burned by the user.
- [static let activeEnergyBurned: HKQuantityTypeIdentifier](hkquantitytypeidentifier/activeenergyburned.md)
  A quantity sample type that measures the amount of active energy the user has burned.
- [static let flightsClimbed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/flightsclimbed.md)
  A quantity sample type that measures the number flights of stairs that the user has climbed.
- [static let nikeFuel: HKQuantityTypeIdentifier](hkquantitytypeidentifier/nikefuel.md)
  A quantity sample type that measures the number of NikeFuel points the user has earned.
- [static let appleExerciseTime: HKQuantityTypeIdentifier](hkquantitytypeidentifier/appleexercisetime.md)
  A quantity sample type that measures the amount of time the user spent exercising.
- [static let appleMoveTime: HKQuantityTypeIdentifier](hkquantitytypeidentifier/applemovetime.md)
  A quantity sample type that measures the amount of time the user has spent performing activities that involve full-body movements during the specified day.
- [static let appleStandHour: HKCategoryTypeIdentifier](hkcategorytypeidentifier/applestandhour.md)
  A category sample type that counts the number of hours in the day during which the user has stood and moved for at least one minute per hour.
- [static let appleStandTime: HKQuantityTypeIdentifier](hkquantitytypeidentifier/applestandtime.md)
  A quantity sample type that measures the amount of time the user has spent standing.
- [static let vo2Max: HKQuantityTypeIdentifier](hkquantitytypeidentifier/vo2max.md)
  A quantity sample that measures the maximal oxygen consumption during exercise.
- [static let lowCardioFitnessEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/lowcardiofitnessevent.md)
  An event that indicates the user’s VO2 max values consistently fall below a particular aerobic fitness threshold.
### Attachments
- [class HKAttachment](hkattachment.md)
  A file that is attached to a sample in the HealthKit store.
- [class HKAttachmentStore](hkattachmentstore.md)
  The access point for attachments associated with samples in the HealthKit store.
- [class HKAttachmentDataReader](hkattachmentdatareader.md)
  A reader that provides access to an attachment’s data.
### Body measurements
- [static let height: HKQuantityTypeIdentifier](hkquantitytypeidentifier/height.md)
  A quantity sample type that measures the user’s height.
- [static let bodyMass: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bodymass.md)
  A quantity sample type that measures the user’s weight.
- [static let bodyMassIndex: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bodymassindex.md)
  A quantity sample type that measures the user’s body mass index.
- [static let leanBodyMass: HKQuantityTypeIdentifier](hkquantitytypeidentifier/leanbodymass.md)
  A quantity sample type that measures the user’s lean body mass.
- [static let bodyFatPercentage: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bodyfatpercentage.md)
  A quantity sample type that measures the user’s body fat percentage.
- [static let waistCircumference: HKQuantityTypeIdentifier](hkquantitytypeidentifier/waistcircumference.md)
  A quantity sample type that measures the user’s waist circumference.
### Reproductive health
- [static let menstrualFlow: HKCategoryTypeIdentifier](hkcategorytypeidentifier/menstrualflow.md)
  A category sample type that records menstrual cycles.
- [static let intermenstrualBleeding: HKCategoryTypeIdentifier](hkcategorytypeidentifier/intermenstrualbleeding.md)
  A category sample type that records spotting outside the normal menstruation period.
- [static let infrequentMenstrualCycles: HKCategoryTypeIdentifier](hkcategorytypeidentifier/infrequentmenstrualcycles.md)
  A category sample that indicates an infrequent menstrual cycle.
- [static let irregularMenstrualCycles: HKCategoryTypeIdentifier](hkcategorytypeidentifier/irregularmenstrualcycles.md)
  A category sample that indicates an irregular menstrual cycle.
- [static let persistentIntermenstrualBleeding: HKCategoryTypeIdentifier](hkcategorytypeidentifier/persistentintermenstrualbleeding.md)
  A category sample that indicates persistent intermenstrual bleeding.
- [static let prolongedMenstrualPeriods: HKCategoryTypeIdentifier](hkcategorytypeidentifier/prolongedmenstrualperiods.md)
  A category sample that indicates a prolonged menstrual cycle.
- [static let basalBodyTemperature: HKQuantityTypeIdentifier](hkquantitytypeidentifier/basalbodytemperature.md)
  A quantity sample type that records the user’s basal body temperature.
- [static let cervicalMucusQuality: HKCategoryTypeIdentifier](hkcategorytypeidentifier/cervicalmucusquality.md)
  A category sample type that records the quality of the user’s cervical mucus.
- [static let ovulationTestResult: HKCategoryTypeIdentifier](hkcategorytypeidentifier/ovulationtestresult.md)
  A category sample type that records the result of an ovulation home test.
- [static let progesteroneTestResult: HKCategoryTypeIdentifier](hkcategorytypeidentifier/progesteronetestresult.md)
  A category type that represents the results from a home progesterone test.
- [static let sexualActivity: HKCategoryTypeIdentifier](hkcategorytypeidentifier/sexualactivity.md)
  A category sample type that records sexual activity.
- [static let contraceptive: HKCategoryTypeIdentifier](hkcategorytypeidentifier/contraceptive.md)
  A category sample type that records the use of contraceptives.
- [static let pregnancy: HKCategoryTypeIdentifier](hkcategorytypeidentifier/pregnancy.md)
  A category type that records pregnancy.
- [static let pregnancyTestResult: HKCategoryTypeIdentifier](hkcategorytypeidentifier/pregnancytestresult.md)
  A category type that represents the results from a home pregnancy test.
- [static let lactation: HKCategoryTypeIdentifier](hkcategorytypeidentifier/lactation.md)
  A category type that records lactation.
### Hearing
- [static let environmentalAudioExposure: HKQuantityTypeIdentifier](hkquantitytypeidentifier/environmentalaudioexposure.md)
  A quantity sample type that measures audio exposure to sounds in the environment.
- [static let headphoneAudioExposure: HKQuantityTypeIdentifier](hkquantitytypeidentifier/headphoneaudioexposure.md)
  A quantity sample type that measures audio exposure from headphones.
- [static let environmentalAudioExposureEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/environmentalaudioexposureevent.md)
  A category sample type that records exposure to potentially damaging sounds from the environment.
- [static let headphoneAudioExposureEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/headphoneaudioexposureevent.md)
  A category sample type that records exposure to potentially damaging sounds from headphones.
- [static let audioExposureEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/audioexposureevent.md)
  A category sample type for audio exposure events.
### Vital signs
- [static let heartRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartrate.md)
  A quantity sample type that measures the user’s heart rate.
- [static let lowHeartRateEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/lowheartrateevent.md)
  A category sample type for low heart rate events.
- [static let highHeartRateEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/highheartrateevent.md)
  A category sample type for high heart rate events.
- [static let irregularHeartRhythmEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/irregularheartrhythmevent.md)
  A category sample type for irregular heart rhythm events.
- [static let restingHeartRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/restingheartrate.md)
  A quantity sample type that measures the user’s resting heart rate.
- [static let heartRateVariabilitySDNN: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartratevariabilitysdnn.md)
  A quantity sample type that measures the standard deviation of heartbeat intervals.
- [static let heartRateRecoveryOneMinute: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartraterecoveryoneminute.md)
  A quantity sample that records the reduction in heart rate from the peak exercise rate to the rate one minute after exercising ended.
- [static let atrialFibrillationBurden: HKQuantityTypeIdentifier](hkquantitytypeidentifier/atrialfibrillationburden.md)
  A quantity type that measures an estimate of the percentage of time a person’s heart shows signs of atrial fibrillation (AFib) while wearing Apple Watch.
- [static let walkingHeartRateAverage: HKQuantityTypeIdentifier](hkquantitytypeidentifier/walkingheartrateaverage.md)
  A quantity sample type that measures the user’s heart rate while walking.
- [let HKDataTypeIdentifierHeartbeatSeries: String](hkdatatypeidentifierheartbeatseries.md)
  A series sample containing heartbeat data.
- [class HKElectrocardiogramType](hkelectrocardiogramtype.md)
  A type that identifies samples containing electrocardiogram data.
- [static let oxygenSaturation: HKQuantityTypeIdentifier](hkquantitytypeidentifier/oxygensaturation.md)
  A quantity sample type that measures the user’s oxygen saturation.
- [static let bodyTemperature: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bodytemperature.md)
  A quantity sample type that measures the user’s body temperature.
- [static let bloodPressure: HKCorrelationTypeIdentifier](hkcorrelationtypeidentifier/bloodpressure.md)
  A correlation sample that combines a systolic sample and a diastolic sample into a single blood pressure reading.
- [static let bloodPressureSystolic: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bloodpressuresystolic.md)
  A quantity sample type that measures the user’s systolic blood pressure.
- [static let bloodPressureDiastolic: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bloodpressurediastolic.md)
  A quantity sample type that measures the user’s diastolic blood pressure.
- [static let respiratoryRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/respiratoryrate.md)
  A quantity sample type that measures the user’s respiratory rate.
### Nutrition
- [Nutrition Type Identifiers](nutrition-type-identifiers.md)
  Type identifiers used for tracking diet and nutrition.
### Alcohol consumption
- [static let bloodAlcoholContent: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bloodalcoholcontent.md)
  A quantity sample type that measures the user’s blood alcohol content.
- [static let numberOfAlcoholicBeverages: HKQuantityTypeIdentifier](hkquantitytypeidentifier/numberofalcoholicbeverages.md)
  A quantity sample type that measures the number of standard alcoholic drinks that the user has consumed.
### Mobility
- [static let appleWalkingSteadiness: HKQuantityTypeIdentifier](hkquantitytypeidentifier/applewalkingsteadiness.md)
  A quantity sample type that measures the steadiness of the user’s gait.
- [static let appleWalkingSteadinessEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/applewalkingsteadinessevent.md)
  A category sample type that records an incident where the user showed a reduced score for their gait’s steadiness.
- [static let sixMinuteWalkTestDistance: HKQuantityTypeIdentifier](hkquantitytypeidentifier/sixminutewalktestdistance.md)
  A quantity sample type that stores the distance a user can walk during a six-minute walk test.
- [static let walkingSpeed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/walkingspeed.md)
  A quantity sample type that measures the user’s average speed when walking steadily over flat ground.
- [static let walkingStepLength: HKQuantityTypeIdentifier](hkquantitytypeidentifier/walkingsteplength.md)
  A quantity sample type that measures the average length of the user’s step when walking steadily over flat ground.
- [static let walkingAsymmetryPercentage: HKQuantityTypeIdentifier](hkquantitytypeidentifier/walkingasymmetrypercentage.md)
  A quantity sample type that measures the percentage of steps in which one foot moves at a different speed than the other when walking on flat ground.
- [static let walkingDoubleSupportPercentage: HKQuantityTypeIdentifier](hkquantitytypeidentifier/walkingdoublesupportpercentage.md)
  A quantity sample type that measures the percentage of time when both of the user’s feet touch the ground while walking steadily over flat ground.
- [static let stairAscentSpeed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/stairascentspeed.md)
  A quantity sample type measuring the user’s speed while climbing a flight of stairs.
- [static let stairDescentSpeed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/stairdescentspeed.md)
  A quantity sample type measuring the user’s speed while descending a flight of stairs.
### Symptoms
- [Symptom Type Identifiers](symptom-type-identifiers.md)
  Identifiers for medical symptoms.
### Lab and test results
- [static let bloodAlcoholContent: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bloodalcoholcontent.md)
  A quantity sample type that measures the user’s blood alcohol content.
- [static let bloodGlucose: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bloodglucose.md)
  A quantity sample type that measures the user’s blood glucose level.
- [static let electrodermalActivity: HKQuantityTypeIdentifier](hkquantitytypeidentifier/electrodermalactivity.md)
  A quantity sample type that measures electrodermal activity.
- [static let forcedExpiratoryVolume1: HKQuantityTypeIdentifier](hkquantitytypeidentifier/forcedexpiratoryvolume1.md)
  A quantity sample type that measures the amount of air that can be forcibly exhaled from the lungs during the first second of a forced exhalation.
- [static let forcedVitalCapacity: HKQuantityTypeIdentifier](hkquantitytypeidentifier/forcedvitalcapacity.md)
  A quantity sample type that measures the amount of air that can be forcibly exhaled from the lungs after taking the deepest breath possible.
- [static let inhalerUsage: HKQuantityTypeIdentifier](hkquantitytypeidentifier/inhalerusage.md)
  A quantity sample type that measures the number of puffs the user takes from their inhaler.
- [static let insulinDelivery: HKQuantityTypeIdentifier](hkquantitytypeidentifier/insulindelivery.md)
  A quantity sample that measures the amount of insulin delivered.
- [static let numberOfTimesFallen: HKQuantityTypeIdentifier](hkquantitytypeidentifier/numberoftimesfallen.md)
  A quantity sample type that measures the number of times the user fell.
- [static let peakExpiratoryFlowRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/peakexpiratoryflowrate.md)
  A quantity sample type that measures the user’s maximum flow rate generated during a forceful exhalation.
- [static let peripheralPerfusionIndex: HKQuantityTypeIdentifier](hkquantitytypeidentifier/peripheralperfusionindex.md)
  A quantity sample type that measures the user’s peripheral perfusion index.
### Mindfulness and sleep
- [static let mindfulSession: HKCategoryTypeIdentifier](hkcategorytypeidentifier/mindfulsession.md)
  A category sample type for recording a mindful session.
- [static let sleepAnalysis: HKCategoryTypeIdentifier](hkcategorytypeidentifier/sleepanalysis.md)
  A category sample type for sleep analysis information.
- [HKCategoryValueSleepAnalysisAsleepValues](hkcategoryvaluesleepanalysisasleepvalues.md)
- [static let appleSleepingWristTemperature: HKQuantityTypeIdentifier](hkquantitytypeidentifier/applesleepingwristtemperature.md)
  A quantity sample type that records the wrist temperature during sleep.
- [HKAppleSleepingBreathingDisturbancesClassificationForQuantity](hkapplesleepingbreathingdisturbancesclassificationforquantity.md)
- [enum HKAppleSleepingBreathingDisturbancesClassification](hkapplesleepingbreathingdisturbancesclassification.md)
### Self care
- [static let toothbrushingEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/toothbrushingevent.md)
  A category sample type for toothbrushing events.
- [static let handwashingEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/handwashingevent.md)
  A category sample type for handwashing events.
### Workouts
- [let HKWorkoutTypeIdentifier: String](hkworkouttypeidentifier.md)
  The workout type identifier.
- [let HKWorkoutRouteTypeIdentifier: String](hkworkoutroutetypeidentifier.md)
  A series sample containing location data that defines the route the user took during a workout.
### Clinical records
- [struct HKClinicalTypeIdentifier](hkclinicaltypeidentifier.md)
  A type identifier for the different categories of clinical records.
### UV exposure
- [static let uvExposure: HKQuantityTypeIdentifier](hkquantitytypeidentifier/uvexposure.md)
  A quantity sample type that measures the user’s exposure to UV radiation.
### Vision
- [let HKVisionPrescriptionTypeIdentifier: String](hkvisionprescriptiontypeidentifier.md)
  A type identifier for vision prescription samples.
### Diving
- [static let underwaterDepth: HKQuantityTypeIdentifier](hkquantitytypeidentifier/underwaterdepth.md)
  A quantity sample that records a person’s depth underwater.
- [static let waterTemperature: HKQuantityTypeIdentifier](hkquantitytypeidentifier/watertemperature.md)
  A quantity sample that records the water temperature.
### Utilities
- [struct BufferedAsyncByteIterator](bufferedasyncbyteiterator.md)
  An asynchronous iterator for byte data.

## See Also

- [Saving data to HealthKit](saving-data-to-healthkit.md)
  Create and share HealthKit samples.
- [Reading data from HealthKit](reading-data-from-healthkit.md)
  Use queries to request sample data from HealthKit.
- [class HKHealthStore](hkhealthstore.md)
  The access point for all data managed by HealthKit.
- [Creating a Mobility Health App](creating-a-mobility-health-app.md)
  Create a health app that allows a clinical care team to send and receive mobility data.
- [Samples](samples.md)
  Create and save health and fitness samples.
- [Queries](queries.md)
  Query health and fitness data.
- [Visualizing HealthKit State of Mind in visionOS](visualizing-healthkit-state-of-mind-in-visionos.md)
  Incorporate HealthKit State of Mind into your app and visualize the data in visionOS.
- [Logging symptoms associated with a medication](logging-symptoms-associated-with-a-medication.md)
  Fetch medications and dose events from the HealthKit store, and create symptom samples to associate with them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/data-types)*