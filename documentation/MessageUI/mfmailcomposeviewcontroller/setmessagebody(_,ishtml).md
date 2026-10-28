# setMessageBody(_:isHTML:)

**Framework**: Message UI  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) setMessageBody:(NSString *) body isHTML:(BOOL) isHTML;
```

## Discussion

This method replaces the previous body content with the new content. If the user has a signature file, the body content is inserted immediately before the signature. If you want to include images with your content, you must attach the images separately using the [`addAttachmentData(_:mimeType:fileName:)`](./addattachmentdata%28_,mimetype,filename%29.md) method.

Only call this method before you display the mail composition interface. Don’t call it after presenting the interface to the user.

## Parameters

- `body`: The initial body text of the message. The text is interpreted as either plain text or HTML, depending on the value of the `isHTML` parameter.
- `isHTML`: Specify [`true`](../../Swift/true.md) if the body parameter contains HTML content or specify [`false`](../../Swift/false.md) if it contains plain text.

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
- [func addAttachmentData(Data, mimeType: String, fileName: String)](./addattachmentdata%28_,mimetype,filename%29.md)
  Adds the specified data as an attachment to the message.
- [func setPreferredSendingEmailAddress(String)](./setpreferredsendingemailaddress%28_%29.md)
  Sets the preferred email address to use in the From field, if such an address is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messageui/mfmailcomposeviewcontroller/setmessagebody(_:ishtml:))*