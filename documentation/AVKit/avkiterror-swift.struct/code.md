# AVKitError.Code

**Framework**: AVKit  
**Kind**: enum  
**Role**: Enumeration

Constants that identify framework error codes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum AVKitError : NSInteger;
```

## Topics

### Creating an error code
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)
### Error codes
- [AVKitError.Code.unknown](./code/unknown.md)
  An unknown error.
- [AVKitError.Code.contentRatingUnknown](./code/contentratingunknown.md)
  The media content rating is missing or unrecognized.
- [AVKitError.Code.contentDisallowedByPasscode](./code/contentdisallowedbypasscode.md)
  A restriction disallows access to this content, but the user can override the restriction by entering the device passcode.
- [AVKitError.Code.pictureInPictureStartFailed](./code/pictureinpicturestartfailed.md)
  The system failed to start Picture in Picture.
- [AVKitError.Code.contentDisallowedByProfile](./code/contentdisallowedbyprofile.md)
  An installed profile restricts access to this content.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [let AVKitErrorDomain: String](../avkiterrordomain.md)
  The domain of errors the framework generates.
- [struct AVKitError](../avkiterror-swift.struct.md)
  A structure that represents a framework error.
- [Error constants](../error-constants.md)
  Error code constants for framework operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avkiterror-swift.struct/code)*