# MobileDocumentDisplayRequest.Options.DocumentType

**Framework**: ProximityReader  
**Kind**: struct

A type that represents a type of supported mobile document.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct DocumentType
```

## Topics

### Operators
- [static func == (MobileDocumentDisplayRequest.Options.DocumentType, MobileDocumentDisplayRequest.Options.DocumentType) -> Bool](mobiledocumentdisplayrequest/options-swift.struct/documenttype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](mobiledocumentdisplayrequest/options-swift.struct/documenttype/hashvalue.md)
  The hash value.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledocumentdisplayrequest/options-swift.struct/documenttype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Type Properties
- [static let driversLicense: MobileDocumentDisplayRequest.Options.DocumentType](mobiledocumentdisplayrequest/options-swift.struct/documenttype/driverslicense.md)
  A document of type driver’s license.
- [static let photoID: MobileDocumentDisplayRequest.Options.DocumentType](mobiledocumentdisplayrequest/options-swift.struct/documenttype/photoid.md)
  A document of type photo ID.
### Type Methods
- [static func nationalIDCard(region: Locale.Region) -> MobileDocumentDisplayRequest.Options.DocumentType](mobiledocumentdisplayrequest/options-swift.struct/documenttype/nationalidcard(region:).md)
  A document of type national ID card for a given region.
### Default Implementations
- [Equatable Implementations](mobiledocumentdisplayrequest/options-swift.struct/documenttype/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentdisplayrequest/options-swift.struct/documenttype)*