# contentDisallowedByPasscode

**Framework**: AVKit  
**Kind**: property  
**Role**: Type Property

A restriction disallows access to this content, but the user can override the restriction by entering the device passcode.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
static var contentDisallowedByPasscode: AVKitError.Code { get }
```

## See Also

### Error codes
- [static var unknown: AVKitError.Code](./unknown.md)
  An unknown error.
- [static var contentRatingUnknown: AVKitError.Code](./contentratingunknown.md)
  The media content rating is missing or unrecognized.
- [static var contentDisallowedByProfile: AVKitError.Code](./contentdisallowedbyprofile.md)
  An installed profile restricts access to this content.
- [static var pictureInPictureStartFailed: AVKitError.Code](./pictureinpicturestartfailed.md)
  The system failed to start Picture in Picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avkiterror-swift.struct/contentdisallowedbypasscode)*