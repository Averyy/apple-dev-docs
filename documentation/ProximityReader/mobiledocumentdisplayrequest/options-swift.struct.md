# MobileDocumentDisplayRequest.Options

**Framework**: ProximityReader  
**Kind**: struct  
**Role**: Structure

An object that customizes how to perform a display request.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
struct Options
```

#### Overview

Use this object to configure the validation mode of the request.

## Topics

### Structures
- [MobileDocumentDisplayRequest.Options.DocumentType](./options-swift.struct/documenttype.md)
  A type that represents a type of supported mobile document.
- [MobileDocumentDisplayRequest.Options.ValidationMode](./options-swift.struct/validationmode-swift.struct.md)
  A type that represents the validation mode of the mobile document request.
### Initializers
- [init(allowedDocumentTypes: [MobileDocumentDisplayRequest.Options.DocumentType], validationMode: MobileDocumentDisplayRequest.Options.ValidationMode)](./options-swift.struct/init%28alloweddocumenttypes,validationmode%29.md)
  Creates a mobile document reader display request options type.
### Instance Properties
- [var allowedDocumentTypes: [MobileDocumentDisplayRequest.Options.DocumentType]](./options-swift.struct/alloweddocumenttypes.md)
  The allowed document types of the mobile document request.
- [var validationMode: MobileDocumentDisplayRequest.Options.ValidationMode](./options-swift.struct/validationmode-swift.property.md)
  The validation mode of the mobile document request.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring a display request
- [var options: MobileDocumentDisplayRequest.Options](./options-swift.property.md)
  An object that customizes how to perform a display request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/proximityreader/mobiledocumentdisplayrequest/options-swift.struct)*