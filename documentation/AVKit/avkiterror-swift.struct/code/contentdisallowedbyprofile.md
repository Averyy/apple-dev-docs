# AVKitError.Code.contentDisallowedByProfile

**Framework**: AVKit  
**Kind**: case

An installed profile restricts access to this content.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
case contentDisallowedByProfile
```

#### Discussion

The user can’t override this restriction by entering the device passcode, but they may be able to override it in the Settings app.

## See Also

- [AVKitError.Code.unknown](avkiterror-swift.struct/code/unknown.md)
  An unknown error.
- [AVKitError.Code.contentRatingUnknown](avkiterror-swift.struct/code/contentratingunknown.md)
  The media content rating is missing or unrecognized.
- [AVKitError.Code.contentDisallowedByPasscode](avkiterror-swift.struct/code/contentdisallowedbypasscode.md)
  A restriction disallows access to this content, but the user can override the restriction by entering the device passcode.
- [AVKitError.Code.pictureInPictureStartFailed](avkiterror-swift.struct/code/pictureinpicturestartfailed.md)
  The system failed to start Picture in Picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avkiterror-swift.struct/code/contentdisallowedbyprofile)*