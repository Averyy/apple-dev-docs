# disableUserAttachments()

**Framework**: Message UI  
**Kind**: method

Disables the camera/attachment button in the message composition view.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func disableUserAttachments()
```

#### Discussion

In iOS 7.0 and later, call this method to disable the camera/attachment button in the message composition view. In an app linked against an older version of iOS, the camera/attachment button is not available in any case.

## See Also

- [var attachments: [[AnyHashable : Any]]?](mfmessagecomposeviewcontroller/attachments.md)
  Returns an array of dictionaries that describe the properties of an attachment.
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

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmessagecomposeviewcontroller/disableuserattachments())*