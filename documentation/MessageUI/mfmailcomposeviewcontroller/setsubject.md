# setSubject(_:)

**Framework**: Message UI  
**Kind**: method

Sets the initial text for the subject line of the email.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setSubject(_ subject: String)
```

#### Discussion

This method replaces the previous subject text with the new text. Only call this method before you display the mail composition interface. Don’t call it after presenting the interface to the user.

## Parameters

- `subject`: The text to display in the subject line.

## See Also

- [func setToRecipients([String]?)](mfmailcomposeviewcontroller/settorecipients(_:).md)
  Sets the initial recipients to include in the email’s To field.
- [func setCcRecipients([String]?)](mfmailcomposeviewcontroller/setccrecipients(_:).md)
  Sets the initial recipients to include in the email’s Cc field.
- [func setBccRecipients([String]?)](mfmailcomposeviewcontroller/setbccrecipients(_:).md)
  Sets the initial recipients to include in the email’s Bcc field.
- [func setMessageBody(String, isHTML: Bool)](mfmailcomposeviewcontroller/setmessagebody(_:ishtml:).md)
  Sets the initial body text to include in the email.
- [func addAttachmentData(Data, mimeType: String, fileName: String)](mfmailcomposeviewcontroller/addattachmentdata(_:mimetype:filename:).md)
  Adds the specified data as an attachment to the message.
- [func setPreferredSendingEmailAddress(String)](mfmailcomposeviewcontroller/setpreferredsendingemailaddress(_:).md)
  Sets the preferred email address to use in the From field, if such an address is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/setsubject(_:))*