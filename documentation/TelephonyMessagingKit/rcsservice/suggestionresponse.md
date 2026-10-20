# RCSService.SuggestionResponse

**Framework**: TelephonyMessagingKit  
**Kind**: struct  
**Role**: Structure

Structure representing a response to a business suggestion.

**Availability**:
- iOS 26.0+

## Declaration

```swift
struct SuggestionResponse
```

## Topics

### Creating a suggestion response
- [init(cellularServiceID: CellularServiceID, destination: RCSHandle, messageID: RCSMessageID, originatingMessageID: RCSMessageID, suggestion: RCSService.Business.Suggestion)](./suggestionresponse/init%28cellularserviceid,destination,messageid,originatingmessageid,suggestion%29.md)
### Accessing response properties
- [var cellularServiceID: CellularServiceID](./suggestionresponse/cellularserviceid.md)
  Service identifier to use for this response.
- [var destination: RCSHandle](./suggestionresponse/destination.md)
  Destination handle to send response to.
- [enum RCSHandle](../rcshandle.md)
  An enumeration that represents an RCS destination or sender.
- [var messageID: RCSMessageID](./suggestionresponse/messageid.md)
  Message identifier to use for this response.
- [var originatingMessageID: RCSMessageID](./suggestionresponse/originatingmessageid.md)
  Message indentifier of the message that contained the specified suggestion.
- [struct RCSMessageID](../rcsmessageid.md)
  A structure that represents an RCS message identifier.
- [var suggestion: RCSService.Business.Suggestion](./suggestionresponse/suggestion.md)
  Suggestion for which to send the response.
- [RCSService.Business.Suggestion](./business/suggestion.md)
  Enumeration representing a suggestion from a business.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Responding to business suggestions
- [func sendSuggestionResponse(RCSService.SuggestionResponse) async throws](./sendsuggestionresponse%28_%29.md)
  Sends a response for a business suggestion.
- [func sendDeviceSpecifics(to: RCSHandle.URI, using: CellularServiceID, messageID: RCSMessageID) async throws](./senddevicespecifics%28to,using,messageid%29.md)
  Sends device specifics in response to a suggested action to send device specifics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/suggestionresponse)*