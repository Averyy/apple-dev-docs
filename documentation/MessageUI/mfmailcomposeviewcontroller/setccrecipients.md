# setCcRecipients(_:)

**Framework**: Message UI  
**Kind**: method

Sets the initial recipients to include in the email’s Cc field.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setCcRecipients(_ ccRecipients: [String]?)
```

#### Discussion

This method replaces the previous carbon-copy (Cc) recipients with the new ones listed in the `ccRecipients` parameter. This method doesn’t filter out duplicate email addresses, so if duplicates are present, multiple copies of the email message may be sent to the same address.

Only call this method before you display the mail composition interface. Don’t call it after presenting the interface to the user.

## Parameters

- `ccRecipients`: An array of   objects, each containing the email address of a single recipient.

## See Also

- [func setSubject(String)](mfmailcomposeviewcontroller/setsubject(_:).md)
  Sets the initial text for the subject line of the email.
- [func setToRecipients([String]?)](mfmailcomposeviewcontroller/settorecipients(_:).md)
  Sets the initial recipients to include in the email’s To field.
- [func setBccRecipients([String]?)](mfmailcomposeviewcontroller/setbccrecipients(_:).md)
  Sets the initial recipients to include in the email’s Bcc field.
- [func setMessageBody(String, isHTML: Bool)](mfmailcomposeviewcontroller/setmessagebody(_:ishtml:).md)
  Sets the initial body text to include in the email.
- [func addAttachmentData(Data, mimeType: String, fileName: String)](mfmailcomposeviewcontroller/addattachmentdata(_:mimetype:filename:).md)
  Adds the specified data as an attachment to the message.
- [func setPreferredSendingEmailAddress(String)](mfmailcomposeviewcontroller/setpreferredsendingemailaddress(_:).md)
  Sets the preferred email address to use in the From field, if such an address is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/setccrecipients(_:))*