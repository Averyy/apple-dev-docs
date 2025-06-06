# identifier

**Framework**: HealthKit  
**Kind**: property

A unique string identifying the HealthKit object type.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var identifier: String { get }
```

#### Discussion

Each object type has a unique identifier. The identifiers can be grouped into different categories: [`HKQuantityTypeIdentifier`](hkquantitytypeidentifier.md), [`HKCategoryTypeIdentifier`](hkcategorytypeidentifier.md), [`HKCharacteristicTypeIdentifier`](hkcharacteristictypeidentifier.md), [`HKCorrelationTypeIdentifier`](hkcorrelationtypeidentifier.md), and [`HKDocumentTypeIdentifier`](hkdocumenttypeidentifier.md) Each group of identifiers is associated with a different concrete subclass of `HKObjectType`.

## See Also

- [func requiresPerObjectAuthorization() -> Bool](hkobjecttype/requiresperobjectauthorization.md)
  Returns a Boolean that indicates whether the data type requires per-object authorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkobjecttype/identifier)*