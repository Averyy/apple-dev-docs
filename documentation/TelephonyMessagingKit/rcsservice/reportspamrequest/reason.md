# reason

**Framework**: TelephonyMessagingKit  
**Kind**: property

An optional reason to report the message as spam.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
var reason: String?
```

## See Also

- [var message: RCSMessage](rcsservice/reportspamrequest/message.md)
  The message to report as spam.
- [var fileContent: Data?](rcsservice/reportspamrequest/filecontent.md)
  The content of the file attachment message.
- [var category: RCSService.ReportSpamRequest.Category?](rcsservice/reportspamrequest/category-swift.property.md)
  An optional category to classify the spam type of the message.
- [RCSService.ReportSpamRequest.Category](rcsservice/reportspamrequest/category-swift.enum.md)
  An enumeration of spam types, for use while reporting an RCS message as spam.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/reportspamrequest/reason)*