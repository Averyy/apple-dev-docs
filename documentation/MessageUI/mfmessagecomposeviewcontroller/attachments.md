# attachments

**Framework**: Message UI  
**Kind**: property

Returns an array of dictionaries that describe the properties of an attachment.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var attachments: [[AnyHashable : Any]]? { get }
```

#### Discussion

Each attachment is described by an [`NSDictionary`](https://developer.apple.com/documentation/Foundation/NSDictionary) object in the `attachments` array. To retrieve the alternate file name for an attachment from its dictionary, use the [`MFMessageComposeViewControllerAttachmentAlternateFilename`](mfmessagecomposeviewcontrollerattachmentalternatefilename.md) key.

## See Also

- [func disableUserAttachments()](mfmessagecomposeviewcontroller/disableuserattachments.md)
  Disables the camera/attachment button in the message composition view.
- [func addAttachmentURL(URL, withAlternateFilename: String?) -> Bool](mfmessagecomposeviewcontroller/addattachmenturl(_:withalternatefilename:).md)
  Attaches a specified file to the message.
- [func addAttachmentData(Data, typeIdentifier: String, filename: String) -> Bool](mfmessagecomposeviewcontroller/addattachmentdata(_:typeidentifier:filename:).md)
  Attaches arbitrary content to the message.
- [let MFMessageComposeViewControllerAttachmentURL: String](mfmessagecomposeviewcontrollerattachmenturl.md)
  The URL for the item that is attached to the message.
- [let MFMessageComposeViewControllerAttachmentAlternateFilename: String](mfmessagecomposeviewcontrollerattachmentalternatefilename.md)
  The key for the alternate filename for the file-based item attached to the message.
- [func insertCollaborationItemProvider(NSItemProvider) -> Bool](mfmessagecomposeviewcontroller/insertcollaborationitemprovider(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/attachments)*