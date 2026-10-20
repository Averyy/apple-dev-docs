# dateOfBirthComponents()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSDateComponents *) dateOfBirthComponentsWithError:(NSError **) error;
```

#### Return Value

An [`NSDateComponents`](../../Foundation/nsdatecomponents.md) object representing the user’s birthdate in the Gregorian calendar, or `nil`.

#### Discussion

If the user has not yet specified a birth date, or if the user has denied your app permission to read the birth date, this method returns `nil`.

## See Also

### Reading characteristic data
- [func biologicalSex() throws -> HKBiologicalSexObject](./biologicalsex%28%29.md)
  Reads someone’s biological sex from the HealthKit store.
- [func bloodType() throws -> HKBloodTypeObject](./bloodtype%28%29.md)
  Reads the user’s blood type from the HealthKit store.
- [func dateOfBirth() throws -> Date](./dateofbirth%28%29.md)
  Reads the user’s date of birth from the HealthKit store as a date value.
- [func fitzpatrickSkinType() throws -> HKFitzpatrickSkinTypeObject](./fitzpatrickskintype%28%29.md)
  Reads the user’s Fitzpatrick Skin Type from the HealthKit store.
- [func wheelchairUse() throws -> HKWheelchairUseObject](./wheelchairuse%28%29.md)
  Reads the user’s wheelchair use from the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/dateofbirthcomponents())*