# contentDisallowedByProfile

**Framework**: AVKit  
**Kind**: property  
**Role**: Type Property

An installed profile restricts access to this content.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
static var contentDisallowedByProfile: AVKitError.Code { get }
```

#### Discussion

The user can’t override this restriction by entering the passcode, but they may be able to override it in the Settings app.

## See Also

### Error codes
- [static var unknown: AVKitError.Code](./unknown.md)
  An unknown error.
- [static var contentRatingUnknown: AVKitError.Code](./contentratingunknown.md)
  The media content rating is missing or unrecognized.
- [static var contentDisallowedByPasscode: AVKitError.Code](./contentdisallowedbypasscode.md)
  A restriction disallows access to this content, but the user can override the restriction by entering the device passcode.
- [static var pictureInPictureStartFailed: AVKitError.Code](./pictureinpicturestartfailed.md)
  The system failed to start Picture in Picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avkiterror-swift.struct/contentdisallowedbyprofile)*