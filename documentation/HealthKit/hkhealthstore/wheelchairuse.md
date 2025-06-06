# wheelchairUse()

**Framework**: HealthKit  
**Kind**: method

Reads the user’s wheelchair use from the HealthKit store.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func wheelchairUse() throws -> HKWheelchairUseObject
```

#### Return Value

An object indicating whether the user uses a wheelchair.

#### Discussion

If the user has not yet specified their wheelchair use, or if the user has denied your app permission to read the wheelchair use, this method returns [`HKWheelchairUse.notSet`](hkwheelchairuse/notset.md).

## Topics

### Possible Values
- [class HKWheelchairUseObject](hkwheelchairuseobject.md)
  This class acts as a wrapper for the wheelchair use enumeration.
- [enum HKWheelchairUse](hkwheelchairuse.md)
  Constants indicating the user’s wheelchair use.

## See Also

- [func biologicalSex() throws -> HKBiologicalSexObject](hkhealthstore/biologicalsex.md)
  Reads someone’s biological sex from the HealthKit store.
- [func bloodType() throws -> HKBloodTypeObject](hkhealthstore/bloodtype.md)
  Reads the user’s blood type from the HealthKit store.
- [func dateOfBirth() throws -> Date](hkhealthstore/dateofbirth.md)
  Reads the user’s date of birth from the HealthKit store as a date value.
- [func dateOfBirthComponents() throws -> DateComponents](hkhealthstore/dateofbirthcomponents.md)
  Reads the user’s date of birth from the HealthKit store as date components.
- [func fitzpatrickSkinType() throws -> HKFitzpatrickSkinTypeObject](hkhealthstore/fitzpatrickskintype.md)
  Reads the user’s Fitzpatrick Skin Type from the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/wheelchairuse())*