# bloodType

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

A characteristic type identifier for the user’s blood type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let bloodType: HKCharacteristicTypeIdentifier
```

```c
extern HKCharacteristicTypeIdentifier const HKCharacteristicTypeIdentifierBloodType;
```

## Discussion

This type uses values from the [`HKBloodType`](../hkbloodtype.md) enum.

## See Also

### Related Documentation
- [class HKCharacteristicType](../hkcharacteristictype.md)
  A type that represents data that doesn’t typically change over time.
- [struct HKCharacteristicTypeIdentifier](../hkcharacteristictypeidentifier.md)
  The identifiers that create characteristic type objects.
- [enum HKBloodType](../hkbloodtype.md)
  Constants indicating the user’s blood type.
- [class HKBloodTypeObject](../hkbloodtypeobject.md)
  This class acts as a wrapper for the [`HKBloodType`](../hkbloodtype.md) enumeration.
### Characteristic identifiers
- [static let activityMoveMode: HKCharacteristicTypeIdentifier](./activitymovemode.md)
  A characteristic identifier for the user’s activity mode.
- [static let biologicalSex: HKCharacteristicTypeIdentifier](./biologicalsex.md)
  A characteristic type identifier for the user’s sex.
- [static let dateOfBirth: HKCharacteristicTypeIdentifier](./dateofbirth.md)
  A characteristic type identifier for the user’s date of birth.
- [static let fitzpatrickSkinType: HKCharacteristicTypeIdentifier](./fitzpatrickskintype.md)
  A characteristic type identifier for the user’s skin type.
- [static let wheelchairUse: HKCharacteristicTypeIdentifier](./wheelchairuse.md)
  A characteristic identifier for the user’s use of a wheelchair.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcharacteristictypeidentifier/bloodtype)*