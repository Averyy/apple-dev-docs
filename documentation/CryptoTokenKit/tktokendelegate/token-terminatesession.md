# token(_:terminateSession:)

**Framework**: CryptoTokenKit  
**Kind**: method

Tells the delegate to terminate the specified token session.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
optional func token(_ token: TKToken, terminateSession session: TKTokenSession)
```

## Parameters

- `token`: The token.
- `session`: The token session to be terminated.

## See Also

- [func createSession(TKToken) throws -> TKTokenSession](tktokendelegate/createsession(_:).md)
  Tells the delegate to create a session for the specified token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendelegate/token(_:terminatesession:))*