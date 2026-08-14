# ASImportableFIDO2LargeBlob

**Framework**: Authentication Services  
**Kind**: struct

A representation of FIDO2 LargeBlob extensions as defined in CXF.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+
- visionOS 26.4+

## Declaration

```swift
struct ASImportableFIDO2LargeBlob
```

## Topics

### Initializers
- [init(uncompressedSize: Int, data: Data)](asimportablefido2largeblob/init(uncompressedsize:data:).md)
### Instance Properties
- [var data: Data](asimportablefido2largeblob/data.md)
  The contents of the large blob value which has been DEFLATE compressed.
- [var uncompressedSize: Int](asimportablefido2largeblob/uncompressedsize.md)
  The claimed uncompressed size of stored data.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablefido2largeblob)*