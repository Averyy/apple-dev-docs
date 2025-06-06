# dateOfBirthComponents()

**Framework**: HealthKit  
**Kind**: method

Reads the user’s date of birth from the HealthKit store as date components.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func dateOfBirthComponents() throws -> DateComponents
```

#### Return Value

An [`NSDateComponents`](https://developer.apple.com/documentation/Foundation/NSDateComponents) object representing the user’s birthdate in the Gregorian calendar, or `nil`.

#### Discussion

If the user has not yet specified a birth date, or if the user has denied your app permission to read the birth date, this method returns `nil`.

## See Also

- [func biologicalSex() throws -> HKBiologicalSexObject](hkhealthstore/biologicalsex.md)
  Reads someone’s biological sex from the HealthKit store.
- [func bloodType() throws -> HKBloodTypeObject](hkhealthstore/bloodtype.md)
  Reads the user’s blood type from the HealthKit store.
- [func dateOfBirth() throws -> Date](hkhealthstore/dateofbirth.md)
  Reads the user’s date of birth from the HealthKit store as a date value.
- [func fitzpatrickSkinType() throws -> HKFitzpatrickSkinTypeObject](hkhealthstore/fitzpatrickskintype.md)
  Reads the user’s Fitzpatrick Skin Type from the HealthKit store.
- [func wheelchairUse() throws -> HKWheelchairUseObject](hkhealthstore/wheelchairuse.md)
  Reads the user’s wheelchair use from the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/dateofbirthcomponents())*