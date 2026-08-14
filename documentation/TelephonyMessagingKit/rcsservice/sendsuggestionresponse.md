# sendSuggestionResponse(_:)

**Framework**: TelephonyMessagingKit  
**Kind**: method

Sends a response for a business suggestion.

**Availability**:
- iOS 26.0+

## Declaration

```swift
final func sendSuggestionResponse(_ response: RCSService.SuggestionResponse) async throws
```

## Parameters

- `response`: `SuggestionResponse` containing the response parameters.

## See Also

- [RCSService.SuggestionResponse](rcsservice/suggestionresponse.md)
  Structure representing a response to a business suggestion.
- [func sendDeviceSpecifics(to: RCSHandle.URI, using: CellularServiceID, messageID: RCSMessageID) async throws](rcsservice/senddevicespecifics(to:using:messageid:).md)
  Sends device specifics in response to a suggested action to send device specifics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/sendsuggestionresponse(_:))*