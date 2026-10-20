# sendFailed

**Framework**: Message UI  
**Kind**: property  
**Role**: Type Property

An error occurred while trying to queue or send the email message.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static var sendFailed: MFMailComposeError.Code { get }
```

## See Also

### Errors
- [static var errorDomain: String](./errordomain.md)
  The domain for errors related to mail composition.
- [static var saveFailed: MFMailComposeError.Code](./savefailed.md)
  An error occurred while trying to save the email message to the drafts folder.
- [MFMailComposeError.Code](./code.md)
  Error codes for [`NSError`](../../Foundation/nserror.md) objects that are associated with the mail composition interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeerror/sendfailed)*