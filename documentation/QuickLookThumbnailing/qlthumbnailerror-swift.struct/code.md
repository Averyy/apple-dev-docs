# QLThumbnailError.Code

**Framework**: Quick Look Thumbnailing  
**Kind**: enum  
**Role**: Enumeration

Error codes that may be returned when generating a thumbnail.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum QLThumbnailError : NSInteger;
```

## Topics

### Error Codes
- [QLThumbnailError.Code.generationFailed](./code/generationfailed.md)
  The thumbnail couldn’t be created for the given file.
- [QLThumbnailError.Code.noCachedThumbnail](./code/nocachedthumbnail.md)
  A low-quality thumbnail couldn’t be created.
- [QLThumbnailError.Code.noCloudThumbnail](./code/nocloudthumbnail.md)
  The thumbnail for a remote file couldn’t be created.
- [QLThumbnailError.Code.requestCancelled](./code/requestcancelled.md)
  The request to create a thumbnail was canceled.
- [QLThumbnailError.Code.requestInvalid](./code/requestinvalid.md)
  The request to create a thumbnail was invalid, for example, there’s no file at a provided URL.
- [QLThumbnailError.Code.savingToURLFailed](./code/savingtourlfailed.md)
  The thumbnail couldn’t be saved at the given URL.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Error Information
- [let QLThumbnailErrorDomain: String](../qlthumbnailerrordomain.md)
  The error domain of the QuickLookThumbnailing framework.
- [struct QLThumbnailError](../qlthumbnailerror-swift.struct.md)
  Error information that might return when you generate a thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailerror-swift.struct/code)*