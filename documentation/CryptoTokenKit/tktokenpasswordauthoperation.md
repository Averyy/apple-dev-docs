# TKTokenPasswordAuthOperation

**Framework**: CryptoTokenKit  
**Kind**: class

A password-based authentication operation.

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
class TKTokenPasswordAuthOperation
```

## Topics

### Managing the Password
- [var password: String?](tktokenpasswordauthoperation/password.md)
  The password to be filled in when the `finishWithError:` is called.

## Relationships

### Inherits From
- [TKTokenAuthOperation](tktokenauthoperation.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [func tokenSession(TKTokenSession, beginAuthFor: TKTokenOperation, constraint: Any) throws -> TKTokenAuthOperation](tktokensessiondelegate/tokensession(_:beginauthfor:constraint:).md)
  Tells the delegate that authentication has begun for the specified operation and constraint.
- [typealias TKTokenOperationConstraint](tktokenoperationconstraint.md)
  A token’s authentication constraint for a specific operation.
- [class TKTokenAuthOperation](tktokenauthoperation.md)
  An authentication operation for a cryptographic token.
- [class TKTokenSmartCardPINAuthOperation](tktokensmartcardpinauthoperation.md)
  A Smart Card PIN authentication operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenpasswordauthoperation)*