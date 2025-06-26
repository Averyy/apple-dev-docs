# cyclingCadence

**Framework**: HealthKit  
**Kind**: property

A quantity sample type that represents the rate at which the user is pedaling.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
static let cyclingCadence: HKQuantityTypeIdentifier
```

#### Discussion

Cycling cadence represents the number of times the pedals turn over in the minute. The value is measured in revolutions per minute, or RPMs. These samples use counts per minute units (described in [`HKUnit`](hkunit.md)) and measure discrete values (described in [`HKQuantityAggregationStyle`](hkquantityaggregationstyle.md)). Cycling cadence can be automatically collected by peripherals connected to an Apple Watch during cycling workouts.

## See Also

- [static let bleedingAfterPregnancy: HKCategoryTypeIdentifier](hkcategorytypeidentifier/bleedingafterpregnancy.md)
  A category type that records bleeding after pregnancy as a symptom.
- [static let bleedingDuringPregnancy: HKCategoryTypeIdentifier](hkcategorytypeidentifier/bleedingduringpregnancy.md)
  A category type that records bleeding during pregnancy as a symptom.
- [static let sleepApneaEvent: HKCategoryTypeIdentifier](hkcategorytypeidentifier/sleepapneaevent.md)
- [let HKDevicePropertyKeyFirmwareVersion: String](hkdevicepropertykeyfirmwareversion.md)
  The device’s firmware version.
- [let HKDevicePropertyKeyHardwareVersion: String](hkdevicepropertykeyhardwareversion.md)
  The device’s hardware version.
- [let HKDevicePropertyKeyLocalIdentifier: String](hkdevicepropertykeylocalidentifier.md)
  A unique identifier for the device on the hardware running the app. For more information, see [`localIdentifier`](hkdevice/localidentifier.md).
- [let HKDevicePropertyKeyManufacturer: String](hkdevicepropertykeymanufacturer.md)
  The device’s manufacturer.
- [let HKDevicePropertyKeyModel: String](hkdevicepropertykeymodel.md)
  The device’s model.
- [let HKDevicePropertyKeyName: String](hkdevicepropertykeyname.md)
  The device’s name.
- [let HKDevicePropertyKeySoftwareVersion: String](hkdevicepropertykeysoftwareversion.md)
  The device’s software version.
- [let HKDevicePropertyKeyUDIDeviceIdentifier: String](hkdevicepropertykeyudideviceidentifier.md)
  The device’s UDI Device Identifier.
- [let HKPredicateKeyPathCount: String](hkpredicatekeypathcount.md)
  A key path for the sample’s count.
- [static let appleSleepingBreathingDisturbances: HKQuantityTypeIdentifier](hkquantitytypeidentifier/applesleepingbreathingdisturbances.md)
- [static let crossCountrySkiingSpeed: HKQuantityTypeIdentifier](hkquantitytypeidentifier/crosscountryskiingspeed.md)
- [static let cyclingFunctionalThresholdPower: HKQuantityTypeIdentifier](hkquantitytypeidentifier/cyclingfunctionalthresholdpower.md)
  A quantity sample type that measures the estimated maximum average power sustained while riding a bike for 60 minutes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/cyclingcadence)*