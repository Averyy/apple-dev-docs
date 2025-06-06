# TKTokenAuthOperation

**Framework**: CryptoTokenKit  
**Kind**: class

An authentication operation for a cryptographic token.

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
class TKTokenAuthOperation
```

#### Overview

The CryptoTokenKit framework provides the following concrete subclasses: [`TKTokenPasswordAuthOperation`](tktokenpasswordauthoperation.md), for password-based authentication, and [`TKTokenSmartCardPINAuthOperation`](tktokensmartcardpinauthoperation.md) for Smart Card PIN-based authentication.

## Topics

### Finishing the Operation
- [func finish() throws](tktokenauthoperation/finish.md)
  Finishes the authentication operation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [TKTokenPasswordAuthOperation](tktokenpasswordauthoperation.md)
- [TKTokenSmartCardPINAuthOperation](tktokensmartcardpinauthoperation.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func tokenSession(TKTokenSession, beginAuthFor: TKTokenOperation, constraint: Any) throws -> TKTokenAuthOperation](tktokensessiondelegate/tokensession(_:beginauthfor:constraint:).md)
  Tells the delegate that authentication has begun for the specified operation and constraint.
- [typealias TKTokenOperationConstraint](tktokenoperationconstraint.md)
  A token’s authentication constraint for a specific operation.
- [class TKTokenPasswordAuthOperation](tktokenpasswordauthoperation.md)
  A password-based authentication operation.
- [class TKTokenSmartCardPINAuthOperation](tktokensmartcardpinauthoperation.md)
  A Smart Card PIN authentication operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenauthoperation)*