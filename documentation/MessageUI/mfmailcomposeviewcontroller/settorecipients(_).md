# setToRecipients(_:)

**Framework**: Message UI  
**Kind**: method  
**Role**: Instance Method

Sets the initial recipients to include in the email’s To field.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setToRecipients(_ toRecipients: [String]?)
```

```objc
- (void) setToRecipients:(NSArray<NSString *> *) toRecipients;
```

## Discussion

This method replaces the previous recipients with the new ones listed in the `toRecipients` parameter. This method doesn’t filter out duplicate email addresses, so if duplicates are present, multiple copies of the email message may be sent to the same address.

Only call this method before you display the mail composition interface. Don’t call it after presenting the interface to the user.

## Parameters

- `toRecipients`: An array of [`String`](../../Swift/string.md) objects, each containing the email address of a single recipient.

## See Also

### Setting mail fields programmatically
- [func setSubject(String)](./setsubject%28_%29.md)
  Sets the initial text for the subject line of the email.
- [func setCcRecipients([String]?)](./setccrecipients%28_%29.md)
  Sets the initial recipients to include in the email’s Cc field.
- [func setBccRecipients([String]?)](./setbccrecipients%28_%29.md)
  Sets the initial recipients to include in the email’s Bcc field.
- [func setMessageBody(String, isHTML: Bool)](./setmessagebody%28_,ishtml%29.md)
  Sets the initial body text to include in the email.
- [func addAttachmentData(Data, mimeType: String, fileName: String)](./addattachmentdata%28_,mimetype,filename%29.md)
  Adds the specified data as an attachment to the message.
- [func setPreferredSendingEmailAddress(String)](./setpreferredsendingemailaddress%28_%29.md)
  Sets the preferred email address to use in the From field, if such an address is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/settorecipients(_:))*