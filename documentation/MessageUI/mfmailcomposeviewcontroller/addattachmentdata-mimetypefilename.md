# addAttachmentData(_:mimeType:fileName:)

**Framework**: Message UI  
**Kind**: method

Adds the specified data as an attachment to the message.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func addAttachmentData(_ attachment: Data, mimeType: String, fileName filename: String)
```

#### Discussion

This method attaches the specified data after the message body, but before the user’s signature. You may attach multiple files (using different file names), but must do so prior to displaying the mail composition interface. Don’t call this method after presenting the interface to the user.

## Parameters

- `attachment`: The data to attach. Typically, this is the contents of a file that you want to include. This parameter must not be  .
- `mimeType`: The MIME type of the specified data. (For example, the MIME type for a JPEG image is  .) For a list of valid MIME types, see  . This parameter must not be  .
- `filename`: The preferred filename to associate with the data. This is the default name applied to the file when it is transferred to its destination. Any path separator ( ) characters in the filename are converted to underscore ( ) characters prior to transmission. This parameter must not be  .

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
- [func setPreferredSendingEmailAddress(String)](mfmailcomposeviewcontroller/setpreferredsendingemailaddress(_:).md)
  Sets the preferred email address to use in the From field, if such an address is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/addattachmentdata(_:mimetype:filename:))*