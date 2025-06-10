# originatingMessageID

**Framework**: TelephonyMessagingKit  
**Kind**: property

Message indentifier of the message that contained the specified suggestion.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst ?+

## Declaration

```swift
var originatingMessageID: RCSMessageID
```

## See Also

- [var cellularServiceID: CellularServiceID](rcsservice/suggestionresponse/cellularserviceid.md)
  Service identifier to use for this response.
- [var destination: RCSHandle](rcsservice/suggestionresponse/destination.md)
  Destination handle to send response to.
- [enum RCSHandle](rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [var messageID: RCSMessageID](rcsservice/suggestionresponse/messageid.md)
  Message identifier to use for this response.
- [struct RCSMessageID](rcsmessageid.md)
  A structure that represents an RCS message identifier.
- [var suggestion: RCSService.Business.Suggestion](rcsservice/suggestionresponse/suggestion.md)
  Suggestion for which to send the response.
- [RCSService.Business.Suggestion](rcsservice/business/suggestion.md)
  Enumeration representing a suggestion from a business.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/suggestionresponse/originatingmessageid)*