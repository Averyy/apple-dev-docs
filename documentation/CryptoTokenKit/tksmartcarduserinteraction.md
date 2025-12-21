# TKSmartCardUserInteraction

**Framework**: CryptoTokenKit  
**Kind**: class

The base class for encapsulating user interaction with a Smart Card reader.

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
class TKSmartCardUserInteraction
```

#### Overview

There are two types of user interactions: those for secure PIN change and those for secure PIN validation. These interactions are instances of the [`TKSmartCardUserInteractionForSecurePINChange`](tksmartcarduserinteractionforsecurepinchange.md), or [`TKSmartCardUserInteractionForSecurePINVerification`](tksmartcarduserinteractionforsecurepinverification.md) subclasses of [`TKSmartCardUserInteractionForPINOperation`](tksmartcarduserinteractionforpinoperation.md), respectively. [`TKSmartCardUserInteractionForPINOperation`](tksmartcarduserinteractionforpinoperation.md) is a subclass of `TKSmartCardUserInteraction`.

You interact with instances of one of the subclasses of [`TKSmartCardUserInteractionForPINOperation`](tksmartcarduserinteractionforpinoperation.md)when calling the [`userInteractionForSecurePINChange(_:apdu:currentPINByteOffset:newPINByteOffset:)`](tksmartcard/userinteractionforsecurepinchange(_:apdu:currentpinbyteoffset:newpinbyteoffset:).md) and [`userInteractionForSecurePINVerification(_:apdu:pinByteOffset:)`](tksmartcard/userinteractionforsecurepinverification(_:apdu:pinbyteoffset:).md) methods on an [`TKSmartCard`](tksmartcard.md) object.

## Topics

### Handling User Interaction Events
- [var delegate: (any TKSmartCardUserInteractionDelegate)?](tksmartcarduserinteraction/delegate.md)
  The delegate for observing events that occur during the user interaction.
- [protocol TKSmartCardUserInteractionDelegate](tksmartcarduserinteractiondelegate.md)
  The interface implemented by a Smart Card user interaction delegate to handle user interaction events.
### Configuring Timeout
- [var initialTimeout: TimeInterval](tksmartcarduserinteraction/initialtimeout.md)
  The timeout, in seconds, for initial interaction. If set to `0`, the reader-defined default timeout is used. `0` by default.
- [var interactionTimeout: TimeInterval](tksmartcarduserinteraction/interactiontimeout.md)
  The timeout, in seconds, after the first key stroke. If set to `0`, the reader-defined default timeout is used. `0` by default.
### Starting and Stopping
- [func run(reply: (Bool, (any Error)?) -> Void)](tksmartcarduserinteraction/run(reply:).md)
  Runs the user interaction and asynchronously receives a reply.
- [func cancel() -> Bool](tksmartcarduserinteraction/cancel.md)
  Attempts to cancel an interaction started by calling [`run(reply:)`](tksmartcarduserinteraction/run(reply:).md). For certain interactions, cancellation may not be available.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [TKSmartCardUserInteractionForPINOperation](tksmartcarduserinteractionforpinoperation.md)
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
- [class TKSmartCardUserInteractionForPINOperation](tksmartcarduserinteractionforpinoperation.md)
  A representation of user interaction for secure PIN operations on a Smart Card reader.
- [class TKSmartCardUserInteractionForSecurePINChange](tksmartcarduserinteractionforsecurepinchange.md)
  A representation of the user interaction for secure PIN change operations on a Smart Card reader.
- [class TKSmartCardUserInteractionForSecurePINVerification](tksmartcarduserinteractionforsecurepinverification.md)
  A representation of the user interaction for secure PIN change verification on a Smart Card reader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcarduserinteraction)*