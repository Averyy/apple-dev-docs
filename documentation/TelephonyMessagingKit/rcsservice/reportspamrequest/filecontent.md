# fileContent

**Framework**: TelephonyMessagingKit  
**Kind**: property  
**Role**: Instance Property

The content of the file attachment message.

**Availability**:
- iOS 26.0+

## Declaration

```swift
var fileContent: Data?
```

#### Discussion

When possible, supply downloaded file content when reporting a message as spam.

## See Also

### Accessing request properties
- [var message: RCSMessage](./message.md)
  The message to report as spam.
- [var category: RCSService.ReportSpamRequest.Category?](./category-swift.property.md)
  An optional category to classify the spam type of the message.
- [RCSService.ReportSpamRequest.Category](./category-swift.enum.md)
  An enumeration of spam types, for use while reporting an RCS message as spam.
- [var reason: String?](./reason.md)
  An optional reason to report the message as spam.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/reportspamrequest/filecontent)*