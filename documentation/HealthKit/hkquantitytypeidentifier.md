# HKQuantityTypeIdentifier

**Framework**: HealthKit  
**Kind**: struct

The identifiers that create quantity type objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct HKQuantityTypeIdentifier
```

#### Overview

To create an [`HKQuantityType`](hkquantitytype.md) instance, pass an [`HKQuantityTypeIdentifier`](hkquantitytypeidentifier.md) value to the [`quantityType(forIdentifier:)`](hkobjecttype/quantitytype(foridentifier:).md) method.

## Topics

### Activity
- [static let stepCount: HKQuantityTypeIdentifier](hkquantitytypeidentifier/stepcount.md)
  A quantity sample type that measures the number of steps the user has taken.
- [static let distanceWalkingRunning: HKQuantityTypeIdentifier](hkquantitytypeidentifier/distancewalkingrunning.md)
  A quantity sample type that measures the distance the user has moved by walking or running.
- [static let runningGroundContactTime: HKQuantityTypeIdentifier](hkquantitytypeidentifier/runninggroundcontacttime.md)
  A quantity sample type that measures the amount of time the runner’s foot is in contact with the ground while running.
- [static let runningPower: HKQuantityTypeIdentifier](hkquantitytypeidentifier/runningpower.md)
  A quantity sample type that measures the rate of work required for the runner to maintain their speed.
- [static let runningSpeed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/runningspeed.md)
  A quantity sample type that measures the runner’s speed.
- [static let runningStrideLength: HKQuantityTypeIdentifier](hkquantitytypeidentifier/runningstridelength.md)
  A quantity sample type that measures the distance covered by a single step while running.
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
- [static let appleStandTime: HKQuantityTypeIdentifier](hkquantitytypeidentifier/applestandtime.md)
  A quantity sample type that measures the amount of time the user has spent standing.
- [static let vo2Max: HKQuantityTypeIdentifier](hkquantitytypeidentifier/vo2max.md)
  A quantity sample that measures the maximal oxygen consumption during exercise.
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
- [static let appleSleepingWristTemperature: HKQuantityTypeIdentifier](hkquantitytypeidentifier/applesleepingwristtemperature.md)
  A quantity sample type that records the wrist temperature during sleep.
### Reproductive health
- [static let basalBodyTemperature: HKQuantityTypeIdentifier](hkquantitytypeidentifier/basalbodytemperature.md)
  A quantity sample type that records the user’s basal body temperature.
### Hearing
- [static let environmentalAudioExposure: HKQuantityTypeIdentifier](hkquantitytypeidentifier/environmentalaudioexposure.md)
  A quantity sample type that measures audio exposure to sounds in the environment.
- [static let headphoneAudioExposure: HKQuantityTypeIdentifier](hkquantitytypeidentifier/headphoneaudioexposure.md)
  A quantity sample type that measures audio exposure from headphones.
### Vital signs
- [static let heartRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartrate.md)
  A quantity sample type that measures the user’s heart rate.
- [static let restingHeartRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/restingheartrate.md)
  A quantity sample type that measures the user’s resting heart rate.
- [static let walkingHeartRateAverage: HKQuantityTypeIdentifier](hkquantitytypeidentifier/walkingheartrateaverage.md)
  A quantity sample type that measures the user’s heart rate while walking.
- [static let heartRateVariabilitySDNN: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartratevariabilitysdnn.md)
  A quantity sample type that measures the standard deviation of heartbeat intervals.
- [static let heartRateRecoveryOneMinute: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartraterecoveryoneminute.md)
  A quantity sample that records the reduction in heart rate from the peak exercise rate to the rate one minute after exercising ended.
- [static let atrialFibrillationBurden: HKQuantityTypeIdentifier](hkquantitytypeidentifier/atrialfibrillationburden.md)
  A quantity type that measures an estimate of the percentage of time a person’s heart shows signs of atrial fibrillation (AFib) while wearing Apple Watch.
- [static let oxygenSaturation: HKQuantityTypeIdentifier](hkquantitytypeidentifier/oxygensaturation.md)
  A quantity sample type that measures the user’s oxygen saturation.
- [static let bodyTemperature: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bodytemperature.md)
  A quantity sample type that measures the user’s body temperature.
- [static let bloodPressureDiastolic: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bloodpressurediastolic.md)
  A quantity sample type that measures the user’s diastolic blood pressure.
- [static let bloodPressureSystolic: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bloodpressuresystolic.md)
  A quantity sample type that measures the user’s systolic blood pressure.
- [static let respiratoryRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/respiratoryrate.md)
  A quantity sample type that measures the user’s respiratory rate.
### Lab and test results
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
### Mindfulness and Sleep
- [static let appleSleepingWristTemperature: HKQuantityTypeIdentifier](hkquantitytypeidentifier/applesleepingwristtemperature.md)
  A quantity sample type that records the wrist temperature during sleep.
### Nutrition
- [static let dietaryBiotin: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarybiotin.md)
  A quantity sample type that measures the amount of biotin (vitamin B7) consumed.
- [static let dietaryCaffeine: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarycaffeine.md)
  A quantity sample type that measures the amount of caffeine consumed.
- [static let dietaryCalcium: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarycalcium.md)
  A quantity sample type that measures the amount of calcium consumed.
- [static let dietaryCarbohydrates: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarycarbohydrates.md)
  A quantity sample type that measures the amount of carbohydrates consumed.
- [static let dietaryChloride: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarychloride.md)
  A quantity sample type that measures the amount of chloride consumed.
- [static let dietaryCholesterol: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarycholesterol.md)
  A quantity sample type that measures the amount of cholesterol consumed.
- [static let dietaryChromium: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarychromium.md)
  A quantity sample type that measures the amount of chromium consumed.
- [static let dietaryCopper: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarycopper.md)
  A quantity sample type that measures the amount of copper consumed.
- [static let dietaryEnergyConsumed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryenergyconsumed.md)
  A quantity sample type that measures the amount of energy consumed.
- [static let dietaryFatMonounsaturated: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryfatmonounsaturated.md)
  A quantity sample type that measures the amount of monounsaturated fat consumed.
- [static let dietaryFatPolyunsaturated: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryfatpolyunsaturated.md)
  A quantity sample type that measures the amount of polyunsaturated fat consumed.
- [static let dietaryFatSaturated: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryfatsaturated.md)
  A quantity sample type that measures the amount of saturated fat consumed.
- [static let dietaryFatTotal: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryfattotal.md)
  A quantity sample type that measures the total amount of fat consumed.
- [static let dietaryFiber: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryfiber.md)
  A quantity sample type that measures the amount of fiber consumed.
- [static let dietaryFolate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryfolate.md)
  A quantity sample type that measures the amount of folate (folic acid) consumed.
- [static let dietaryIodine: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryiodine.md)
  A quantity sample type that measures the amount of iodine consumed.
- [static let dietaryIron: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryiron.md)
  A quantity sample type that measures the amount of iron consumed.
- [static let dietaryMagnesium: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarymagnesium.md)
  A quantity sample type that measures the amount of magnesium consumed.
- [static let dietaryManganese: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarymanganese.md)
  A quantity sample type that measures the amount of manganese consumed.
- [static let dietaryMolybdenum: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarymolybdenum.md)
  A quantity sample type that measures the amount of molybdenum consumed.
- [static let dietaryNiacin: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryniacin.md)
  A quantity sample type that measures the amount of niacin (vitamin B3) consumed.
- [static let dietaryPantothenicAcid: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarypantothenicacid.md)
  A quantity sample type that measures the amount of pantothenic acid (vitamin B5) consumed.
- [static let dietaryPhosphorus: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryphosphorus.md)
  A quantity sample type that measures the amount of phosphorus consumed.
- [static let dietaryPotassium: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarypotassium.md)
  A quantity sample type that measures the amount of potassium consumed.
- [static let dietaryProtein: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryprotein.md)
  A quantity sample type that measures the amount of protein consumed.
- [static let dietaryRiboflavin: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryriboflavin.md)
  A quantity sample type that measures the amount of riboflavin (vitamin B2) consumed.
- [static let dietarySelenium: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryselenium.md)
  A quantity sample type that measures the amount of selenium consumed.
- [static let dietarySodium: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarysodium.md)
  A quantity sample type that measures the amount of sodium consumed.
- [static let dietarySugar: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarysugar.md)
  A quantity sample type that measures the amount of sugar consumed.
- [static let dietaryThiamin: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarythiamin.md)
  A quantity sample type that measures the amount of thiamin (vitamin B1) consumed.
- [static let dietaryVitaminA: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryvitamina.md)
  A quantity sample type that measures the amount of vitamin A consumed.
- [static let dietaryVitaminB12: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryvitaminb12.md)
  A quantity sample type that measures the amount of cyanocobalamin (vitamin B12) consumed.
- [static let dietaryVitaminB6: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryvitaminb6.md)
  A quantity sample type that measures the amount of pyridoxine (vitamin B6) consumed.
- [static let dietaryVitaminC: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryvitaminc.md)
  A quantity sample type that measures the amount of vitamin C consumed.
- [static let dietaryVitaminD: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryvitamind.md)
  A quantity sample type that measures the amount of vitamin D consumed.
- [static let dietaryVitaminE: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryvitamine.md)
  A quantity sample type that measures the amount of vitamin E consumed.
- [static let dietaryVitaminK: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryvitamink.md)
  A quantity sample type that measures the amount of vitamin K consumed.
- [static let dietaryWater: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietarywater.md)
  A quantity sample type that measures the amount of water consumed.
- [static let dietaryZinc: HKQuantityTypeIdentifier](hkquantitytypeidentifier/dietaryzinc.md)
  A quantity sample type that measures the amount of zinc consumed.
### Alcohol consumption
- [static let bloodAlcoholContent: HKQuantityTypeIdentifier](hkquantitytypeidentifier/bloodalcoholcontent.md)
  A quantity sample type that measures the user’s blood alcohol content.
- [static let numberOfAlcoholicBeverages: HKQuantityTypeIdentifier](hkquantitytypeidentifier/numberofalcoholicbeverages.md)
  A quantity sample type that measures the number of standard alcoholic drinks that the user has consumed.
### Mobility
- [static let appleWalkingSteadiness: HKQuantityTypeIdentifier](hkquantitytypeidentifier/applewalkingsteadiness.md)
  A quantity sample type that measures the steadiness of the user’s gait.
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
### UV exposure
- [static let uvExposure: HKQuantityTypeIdentifier](hkquantitytypeidentifier/uvexposure.md)
  A quantity sample type that measures the user’s exposure to UV radiation.
### Diving
- [static let underwaterDepth: HKQuantityTypeIdentifier](hkquantitytypeidentifier/underwaterdepth.md)
  A quantity sample that records a person’s depth underwater.
- [static let waterTemperature: HKQuantityTypeIdentifier](hkquantitytypeidentifier/watertemperature.md)
  A quantity sample that records the water temperature.
### Initializers
- [init(rawValue: String)](hkquantitytypeidentifier/init(rawvalue:).md)
  Returns a newly initialized quantity type identifier using the provided string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func quantityType(forIdentifier: HKQuantityTypeIdentifier) -> HKQuantityType?](hkobjecttype/quantitytype(foridentifier:).md)
  Returns the shared quantity type for the provided identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier)*