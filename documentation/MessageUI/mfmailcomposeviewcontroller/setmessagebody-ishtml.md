# setMessageBody(_:isHTML:)

**Framework**: Message UI  
**Kind**: method

Sets the initial body text to include in the email.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setMessageBody(_ body: String, isHTML: Bool)
```

#### Discussion

This method replaces the previous body content with the new content. If the user has a signature file, the body content is inserted immediately before the signature. If you want to include images with your content, you must attach the images separately using the [`addAttachmentData(_:mimeType:fileName:)`](mfmailcomposeviewcontroller/addattachmentdata(_:mimetype:filename:).md) method.

Only call this method before you display the mail composition interface. Don’t call it after presenting the interface to the user.

## Parameters

- `body`: The initial body text of the message. The text is interpreted as either plain text or HTML, depending on the value of the   parameter.
- `isHTML`: Specify   if the body parameter contains HTML content or specify   if it contains plain text.

## See Also

- [func setSubject(String)](mfmailcomposeviewcontroller/setsubject(_:).md)
  Sets the initial text for the subject line of the email.
- [func setToRecipients([String]?)](mfmailcomposeviewcontroller/settorecipients(_:).md)
  Sets the initial recipients to include in the email’s To field.
- [func setCcRecipients([String]?)](mfmailcomposeviewcontroller/setccrecipients(_:).md)
  Sets the initial recipients to include in the email’s Cc field.
- [func setBccRecipients([String]?)](mfmailcomposeviewcontroller/setbccrecipients(_:).md)
  Sets the initial recipients to include in the email’s Bcc field.
- [func addAttachmentData(Data, mimeType: String, fileName: String)](mfmailcomposeviewcontroller/addattachmentdata(_:mimetype:filename:).md)
  Adds the specified data as an attachment to the message.
- [func setPreferredSendingEmailAddress(String)](mfmailcomposeviewcontroller/setpreferredsendingemailaddress(_:).md)
  Sets the preferred email address to use in the From field, if such an address is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/setmessagebody(_:ishtml:))*