# RCSService.ReportSpamRequest.Category

**Framework**: TelephonyMessagingKit  
**Kind**: enum

An enumeration of spam types, for use while reporting an RCS message as spam.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum Category
```

## Topics

### Identifying spam categories
- [RCSService.ReportSpamRequest.Category.invalid](rcsservice/reportspamrequest/category-swift.enum/invalid.md)
  RCS message considered as invalid.
- [RCSService.ReportSpamRequest.Category.spam](rcsservice/reportspamrequest/category-swift.enum/spam.md)
  RCS message considered as spam.
- [RCSService.ReportSpamRequest.Category.fraud](rcsservice/reportspamrequest/category-swift.enum/fraud.md)
  RCS message considered as fraud.
- [RCSService.ReportSpamRequest.Category.inappropriateContent](rcsservice/reportspamrequest/category-swift.enum/inappropriatecontent.md)
  RCS message considered as inappropriate content.
- [RCSService.ReportSpamRequest.Category.other](rcsservice/reportspamrequest/category-swift.enum/other.md)
  RCS message considered as other spam category.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var message: RCSMessage](rcsservice/reportspamrequest/message.md)
  The message to report as spam.
- [var fileContent: Data?](rcsservice/reportspamrequest/filecontent.md)
  The content of the file attachment message.
- [var category: RCSService.ReportSpamRequest.Category?](rcsservice/reportspamrequest/category-swift.property.md)
  An optional category to classify the spam type of the message.
- [var reason: String?](rcsservice/reportspamrequest/reason.md)
  An optional reason to report the message as spam.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/reportspamrequest/category-swift.enum)*