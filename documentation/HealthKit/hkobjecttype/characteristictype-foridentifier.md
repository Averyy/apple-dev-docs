# characteristicType(forIdentifier:)

**Framework**: HealthKit  
**Kind**: method

Returns the shared characteristic type for the provided identifier.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func characteristicType(forIdentifier identifier: HKCharacteristicTypeIdentifier) -> HKCharacteristicType?
```

#### Return Value

The shared `HKCharacteristicType` instance based on the provided identifier.

#### Discussion

This method returns an instance of the [`HKCharacteristicType`](hkcharacteristictype.md) concrete subclass. Characteristic types represent data that doesn’t typically change over time. Unlike the other object types, characteristic types cannot be used to create new HealthKit objects. Instead, users must enter and edit their characteristic data using the Health app. Characteristic types are used only when asking for permission to read data from the HealthKit store.

## Parameters

- `identifier`: A characteristic type identifier. For a list of valid identifiers, see  .

## See Also

- [struct HKCharacteristicTypeIdentifier](hkcharacteristictypeidentifier.md)
  The identifiers that create characteristic type objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype/characteristictype(foridentifier:))*