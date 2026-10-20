# RCSService.ReportSpamRequest.Category

**Framework**: TelephonyMessagingKit  
**Kind**: enum  
**Role**: Enumeration

An enumeration of spam types, for use while reporting an RCS message as spam.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum Category
```

## Topics

### Identifying spam categories
- [RCSService.ReportSpamRequest.Category.invalid](./category-swift.enum/invalid.md)
  RCS message considered as invalid.
- [RCSService.ReportSpamRequest.Category.spam](./category-swift.enum/spam.md)
  RCS message considered as spam.
- [RCSService.ReportSpamRequest.Category.fraud](./category-swift.enum/fraud.md)
  RCS message considered as fraud.
- [RCSService.ReportSpamRequest.Category.inappropriateContent](./category-swift.enum/inappropriatecontent.md)
  RCS message considered as inappropriate content.
- [RCSService.ReportSpamRequest.Category.other](./category-swift.enum/other.md)
  RCS message considered as other spam category.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Accessing request properties
- [var message: RCSMessage](./message.md)
  The message to report as spam.
- [var fileContent: Data?](./filecontent.md)
  The content of the file attachment message.
- [var category: RCSService.ReportSpamRequest.Category?](./category-swift.property.md)
  An optional category to classify the spam type of the message.
- [var reason: String?](./reason.md)
  An optional reason to report the message as spam.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/reportspamrequest/category-swift.enum)*