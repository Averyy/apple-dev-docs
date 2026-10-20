# RCSService.ReportSpamRequest

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

A structure that contains information about a spam reporting request for an RCS message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct ReportSpamRequest
```

## Topics

### Creating a report spam request
- [init(message: RCSMessage, fileContent: Data?, category: RCSService.ReportSpamRequest.Category?, reason: String?)](./reportspamrequest/init%28message,filecontent,category,reason%29.md)
### Accessing request properties
- [var message: RCSMessage](./reportspamrequest/message.md)
  The message to report as spam.
- [var fileContent: Data?](./reportspamrequest/filecontent.md)
  The content of the file attachment message.
- [var category: RCSService.ReportSpamRequest.Category?](./reportspamrequest/category-swift.property.md)
  An optional category to classify the spam type of the message.
- [RCSService.ReportSpamRequest.Category](./reportspamrequest/category-swift.enum.md)
  An enumeration of spam types, for use while reporting an RCS message as spam.
- [var reason: String?](./reportspamrequest/reason.md)
  An optional reason to report the message as spam.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Reporting spam
- [func reportSpam(RCSService.ReportSpamRequest) async throws](./reportspam%28_%29.md)
  Reports an RCS message as spam to the carrier and to partners.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/reportspamrequest)*