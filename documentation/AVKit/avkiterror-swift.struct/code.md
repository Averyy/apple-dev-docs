# AVKitError.Code

**Framework**: AVKit  
**Kind**: enum

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

## Topics

### Creating an error code
- [init?(rawValue: Int)](avkiterror-swift.struct/code/init(rawvalue:).md)
### Error Codes
- [AVKitError.Code.unknown](avkiterror-swift.struct/code/unknown.md)
  An unknown error.
- [AVKitError.Code.contentRatingUnknown](avkiterror-swift.struct/code/contentratingunknown.md)
  The media content rating is missing or unrecognized.
- [AVKitError.Code.contentDisallowedByPasscode](avkiterror-swift.struct/code/contentdisallowedbypasscode.md)
  A restriction disallows access to this content, but the user can override the restriction by entering the device passcode.
- [AVKitError.Code.pictureInPictureStartFailed](avkiterror-swift.struct/code/pictureinpicturestartfailed.md)
  The system failed to start Picture in Picture.
- [AVKitError.Code.contentDisallowedByProfile](avkiterror-swift.struct/code/contentdisallowedbyprofile.md)
  An installed profile restricts access to this content.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let AVKitErrorDomain: String](avkiterrordomain.md)
  The domain of errors the framework generates.
- [struct AVKitError](avkiterror-swift.struct.md)
  A structure that represents a framework error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avkiterror-swift.struct/code)*