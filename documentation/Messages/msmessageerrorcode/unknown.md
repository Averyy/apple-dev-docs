# MSMessageErrorCode.unknown

**Framework**: Messages  
**Kind**: case

An unexpected or unknown error has occurred.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case unknown
```

## See Also

- [MSMessageErrorCode.fileNotFound](msmessageerrorcode/filenotfound.md)
  The file could not be found.
- [MSMessageErrorCode.fileUnreadable](msmessageerrorcode/fileunreadable.md)
  The file could not be read.
- [MSMessageErrorCode.improperFileType](msmessageerrorcode/improperfiletype.md)
  The file is not a supported file type.
- [MSMessageErrorCode.improperFileURL](msmessageerrorcode/improperfileurl.md)
  The URL does not refer to a local file.
- [MSMessageErrorCode.stickerFileImproperFileAttributes](msmessageerrorcode/stickerfileimproperfileattributes.md)
  The system cannot read one or more of the file’s attributes (for example, the file size).
- [MSMessageErrorCode.stickerFileImproperFileSize](msmessageerrorcode/stickerfileimproperfilesize.md)
  The image used to create an [`MSSticker`](mssticker.md) object is larger than 500 KB.
- [MSMessageErrorCode.stickerFileImproperFileFormat](msmessageerrorcode/stickerfileimproperfileformat.md)
  The image used to create an [`MSSticker`](mssticker.md) object is not one of the supported file types (PNG, APNG, GIF, or JPEG).
- [MSMessageErrorCode.urlExceedsMaxSize](msmessageerrorcode/urlexceedsmaxsize.md)
  The URL in an [`MSMessage`](msmessage.md) object’s [`url`](msmessage/url.md) property is longer than the maximum allowed length (5,000 characters).
- [MSMessageErrorCode.sendWhileNotVisible](msmessageerrorcode/sendwhilenotvisible.md)
  A message was sent while the app was not visible.
- [MSMessageErrorCode.sendWithoutRecentInteraction](msmessageerrorcode/sendwithoutrecentinteraction.md)
  A message was sent, but the app has not registered a recent touch interaction from the user.
- [MSMessageErrorCode.apiUnavailableInPresentationContext](msmessageerrorcode/apiunavailableinpresentationcontext.md)
  The API is unavailable in the current context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessageerrorcode/unknown)*