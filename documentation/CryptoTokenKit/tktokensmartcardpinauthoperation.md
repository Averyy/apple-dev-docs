# TKTokenSmartCardPINAuthOperation

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

A Smart Card PIN authentication operation.

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
class TKTokenSmartCardPINAuthOperation
```

```objc
@interface TKTokenSmartCardPINAuthOperation : TKTokenAuthOperation
```

## Topics

### Configuring the Operation
- [var pinFormat: TKSmartCardPINFormat](./tktokensmartcardpinauthoperation/pinformat.md)
  The PIN format.
- [var apduTemplate: Data?](./tktokensmartcardpinauthoperation/apdutemplate.md)
  The template into which the PIN is filled in. `nil` by default.
- [var pinByteOffset: Int](./tktokensmartcardpinauthoperation/pinbyteoffset.md)
  The offset, in bytes, within the APDU template to mark the location for filling in the PIN.
- [var smartCard: TKSmartCard?](./tktokensmartcardpinauthoperation/smartcard.md)
  A Smart Card to which the formatted APDU is sent in order to authenticate.
### Accessing the PIN
- [var pin: String?](./tktokensmartcardpinauthoperation/pin.md)
  The PIN value resulting from performing the operation.

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
- [class TKTokenPasswordAuthOperation](./tktokenpasswordauthoperation.md)
  A password-based authentication operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation)*