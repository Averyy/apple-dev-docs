# setBccRecipients(_:)

**Framework**: Message UI  
**Kind**: method  
**Role**: Instance Method

Sets the initial recipients to include in the email’s Bcc field.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func setBccRecipients(_ bccRecipients: [String]?)
```

```objc
- (void) setBccRecipients:(NSArray<NSString *> *) bccRecipients;
```

## Discussion

This method replaces the previous blind carbon-copy (Bcc) recipients with the new ones listed in the `bccRecipients` parameter. This method doesn’t filter out duplicate email addresses, so if duplicates are present, the recipient may receive multiple copies of the email message.

Only call this method before you display the mail composition interface. Don’t call it after presenting the interface to the user.

> ❗ **Important**:  [`MFMailComposeViewController`](../mfmailcomposeviewcontroller.md) ignores calls to this method in Mac apps built with Mac Catalyst.

## Parameters

- `bccRecipients`: An array of [`String`](../../Swift/string.md) objects, each containing the email address of a single recipient.

## See Also

### Setting mail fields programmatically
- [func setSubject(String)](./setsubject%28_%29.md)
  Sets the initial text for the subject line of the email.
- [func setToRecipients([String]?)](./settorecipients%28_%29.md)
  Sets the initial recipients to include in the email’s To field.
- [func setCcRecipients([String]?)](./setccrecipients%28_%29.md)
  Sets the initial recipients to include in the email’s Cc field.
- [func setMessageBody(String, isHTML: Bool)](./setmessagebody%28_,ishtml%29.md)
  Sets the initial body text to include in the email.
- [func addAttachmentData(Data, mimeType: String, fileName: String)](./addattachmentdata%28_,mimetype,filename%29.md)
  Adds the specified data as an attachment to the message.
- [func setPreferredSendingEmailAddress(String)](./setpreferredsendingemailaddress%28_%29.md)
  Sets the preferred email address to use in the From field, if such an address is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/setbccrecipients(_:))*