# RCSService.SuggestionResponse

**Framework**: TelephonyMessagingKit  
**Kind**: struct

Structure representing a response to a business suggestion.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+

## Declaration

```swift
struct SuggestionResponse
```

## Topics

### Creating a suggestion response
- [init(cellularServiceID: CellularServiceID, destination: RCSHandle, messageID: RCSMessageID, originatingMessageID: RCSMessageID, suggestion: RCSService.Business.Suggestion)](rcsservice/suggestionresponse/init(cellularserviceid:destination:messageid:originatingmessageid:suggestion:).md)
### Accessing response properties
- [var cellularServiceID: CellularServiceID](rcsservice/suggestionresponse/cellularserviceid.md)
  Service identifier to use for this response.
- [var destination: RCSHandle](rcsservice/suggestionresponse/destination.md)
  Destination handle to send response to.
- [enum RCSHandle](rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [var messageID: RCSMessageID](rcsservice/suggestionresponse/messageid.md)
  Message identifier to use for this response.
- [var originatingMessageID: RCSMessageID](rcsservice/suggestionresponse/originatingmessageid.md)
  Message indentifier of the message that contained the specified suggestion.
- [struct RCSMessageID](rcsmessageid.md)
  A structure that represents an RCS message identifier.
- [var suggestion: RCSService.Business.Suggestion](rcsservice/suggestionresponse/suggestion.md)
  Suggestion for which to send the response.
- [RCSService.Business.Suggestion](rcsservice/business/suggestion.md)
  Enumeration representing a suggestion from a business.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func sendSuggestionResponse(RCSService.SuggestionResponse) async throws](rcsservice/sendsuggestionresponse(_:).md)
  Sends a response for a business suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/suggestionresponse)*