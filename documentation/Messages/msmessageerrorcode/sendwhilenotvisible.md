# MSMessageErrorCode.sendWhileNotVisible

**Framework**: Messages  
**Kind**: case  
**Role**: Case

A message was sent while the app was not visible.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
case sendWhileNotVisible
```

```c
MSMessageErrorCodeSendWhileNotVisible
```

#### Discussion

An iMessage app can send messages only in response to user interaction with the app. If an app isn’t currently visible and onscreen, it can’t send any messages.

## See Also

### Error Codes
- [MSMessageErrorCode.fileNotFound](./filenotfound.md)
  The file could not be found.
- [MSMessageErrorCode.fileUnreadable](./fileunreadable.md)
  The file could not be read.
- [MSMessageErrorCode.improperFileType](./improperfiletype.md)
  The file is not a supported file type.
- [MSMessageErrorCode.improperFileURL](./improperfileurl.md)
  The URL does not refer to a local file.
- [MSMessageErrorCode.stickerFileImproperFileAttributes](./stickerfileimproperfileattributes.md)
  The system cannot read one or more of the file’s attributes (for example, the file size).
- [MSMessageErrorCode.stickerFileImproperFileSize](./stickerfileimproperfilesize.md)
  The image used to create an [`MSSticker`](../mssticker.md) object is larger than 500 KB.
- [MSMessageErrorCode.stickerFileImproperFileFormat](./stickerfileimproperfileformat.md)
  The image used to create an [`MSSticker`](../mssticker.md) object is not one of the supported file types (PNG, APNG, GIF, or JPEG).
- [MSMessageErrorCode.urlExceedsMaxSize](./urlexceedsmaxsize.md)
  The URL in an [`MSMessage`](../msmessage.md) object’s [`url`](../msmessage/url.md) property is longer than the maximum allowed length (5,000 characters).
- [MSMessageErrorCode.sendWithoutRecentInteraction](./sendwithoutrecentinteraction.md)
  A message was sent, but the app has not registered a recent touch interaction from the user.
- [MSMessageErrorCode.apiUnavailableInPresentationContext](./apiunavailableinpresentationcontext.md)
  The API is unavailable in the current context.
- [MSMessageErrorCode.unknown](./unknown.md)
  An unexpected or unknown error has occurred.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/msmessageerrorcode/sendwhilenotvisible)*