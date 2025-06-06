# TKSmartCardUserInteractionForPINOperation

**Framework**: CryptoTokenKit  
**Kind**: class

A representation of user interaction for secure PIN operations on a Smart Card reader.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
class TKSmartCardUserInteractionForPINOperation
```

#### Overview

There are two types of user interactions: those for secure PIN change and those for secure PIN validation. These interactions are instances of the [`TKSmartCardUserInteractionForSecurePINChange`](tksmartcarduserinteractionforsecurepinchange.md), or [`TKSmartCardUserInteractionForSecurePINVerification`](tksmartcarduserinteractionforsecurepinverification.md) subclasses of [`TKSmartCardUserInteractionForPINOperation`](tksmartcarduserinteractionforpinoperation.md), respectively.

You interact with instances of one of the subclasses of [`TKSmartCardUserInteractionForPINOperation`](tksmartcarduserinteractionforpinoperation.md) when calling the [`userInteractionForSecurePINChange(_:apdu:currentPINByteOffset:newPINByteOffset:)`](tksmartcard/userinteractionforsecurepinchange(_:apdu:currentpinbyteoffset:newpinbyteoffset:).md) and [`userInteractionForSecurePINVerification(_:apdu:pinByteOffset:)`](tksmartcard/userinteractionforsecurepinverification(_:apdu:pinbyteoffset:).md) methods on an [`TKSmartCard`](tksmartcard.md) object.

The result of a user interaction is available once the interaction has completed.

## Topics

### Managing Pin Completion
- [var pinCompletion: TKSmartCardUserInteractionForPINOperation.Completion](tksmartcarduserinteractionforpinoperation/pincompletion.md)
  The conditions under which PIN entry should be considered complete.
- [TKSmartCardUserInteractionForPINOperation.Completion](tksmartcarduserinteractionforpinoperation/completion.md)
### Configuring Messages
- [var pinMessageIndices: [NSNumber]?](tksmartcarduserinteractionforpinoperation/pinmessageindices.md)
  A list of message indices referring to a predefined message table, used to specify the type and number of messages displayed during the PIN operation. `nil` by default.
- [var locale: Locale!](tksmartcarduserinteractionforpinoperation/locale.md)
  The locale for the displayed messages. If `nil`, the user’s current locale is used. By default, this value is the current locale of the system.
### Accessing Response Data
- [var resultSW: UInt16](tksmartcarduserinteractionforpinoperation/resultsw.md)
  The SW1-SW2 status bytes.
- [var resultData: Data?](tksmartcarduserinteractionforpinoperation/resultdata.md)
  The returned data without SW1-SW2 bytes, if any.

## Relationships

### Inherits From
- [TKSmartCardUserInteraction](tksmartcarduserinteraction.md)
### Inherited By
- [TKSmartCardUserInteractionForSecurePINChange](tksmartcarduserinteractionforsecurepinchange.md)
- [TKSmartCardUserInteractionForSecurePINVerification](tksmartcarduserinteractionforsecurepinverification.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func userInteractionForSecurePINVerification(TKSmartCardPINFormat, apdu: Data, pinByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINVerification?](tksmartcard/userinteractionforsecurepinverification(_:apdu:pinbyteoffset:).md)
  Creates and returns a new user interaction object for secure PIN verification using the Smart Card reader facilities.
- [func userInteractionForSecurePINChange(TKSmartCardPINFormat, apdu: Data, currentPINByteOffset: Int, newPINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINChange?](tksmartcard/userinteractionforsecurepinchange(_:apdu:currentpinbyteoffset:newpinbyteoffset:).md)
  Creates a new user interaction object for secure PIN change using the smart card reader facilities (typically a HW keypad).
- [class TKSmartCardPINFormat](tksmartcardpinformat.md)
  The formatting properties for a PIN, such as character encoding and length constraints.
- [class TKSmartCardUserInteraction](tksmartcarduserinteraction.md)
  The base class for encapsulating user interaction with a Smart Card reader.
- [class TKSmartCardUserInteractionForSecurePINChange](tksmartcarduserinteractionforsecurepinchange.md)
  A representation of the user interaction for secure PIN change operations on a Smart Card reader.
- [class TKSmartCardUserInteractionForSecurePINVerification](tksmartcarduserinteractionforsecurepinverification.md)
  A representation of the user interaction for secure PIN change verification on a Smart Card reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteractionforpinoperation)*