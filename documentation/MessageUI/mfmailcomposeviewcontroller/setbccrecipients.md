# setBccRecipients(_:)

**Framework**: Message UI  
**Kind**: method

Sets the initial recipients to include in the email’s Bcc field.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setBccRecipients(_ bccRecipients: [String]?)
```

#### Discussion

This method replaces the previous blind carbon-copy (Bcc) recipients with the new ones listed in the `bccRecipients` parameter. This method doesn’t filter out duplicate email addresses, so if duplicates are present, the recipient may receive multiple copies of the email message.

Only call this method before you display the mail composition interface. Don’t call it after presenting the interface to the user.

> ❗ **Important**:  [`MFMailComposeViewController`](mfmailcomposeviewcontroller.md) ignores calls to this method in Mac apps built with Mac Catalyst.

## Parameters

- `bccRecipients`: An array of   objects, each containing the email address of a single recipient.

## See Also

- [func setSubject(String)](mfmailcomposeviewcontroller/setsubject(_:).md)
  Sets the initial text for the subject line of the email.
- [func setToRecipients([String]?)](mfmailcomposeviewcontroller/settorecipients(_:).md)
  Sets the initial recipients to include in the email’s To field.
- [func setCcRecipients([String]?)](mfmailcomposeviewcontroller/setccrecipients(_:).md)
  Sets the initial recipients to include in the email’s Cc field.
- [func setMessageBody(String, isHTML: Bool)](mfmailcomposeviewcontroller/setmessagebody(_:ishtml:).md)
  Sets the initial body text to include in the email.
- [func addAttachmentData(Data, mimeType: String, fileName: String)](mfmailcomposeviewcontroller/addattachmentdata(_:mimetype:filename:).md)
  Adds the specified data as an attachment to the message.
- [func setPreferredSendingEmailAddress(String)](mfmailcomposeviewcontroller/setpreferredsendingemailaddress(_:).md)
  Sets the preferred email address to use in the From field, if such an address is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/setbccrecipients(_:))*