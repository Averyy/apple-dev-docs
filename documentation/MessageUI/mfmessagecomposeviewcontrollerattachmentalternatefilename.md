# MFMessageComposeViewControllerAttachmentAlternateFilename

**Framework**: Message UI  
**Kind**: var  
**Role**: Global Variable

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

```c
extern NSString * const MFMessageComposeViewControllerAttachmentAlternateFilename;
```

#### Discussion

Use this constant with the [`attachments`](./mfmessagecomposeviewcontroller/attachments.md) property to retrieve the optional, more descriptive name for a message attachment.

## See Also

### Managing attachments
- [func disableUserAttachments()](./mfmessagecomposeviewcontroller/disableuserattachments%28%29.md)
  Disables the camera/attachment button in the message composition view.
- [var attachments: [[AnyHashable : Any]]?](./mfmessagecomposeviewcontroller/attachments.md)
  Returns an array of dictionaries that describe the properties of an attachment.
- [func addAttachmentURL(URL, withAlternateFilename: String?) -> Bool](./mfmessagecomposeviewcontroller/addattachmenturl%28_,withalternatefilename%29.md)
  Attaches a specified file to the message.
- [func addAttachmentData(Data, typeIdentifier: String, filename: String) -> Bool](./mfmessagecomposeviewcontroller/addattachmentdata%28_,typeidentifier,filename%29.md)
  Attaches arbitrary content to the message.
- [let MFMessageComposeViewControllerAttachmentURL: String](./mfmessagecomposeviewcontrollerattachmenturl.md)
  The URL for the item that is attached to the message.
- [func insertCollaborationItemProvider(NSItemProvider) -> Bool](./mfmessagecomposeviewcontroller/insertcollaborationitemprovider%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontrollerattachmentalternatefilename)*