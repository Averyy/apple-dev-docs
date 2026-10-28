# TKTokenAuthOperation

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface TKTokenAuthOperation : NSObject
```

## Overview

The CryptoTokenKit framework provides the following concrete subclasses: [`TKTokenPasswordAuthOperation`](./tktokenpasswordauthoperation.md), for password-based authentication, and [`TKTokenSmartCardPINAuthOperation`](./tktokensmartcardpinauthoperation.md) for Smart Card PIN-based authentication.

## Topics

### Finishing the Operation
- [func finish() throws](./tktokenauthoperation/finish%28%29.md)
  Finishes the authentication operation.
### Initializers
- [init?(coder: NSCoder)](./tktokenauthoperation/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [TKTokenPasswordAuthOperation](./tktokenpasswordauthoperation.md)
- [TKTokenSmartCardPINAuthOperation](./tktokensmartcardpinauthoperation.md)
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
- [class TKTokenPasswordAuthOperation](./tktokenpasswordauthoperation.md)
  A password-based authentication operation.
- [class TKTokenSmartCardPINAuthOperation](./tktokensmartcardpinauthoperation.md)
  A Smart Card PIN authentication operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokenauthoperation)*