# addAttachmentURL(_:withAlternateFilename:)

**Framework**: Message UI  
**Kind**: method

Attaches a specified file to the message.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func addAttachmentURL(_ attachmentURL: URL, withAlternateFilename alternateFilename: String?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the attachment at the specified URL was successfully added to the message, or [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

You can add zero or more attachments to a message before you display the message to the user. To access information about a message’s attachments, access the [`attachments`](mfmessagecomposeviewcontroller/attachments.md) property.

## Parameters

- `attachmentURL`: The file URL for the attachment. Must not be  .
- `alternateFilename`: OK to use a   value, in which case the attachment’s actual filename is displayed in the message UI.

## See Also

- [func disableUserAttachments()](mfmessagecomposeviewcontroller/disableuserattachments.md)
  Disables the camera/attachment button in the message composition view.
- [var attachments: [[AnyHashable : Any]]?](mfmessagecomposeviewcontroller/attachments.md)
  Returns an array of dictionaries that describe the properties of an attachment.
- [func addAttachmentData(Data, typeIdentifier: String, filename: String) -> Bool](mfmessagecomposeviewcontroller/addattachmentdata(_:typeidentifier:filename:).md)
  Attaches arbitrary content to the message.
- [let MFMessageComposeViewControllerAttachmentURL: String](mfmessagecomposeviewcontrollerattachmenturl.md)
  The URL for the item that is attached to the message.
- [let MFMessageComposeViewControllerAttachmentAlternateFilename: String](mfmessagecomposeviewcontrollerattachmentalternatefilename.md)
  The key for the alternate filename for the file-based item attached to the message.
- [func insertCollaborationItemProvider(NSItemProvider) -> Bool](mfmessagecomposeviewcontroller/insertcollaborationitemprovider(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/addattachmenturl(_:withalternatefilename:))*