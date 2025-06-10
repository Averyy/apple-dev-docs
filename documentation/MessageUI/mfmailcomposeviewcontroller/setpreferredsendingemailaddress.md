# setPreferredSendingEmailAddress(_:)

**Framework**: Message UI  
**Kind**: method

Sets the preferred email address to use in the From field, if such an address is available.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setPreferredSendingEmailAddress(_ emailAddress: String)
```

#### Discussion

If the user doesn’t have an account with a preferred address set up, the default account is used instead.

Only call this method before you display the mail composition interface. Don’t call it after presenting the interface to the user.

## Parameters

- `emailAddress`: The preferred email address used to send this message.

## See Also

- [func setSubject(String)](mfmailcomposeviewcontroller/setsubject(_:).md)
  Sets the initial text for the subject line of the email.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/setpreferredsendingemailaddress(_:))*