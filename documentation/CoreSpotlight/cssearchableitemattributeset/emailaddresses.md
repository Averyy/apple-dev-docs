# emailAddresses

**Framework**: Core Spotlight  
**Kind**: property

An array of email addresses associated with the message.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
var emailAddresses: [String]? { get set }
```

## See Also

- [Common Mailbox Identifiers](common-mailbox-identifiers.md)
  Constants that describe common mailbox names.
- [var htmlContentData: Data?](cssearchableitemattributeset/htmlcontentdata.md)
  The HTML content of the document encoded as an NSData object representing a UTF-8 encoded string.
- [var accountHandles: [String]?](cssearchableitemattributeset/accounthandles.md)
  An array of the canonical handles for the account with which the message is associated.
- [var accountIdentifier: String?](cssearchableitemattributeset/accountidentifier.md)
  The unique identifier for the account with which the message is associated, if any.
- [var additionalRecipients: [CSPerson]?](cssearchableitemattributeset/additionalrecipients.md)
  An array of [`CSPerson`](csperson.md) objects representing the content of the Cc: field in an email message.
- [var authorAddresses: [String]?](cssearchableitemattributeset/authoraddresses.md)
  An array of addresses associated with the author of the message.
- [var authorEmailAddresses: [String]?](cssearchableitemattributeset/authoremailaddresses.md)
  An array of email addresses associated with the author of the message.
- [var authorNames: [String]?](cssearchableitemattributeset/authornames.md)
  An array of names representing the authors who have worked on the message.
- [var authors: [CSPerson]?](cssearchableitemattributeset/authors.md)
  An array of [`CSPerson`](csperson.md) objects representing the content of the From: field in an item.
- [var emailHeaders: [String : [Any]]?](cssearchableitemattributeset/emailheaders.md)
  A dictionary that contains all the headers of the message.
- [var hiddenAdditionalRecipients: [CSPerson]?](cssearchableitemattributeset/hiddenadditionalrecipients.md)
  An array of [`CSPerson`](csperson.md) objects representing the content of the Bcc: field in an email message.
- [var instantMessageAddresses: [String]?](cssearchableitemattributeset/instantmessageaddresses.md)
  An array of instant message addresses for the message.
- [var likelyJunk: NSNumber](cssearchableitemattributeset/likelyjunk.md)
  A value that indicates if the message is likely to be considered junk.
- [var mailboxIdentifiers: [String]?](cssearchableitemattributeset/mailboxidentifiers.md)
  An array of mailbox identifiers associated with the message.
- [var phoneNumbers: [String]?](cssearchableitemattributeset/phonenumbers.md)
  An array of phone numbers associated with the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corespotlight/cssearchableitemattributeset/emailaddresses)*