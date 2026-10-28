# TKSmartCardUserInteractionForSecurePINChange

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

A representation of the user interaction for secure PIN change operations on a Smart Card reader.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class TKSmartCardUserInteractionForSecurePINChange
```

```objc
@interface TKSmartCardUserInteractionForSecurePINChange : TKSmartCardUserInteractionForPINOperation
```

## Overview

The result of a user interaction is available once the interaction has completed.

## Topics

### Configuring User Interaction
- [var pinConfirmation: TKSmartCardUserInteractionForSecurePINChange.Confirmation](./tksmartcarduserinteractionforsecurepinchange/pinconfirmation.md)
  The way PIN confirmation is requested. `TKSmartCardPINConfirmationNone` by default.
- [TKSmartCardUserInteractionForSecurePINChange.Confirmation](./tksmartcarduserinteractionforsecurepinchange/confirmation.md)

## Relationships

### Inherits From
- [TKSmartCardUserInteractionForPINOperation](./tksmartcarduserinteractionforpinoperation.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Managing User Interaction
- [func userInteractionForSecurePINVerification(TKSmartCardPINFormat, apdu: Data, pinByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINVerification?](./tksmartcard/userinteractionforsecurepinverification%28_,apdu,pinbyteoffset%29.md)
  Creates and returns a new user interaction object for secure PIN verification using the Smart Card reader facilities.
- [func userInteractionForSecurePINChange(TKSmartCardPINFormat, apdu: Data, currentPINByteOffset: Int, newPINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINChange?](./tksmartcard/userinteractionforsecurepinchange%28_,apdu,currentpinbyteoffset,newpinbyteoffset%29.md)
  Creates a new user interaction object for secure PIN change using the smart card reader facilities (typically a HW keypad).
- [class TKSmartCardPINFormat](./tksmartcardpinformat.md)
  The formatting properties for a PIN, such as character encoding and length constraints.
- [class TKSmartCardUserInteraction](./tksmartcarduserinteraction.md)
  The base class for encapsulating user interaction with a Smart Card reader.
- [class TKSmartCardUserInteractionForPINOperation](./tksmartcarduserinteractionforpinoperation.md)
  A representation of user interaction for secure PIN operations on a Smart Card reader.
- [class TKSmartCardUserInteractionForSecurePINVerification](./tksmartcarduserinteractionforsecurepinverification.md)
  A representation of the user interaction for secure PIN change verification on a Smart Card reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforsecurepinchange)*