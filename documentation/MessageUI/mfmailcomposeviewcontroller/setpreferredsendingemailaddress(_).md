# setPreferredSendingEmailAddress(_:)

**Framework**: Message UI  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setPreferredSendingEmailAddress:(NSString *) emailAddress;
```

## Discussion

If the user doesn’t have an account with a preferred address set up, the default account is used instead.

Only call this method before you display the mail composition interface. Don’t call it after presenting the interface to the user.

## Parameters

- `emailAddress`: The preferred email address used to send this message.

## See Also

### Setting mail fields programmatically
- [func setSubject(String)](./setsubject%28_%29.md)
  Sets the initial text for the subject line of the email.
- [func setToRecipients([String]?)](./settorecipients%28_%29.md)
  Sets the initial recipients to include in the email’s To field.
- [func setCcRecipients([String]?)](./setccrecipients%28_%29.md)
  Sets the initial recipients to include in the email’s Cc field.
- [func setBccRecipients([String]?)](./setbccrecipients%28_%29.md)
  Sets the initial recipients to include in the email’s Bcc field.
- [func setMessageBody(String, isHTML: Bool)](./setmessagebody%28_,ishtml%29.md)
  Sets the initial body text to include in the email.
- [func addAttachmentData(Data, mimeType: String, fileName: String)](./addattachmentdata%28_,mimetype,filename%29.md)
  Adds the specified data as an attachment to the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/setpreferredsendingemailaddress(_:))*