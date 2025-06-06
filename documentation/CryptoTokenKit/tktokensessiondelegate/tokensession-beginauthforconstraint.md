# tokenSession(_:beginAuthFor:constraint:)

**Framework**: CryptoTokenKit  
**Kind**: method

Tells the delegate that authentication has begun for the specified operation and constraint.

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
optional func tokenSession(_ session: TKTokenSession, beginAuthFor operation: TKTokenOperation, constraint: Any) throws -> TKTokenAuthOperation
```

#### Return Value

The resulting context of the operation, or `nil` if an error occurred.

#### Discussion

If you return an instance of a subclass of [`TKTokenAuthOperation`](tktokenauthoperation.md) that is provided by the CryptoTokenKit framework, the system will first fill in the context-specific properties, such as the password, before calling the `finishWithError:` method on the context.

## Parameters

- `session`: The token session.
- `operation`: The kind of operation.
- `constraint`: The constraint to be satisfied.

## See Also

- [typealias TKTokenOperationConstraint](tktokenoperationconstraint.md)
  A token’s authentication constraint for a specific operation.
- [class TKTokenAuthOperation](tktokenauthoperation.md)
  An authentication operation for a cryptographic token.
- [class TKTokenPasswordAuthOperation](tktokenpasswordauthoperation.md)
  A password-based authentication operation.
- [class TKTokenSmartCardPINAuthOperation](tktokensmartcardpinauthoperation.md)
  A Smart Card PIN authentication operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokensessiondelegate/tokensession(_:beginauthfor:constraint:))*