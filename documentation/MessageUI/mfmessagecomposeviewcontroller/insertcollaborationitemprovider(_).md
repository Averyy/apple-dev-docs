# insertCollaborationItemProvider(_:)

**Framework**: Message UI  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
func insertCollaborationItemProvider(_ itemProvider: NSItemProvider) -> Bool
```

```objc
- (BOOL) insertCollaborationItemProvider:(NSItemProvider *) itemProvider;
```

## See Also

### Managing attachments
- [func disableUserAttachments()](./disableuserattachments%28%29.md)
  Disables the camera/attachment button in the message composition view.
- [var attachments: [[AnyHashable : Any]]?](./attachments.md)
  Returns an array of dictionaries that describe the properties of an attachment.
- [func addAttachmentURL(URL, withAlternateFilename: String?) -> Bool](./addattachmenturl%28_,withalternatefilename%29.md)
  Attaches a specified file to the message.
- [func addAttachmentData(Data, typeIdentifier: String, filename: String) -> Bool](./addattachmentdata%28_,typeidentifier,filename%29.md)
  Attaches arbitrary content to the message.
- [let MFMessageComposeViewControllerAttachmentURL: String](../mfmessagecomposeviewcontrollerattachmenturl.md)
  The URL for the item that is attached to the message.
- [let MFMessageComposeViewControllerAttachmentAlternateFilename: String](../mfmessagecomposeviewcontrollerattachmentalternatefilename.md)
  The key for the alternate filename for the file-based item attached to the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/insertcollaborationitemprovider(_:))*