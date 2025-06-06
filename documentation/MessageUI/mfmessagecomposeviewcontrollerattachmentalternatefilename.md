# MFMessageComposeViewControllerAttachmentAlternateFilename

**Framework**: Message UI  
**Kind**: var

The key for the alternate filename for the file-based item attached to the message.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
let MFMessageComposeViewControllerAttachmentAlternateFilename: String
```

#### Discussion

Use this constant with the [`attachments`](mfmessagecomposeviewcontroller/attachments.md) property to retrieve the optional, more descriptive name for a message attachment.

## See Also

- [func disableUserAttachments()](mfmessagecomposeviewcontroller/disableuserattachments.md)
  Disables the camera/attachment button in the message composition view.
- [var attachments: [[AnyHashable : Any]]?](mfmessagecomposeviewcontroller/attachments.md)
  Returns an array of dictionaries that describe the properties of an attachment.
- [func addAttachmentURL(URL, withAlternateFilename: String?) -> Bool](mfmessagecomposeviewcontroller/addattachmenturl(_:withalternatefilename:).md)
  Attaches a specified file to the message.
- [func addAttachmentData(Data, typeIdentifier: String, filename: String) -> Bool](mfmessagecomposeviewcontroller/addattachmentdata(_:typeidentifier:filename:).md)
  Attaches arbitrary content to the message.
- [let MFMessageComposeViewControllerAttachmentURL: String](mfmessagecomposeviewcontrollerattachmenturl.md)
  The URL for the item that is attached to the message.
- [func insertCollaborationItemProvider(NSItemProvider) -> Bool](mfmessagecomposeviewcontroller/insertcollaborationitemprovider(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollerattachmentalternatefilename)*