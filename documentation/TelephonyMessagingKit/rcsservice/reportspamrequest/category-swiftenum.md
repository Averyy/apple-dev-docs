# RCSService.ReportSpamRequest.Category

**Framework**: TelephonyMessagingKit  
**Kind**: enum

An enumeration of spam types, for use while reporting an RCS message as spam.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

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
### Encoding and decoding
- [init(from: any Decoder) throws](rcsservice/reportspamrequest/category-swift.enum/init(from:).md)
  Creates a new instance by decoding from the given decoder.
### Operators
- [static func == (RCSService.ReportSpamRequest.Category, RCSService.ReportSpamRequest.Category) -> Bool](rcsservice/reportspamrequest/category-swift.enum/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var hashValue: Int](rcsservice/reportspamrequest/category-swift.enum/hashvalue.md)
  The hash value.
### Instance Methods
- [func encode(to: any Encoder) throws](rcsservice/reportspamrequest/category-swift.enum/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](rcsservice/reportspamrequest/category-swift.enum/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [Equatable Implementations](rcsservice/reportspamrequest/category-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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