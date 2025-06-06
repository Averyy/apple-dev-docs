# HKCharacteristicTypeIdentifier

**Framework**: HealthKit  
**Kind**: struct

The identifiers that create characteristic type objects.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct HKCharacteristicTypeIdentifier
```

#### Overview

To create an [`HKCharacteristicType`](hkcharacteristictype.md) instance, pass an [`HKCharacteristicTypeIdentifier`](hkcharacteristictypeidentifier.md) value to the [`characteristicType(forIdentifier:)`](hkobjecttype/characteristictype(foridentifier:).md) method.

## Topics

### Characteristic Types
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
### Initializers
- [init(rawValue: String)](hkcharacteristictypeidentifier/init(rawvalue:).md)
  Returns a newly initialized characteristic type identifier using the provided string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func characteristicType(forIdentifier: HKCharacteristicTypeIdentifier) -> HKCharacteristicType?](hkobjecttype/characteristictype(foridentifier:).md)
  Returns the shared characteristic type for the provided identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcharacteristictypeidentifier)*