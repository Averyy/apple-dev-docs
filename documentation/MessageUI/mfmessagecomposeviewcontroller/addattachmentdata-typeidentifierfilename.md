# addAttachmentData(_:typeIdentifier:filename:)

**Framework**: Message UI  
**Kind**: method

Attaches arbitrary content to the message.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addAttachmentData(_ attachmentData: Data, typeIdentifier uti: String, filename: String) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the attachment data was successfully added to the message, or [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

This method is especially useful when the attachment you want to add to a message does not have a file system representation. This can be the case, for example, for programmatically composed audiovisual content.

## Parameters

- `attachmentData`: Content in the form of an   object to attach to the message. Must not be  .
- `uti`: A valid Uniform Type Identifier (UTI) appropriate for the attachment data. See  . Must not be  .
- `filename`: The name to present to the user, in the message UI, for the data attachment.

## See Also

- [func disableUserAttachments()](mfmessagecomposeviewcontroller/disableuserattachments.md)
  Disables the camera/attachment button in the message composition view.
- [var attachments: [[AnyHashable : Any]]?](mfmessagecomposeviewcontroller/attachments.md)
  Returns an array of dictionaries that describe the properties of an attachment.
- [func addAttachmentURL(URL, withAlternateFilename: String?) -> Bool](mfmessagecomposeviewcontroller/addattachmenturl(_:withalternatefilename:).md)
  Attaches a specified file to the message.
- [let MFMessageComposeViewControllerAttachmentURL: String](mfmessagecomposeviewcontrollerattachmenturl.md)
  The URL for the item that is attached to the message.
- [let MFMessageComposeViewControllerAttachmentAlternateFilename: String](mfmessagecomposeviewcontrollerattachmentalternatefilename.md)
  The key for the alternate filename for the file-based item attached to the message.
- [func insertCollaborationItemProvider(NSItemProvider) -> Bool](mfmessagecomposeviewcontroller/insertcollaborationitemprovider(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/addattachmentdata(_:typeidentifier:filename:))*