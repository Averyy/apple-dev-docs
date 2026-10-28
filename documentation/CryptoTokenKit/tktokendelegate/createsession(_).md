# createSession(_:)

**Framework**: CryptoTokenKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the delegate to create a session for the specified token.

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
func createSession(_ token: TKToken) throws -> TKTokenSession
```

```objc
- (TKTokenSession *) token:(TKToken *) token createSessionWithError:(NSError **) error;
```

## Return Value

A new token session, or `nil` if an error occurred.

## Discussion

All operations for a token are performed within a session representing an authentication context. This delegate method is called whenever new authentication context is needed. For example, a client may want to perform a token operation using a keychain object that has an associated `LAContext`.

## Parameters

- `token`: The token.

## See Also

### Delegate Methods
- [func token(TKToken, terminateSession: TKTokenSession)](./token%28_,terminatesession%29.md)
  Tells the delegate to terminate the specified token session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokendelegate/createsession(_:))*