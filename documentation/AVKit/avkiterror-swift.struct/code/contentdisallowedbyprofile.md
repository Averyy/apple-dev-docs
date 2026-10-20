# AVKitError.Code.contentDisallowedByProfile

**Framework**: AVKit  
**Kind**: case  
**Role**: Case

An installed profile restricts access to this content.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
case contentDisallowedByProfile
```

```c
AVKitErrorContentDisallowedByProfile
```

#### Discussion

The user can’t override this restriction by entering the device passcode, but they may be able to override it in the Settings app.

## See Also

### Error codes
- [AVKitError.Code.unknown](./unknown.md)
  An unknown error.
- [AVKitError.Code.contentRatingUnknown](./contentratingunknown.md)
  The media content rating is missing or unrecognized.
- [AVKitError.Code.contentDisallowedByPasscode](./contentdisallowedbypasscode.md)
  A restriction disallows access to this content, but the user can override the restriction by entering the device passcode.
- [AVKitError.Code.pictureInPictureStartFailed](./pictureinpicturestartfailed.md)
  The system failed to start Picture in Picture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avkiterror-swift.struct/code/contentdisallowedbyprofile)*