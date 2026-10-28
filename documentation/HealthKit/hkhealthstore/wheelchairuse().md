# wheelchairUse()

**Framework**: HealthKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (HKWheelchairUseObject *) wheelchairUseWithError:(NSError **) error;
```

## Return Value

An object indicating whether the user uses a wheelchair.

## Discussion

If the user has not yet specified their wheelchair use, or if the user has denied your app permission to read the wheelchair use, this method returns [`HKWheelchairUse.notSet`](../hkwheelchairuse/notset.md).

## Topics

### Possible Values
- [class HKWheelchairUseObject](../hkwheelchairuseobject.md)
  This class acts as a wrapper for the wheelchair use enumeration.
- [enum HKWheelchairUse](../hkwheelchairuse.md)
  Constants indicating the user’s wheelchair use.

## See Also

### Reading characteristic data
- [func biologicalSex() throws -> HKBiologicalSexObject](./biologicalsex%28%29.md)
  Reads someone’s biological sex from the HealthKit store.
- [func bloodType() throws -> HKBloodTypeObject](./bloodtype%28%29.md)
  Reads the user’s blood type from the HealthKit store.
- [func dateOfBirth() throws -> Date](./dateofbirth%28%29.md)
  Reads the user’s date of birth from the HealthKit store as a date value.
- [func dateOfBirthComponents() throws -> DateComponents](./dateofbirthcomponents%28%29.md)
  Reads the user’s date of birth from the HealthKit store as date components.
- [func fitzpatrickSkinType() throws -> HKFitzpatrickSkinTypeObject](./fitzpatrickskintype%28%29.md)
  Reads the user’s Fitzpatrick Skin Type from the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkhealthstore/wheelchairuse())*