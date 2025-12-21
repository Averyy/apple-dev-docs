# TKTokenOperationConstraint

**Framework**: CryptoTokenKit  
**Kind**: typealias

A token’s authentication constraint for a specific operation.

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
typealias TKTokenOperationConstraint = AnyObject
```

#### Discussion

This object persistently identifies a constraint for performing specific operation on specific object.

- [`true`](https://developer.apple.com/documentation/Swift/true), indicating that the operation is always allowed, without any authentication necessary.
- [`false`](https://developer.apple.com/documentation/Swift/false), indicating that the operation is never allowed; this value isn’t typically used.
- Any other property list compatible value defined by the implementation of the token extension. Any such constraint is required to stay constant for the entire lifetime of the token. For example, a Smart Card token extension may decide to use the string constant `"PIN"` to indicate that the operation is authenticated with valid PIN entry to the card.

## See Also

- [func tokenSession(TKTokenSession, beginAuthFor: TKTokenOperation, constraint: Any) throws -> TKTokenAuthOperation](tktokensessiondelegate/tokensession(_:beginauthfor:constraint:).md)
  Tells the delegate that authentication has begun for the specified operation and constraint.
- [class TKTokenAuthOperation](tktokenauthoperation.md)
  An authentication operation for a cryptographic token.
- [class TKTokenPasswordAuthOperation](tktokenpasswordauthoperation.md)
  A password-based authentication operation.
- [class TKTokenSmartCardPINAuthOperation](tktokensmartcardpinauthoperation.md)
  A Smart Card PIN authentication operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenoperationconstraint)*