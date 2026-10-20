# TKTokenPasswordAuthOperation

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface TKTokenPasswordAuthOperation : TKTokenAuthOperation
```

## Topics

### Managing the Password
- [var password: String?](./tktokenpasswordauthoperation/password.md)
  The password to be filled in when the `finishWithError:` is called.

## Relationships

### Inherits From
- [TKTokenAuthOperation](./tktokenauthoperation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Authenticating
- [func tokenSession(TKTokenSession, beginAuthFor: TKTokenOperation, constraint: Any) throws -> TKTokenAuthOperation](./tktokensessiondelegate/tokensession%28_,beginauthfor,constraint%29.md)
  Tells the delegate that authentication has begun for the specified operation and constraint.
- [typealias TKTokenOperationConstraint](./tktokenoperationconstraint.md)
  A token’s authentication constraint for a specific operation.
- [class TKTokenAuthOperation](./tktokenauthoperation.md)
  An authentication operation for a cryptographic token.
- [class TKTokenSmartCardPINAuthOperation](./tktokensmartcardpinauthoperation.md)
  A Smart Card PIN authentication operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenpasswordauthoperation)*