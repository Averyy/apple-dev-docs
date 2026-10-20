# addAttachmentURL(_:withAlternateFilename:)

**Framework**: Message UI  
**Kind**: method  
**Role**: Instance Method

Attaches a specified file to the message.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addAttachmentURL(_ attachmentURL: URL, withAlternateFilename alternateFilename: String?) -> Bool
```

```objc
- (BOOL) addAttachmentURL:(NSURL *) attachmentURL withAlternateFilename:(NSString *) alternateFilename;
```

#### Return Value

[`true`](../../Swift/true.md) if the attachment at the specified URL was successfully added to the message, or [`false`](../../Swift/false.md) otherwise.

#### Discussion

You can add zero or more attachments to a message before you display the message to the user. To access information about a message’s attachments, access the [`attachments`](./attachments.md) property.

## Parameters

- `attachmentURL`: The file URL for the attachment. Must not be `nil`.
- `alternateFilename`: If you supply a string here, the message UI uses it for the attachment. Use an alternate filename to better describe the attachment or to make the name more readable.

  OK to use a `nil` value, in which case the attachment’s actual filename is displayed in the message UI.

## See Also

### Managing attachments
- [func disableUserAttachments()](./disableuserattachments%28%29.md)
  Disables the camera/attachment button in the message composition view.
- [var attachments: [[AnyHashable : Any]]?](./attachments.md)
  Returns an array of dictionaries that describe the properties of an attachment.
- [func addAttachmentData(Data, typeIdentifier: String, filename: String) -> Bool](./addattachmentdata%28_,typeidentifier,filename%29.md)
  Attaches arbitrary content to the message.
- [let MFMessageComposeViewControllerAttachmentURL: String](../mfmessagecomposeviewcontrollerattachmenturl.md)
  The URL for the item that is attached to the message.
- [let MFMessageComposeViewControllerAttachmentAlternateFilename: String](../mfmessagecomposeviewcontrollerattachmentalternatefilename.md)
  The key for the alternate filename for the file-based item attached to the message.
- [func insertCollaborationItemProvider(NSItemProvider) -> Bool](./insertcollaborationitemprovider%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/addattachmenturl(_:withalternatefilename:))*