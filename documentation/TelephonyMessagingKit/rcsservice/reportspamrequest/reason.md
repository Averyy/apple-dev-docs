# reason

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

An optional reason to report the message as spam.

**Availability**:
- iOS 26.0+

## Declaration

```swift
var reason: String?
```

## See Also

### Accessing request properties
- [var message: RCSMessage](./message.md)
  The message to report as spam.
- [var fileContent: Data?](./filecontent.md)
  The content of the file attachment message.
- [var category: RCSService.ReportSpamRequest.Category?](./category-swift.property.md)
  An optional category to classify the spam type of the message.
- [RCSService.ReportSpamRequest.Category](./category-swift.enum.md)
  An enumeration of spam types, for use while reporting an RCS message as spam.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/reportspamrequest/reason)*