# respond(response:)

**Framework**: Core NFC  
**Kind**: method

Respond to the session after receiving and processing an APDU.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
final func respond(response: Data) async throws
```

#### Discussion

Your client must respond to each APDU it receives. Failing to respond throws an error. If your client disposes an APDU object without responding, the card emulation ends.

> ⚠️ **Warning**:  Only respond to a given APDU once. Calling this method more than once raises [`fatalError(_:file:line:)`](https://developer.apple.com/documentation/Swift/fatalError(_:file:line:)). The exception to this is if the call throws [`CardSession.Error.transmissionError`](cardsession/error/transmissionerror.md). In this case, you can retry the response by calling [`respond(response:)`](cardsession/apdu/respond(response:).md) again.

## Parameters

- `response`: The APDU data to send as a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/cardsession/apdu/respond(response:))*