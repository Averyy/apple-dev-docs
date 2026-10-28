# addAttachmentData(_:typeIdentifier:filename:)

**Framework**: Message UI  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (BOOL) addAttachmentData:(NSData *) attachmentData typeIdentifier:(NSString *) uti filename:(NSString *) filename;
```

## Return Value

[`true`](../../Swift/true.md) if the attachment data was successfully added to the message, or [`false`](../../Swift/false.md) otherwise.

## Discussion

This method is especially useful when the attachment you want to add to a message does not have a file system representation. This can be the case, for example, for programmatically composed audiovisual content.

## Parameters

- `attachmentData`: Content in the form of an [`NSData`](../../Foundation/nsdata.md) object to attach to the message. Must not be `nil`.
- `uti`: A valid Uniform Type Identifier (UTI) appropriate for the attachment data. See [Uniform Type Identifiers Reference](https://developer.apple.com/library/archive/documentation/Miscellaneous/Reference/UTIRef/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009257). Must not be `nil`.
- `filename`: The name to present to the user, in the message UI, for the data attachment.

## See Also

### Managing attachments
- [func disableUserAttachments()](./disableuserattachments%28%29.md)
  Disables the camera/attachment button in the message composition view.
- [var attachments: [[AnyHashable : Any]]?](./attachments.md)
  Returns an array of dictionaries that describe the properties of an attachment.
- [func addAttachmentURL(URL, withAlternateFilename: String?) -> Bool](./addattachmenturl%28_,withalternatefilename%29.md)
  Attaches a specified file to the message.
- [let MFMessageComposeViewControllerAttachmentURL: String](../mfmessagecomposeviewcontrollerattachmenturl.md)
  The URL for the item that is attached to the message.
- [let MFMessageComposeViewControllerAttachmentAlternateFilename: String](../mfmessagecomposeviewcontrollerattachmentalternatefilename.md)
  The key for the alternate filename for the file-based item attached to the message.
- [func insertCollaborationItemProvider(NSItemProvider) -> Bool](./insertcollaborationitemprovider%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/addattachmentdata(_:typeidentifier:filename:))*