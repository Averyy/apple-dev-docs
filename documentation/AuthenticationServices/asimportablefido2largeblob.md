# ASImportableFIDO2LargeBlob

**Framework**: Authentication Services  
**Kind**: struct

A representation of FIDO2 LargeBlob extensions as defined in CXF.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)
- visionOS 26.4+ (Beta)

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
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablefido2largeblob)*