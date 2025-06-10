# RCSService.ReportSpamRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct

A structure that contains information about a spam reporting request for an RCS message.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
struct ReportSpamRequest
```

## Topics

### Creating a report spam request
- [init(message: RCSMessage, fileContent: Data?, category: RCSService.ReportSpamRequest.Category?, reason: String?)](rcsservice/reportspamrequest/init(message:filecontent:category:reason:).md)
### Accessing request properties
- [var message: RCSMessage](rcsservice/reportspamrequest/message.md)
  The message to report as spam.
- [var fileContent: Data?](rcsservice/reportspamrequest/filecontent.md)
  The content of the file attachment message.
- [var category: RCSService.ReportSpamRequest.Category?](rcsservice/reportspamrequest/category-swift.property.md)
  An optional category to classify the spam type of the message.
- [RCSService.ReportSpamRequest.Category](rcsservice/reportspamrequest/category-swift.enum.md)
  An enumeration of spam types, for use while reporting an RCS message as spam.
- [var reason: String?](rcsservice/reportspamrequest/reason.md)
  An optional reason to report the message as spam.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func reportSpam(RCSService.ReportSpamRequest) async throws](rcsservice/reportspam(_:).md)
  Reports an RCS message as spam to the carrier and to partners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/reportspamrequest)*