# MobileDocumentDisplayRequest.Options

**Framework**: ProximityReader  
**Kind**: struct

An object that customizes how to perform a display request.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Options
```

#### Overview

Use this object to configure the validation mode of the request.

## Topics

### Structures
- [MobileDocumentDisplayRequest.Options.DocumentType](mobiledocumentdisplayrequest/options-swift.struct/documenttype.md)
  A type that represents a type of supported mobile document.
- [MobileDocumentDisplayRequest.Options.ValidationMode](mobiledocumentdisplayrequest/options-swift.struct/validationmode-swift.struct.md)
  A type that represents the validation mode of the mobile document request.
### Operators
- [static func == (MobileDocumentDisplayRequest.Options, MobileDocumentDisplayRequest.Options) -> Bool](mobiledocumentdisplayrequest/options-swift.struct/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(allowedDocumentTypes: [MobileDocumentDisplayRequest.Options.DocumentType], validationMode: MobileDocumentDisplayRequest.Options.ValidationMode)](mobiledocumentdisplayrequest/options-swift.struct/init(alloweddocumenttypes:validationmode:).md)
  Creates a mobile document reader display request options type.
### Instance Properties
- [var allowedDocumentTypes: [MobileDocumentDisplayRequest.Options.DocumentType]](mobiledocumentdisplayrequest/options-swift.struct/alloweddocumenttypes.md)
  The allowed document types of the mobile document request.
- [var hashValue: Int](mobiledocumentdisplayrequest/options-swift.struct/hashvalue.md)
  The hash value.
- [var validationMode: MobileDocumentDisplayRequest.Options.ValidationMode](mobiledocumentdisplayrequest/options-swift.struct/validationmode-swift.property.md)
  The validation mode of the mobile document request.
### Instance Methods
- [func hash(into: inout Hasher)](mobiledocumentdisplayrequest/options-swift.struct/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](mobiledocumentdisplayrequest/options-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var options: MobileDocumentDisplayRequest.Options](mobiledocumentdisplayrequest/options-swift.property.md)
  An object that customizes how to perform a display request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentdisplayrequest/options-swift.struct)*