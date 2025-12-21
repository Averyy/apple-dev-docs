# TKSmartCard

**Framework**: CryptoTokenKit  
**Kind**: class

A representation of a smart card.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class TKSmartCard
```

#### Overview

This class provides an interface for managing sessions with a smart card, transmitting requests, and facilitating user interaction.

You can create a [`TKSmartCard`](tksmartcard.md) object when a smart card is inserted into a slot, by calling the [`makeSmartCard()`](tksmartcardslot/makesmartcard().md) method on the corresponding [`TKSmartCardSlot`](tksmartcardslot.md) object. To start communicating with the smart card, call the [`beginSession(reply:)`](tksmartcard/beginsession(reply:).md) method on the [`TKSmartCard`](tksmartcard.md) object. Once an exclusive session has been established, you transmit data using the [`transmit(_:reply:)`](tksmartcard/transmit(_:reply:).md) method. After you’ve finished communicating with a smart card, you call the [`endSession()`](tksmartcard/endsession().md) method.

If the smart card is physically removed from its slot, the session object becomes invalid, and any further calls to [`transmit(_:reply:)`](tksmartcard/transmit(_:reply:).md) will return an error. You can use Key-Value Observing on the [`isValid`](tksmartcard/isvalid.md) property to be notified when a smart card is invalidated, due to being removed from the slot or another reason.

## Topics

### Configuring the Smart Card
- [var slot: TKSmartCardSlot](tksmartcard/slot.md)
  The slot in which the Smart Card is inserted.
- [var isValid: Bool](tksmartcard/isvalid.md)
  Whether the Smart Card is valid and accessible from its slot.
- [var isSensitive: Bool](tksmartcard/issensitive.md)
  Whether sessions established for the Smart Card should be considered sensitive. [`false`](https://developer.apple.com/documentation/Swift/false) by default.
- [var context: Any?](tksmartcard/context.md)
  User-specified information. This property is automatically set to `nil` if the Smart Card is removed or another `TKSmartCard` object begins a session.
### Setting the Communication Protocol
- [var allowedProtocols: TKSmartCardProtocol](tksmartcard/allowedprotocols.md)
  The protocols allowed for communication with the Smart Card. [`any`](tksmartcardprotocol/any.md) by default.
- [var currentProtocol: TKSmartCardProtocol](tksmartcard/currentprotocol.md)
  The protocol used for communication with the Smart Card. Returns [`TKSmartCardProtocolNone`](tksmartcardprotocol/tksmartcardprotocolnone.md) if no session is currently established.
- [struct TKSmartCardProtocol](tksmartcardprotocol.md)
  Smart Card transmission protocols.
### Communicating with the Smart Card
- [func beginSession(reply: (Bool, (any Error)?) -> Void)](tksmartcard/beginsession(reply:).md)
  Begins a session with the Smart Card.
- [func transmit(Data, reply: (Data?, (any Error)?) -> Void)](tksmartcard/transmit(_:reply:).md)
  Transmits data in Application Protocol Data Unit (APDU) format to the Smart Card.
- [func endSession()](tksmartcard/endsession.md)
  Completes any pending transmissions and ends the session to the Smart Card.
### Managing User Interaction
- [func userInteractionForSecurePINVerification(TKSmartCardPINFormat, apdu: Data, pinByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINVerification?](tksmartcard/userinteractionforsecurepinverification(_:apdu:pinbyteoffset:).md)
  Creates and returns a new user interaction object for secure PIN verification using the Smart Card reader facilities.
- [func userInteractionForSecurePINChange(TKSmartCardPINFormat, apdu: Data, currentPINByteOffset: Int, newPINByteOffset: Int) -> TKSmartCardUserInteractionForSecurePINChange?](tksmartcard/userinteractionforsecurepinchange(_:apdu:currentpinbyteoffset:newpinbyteoffset:).md)
  Creates a new user interaction object for secure PIN change using the smart card reader facilities (typically a HW keypad).
- [class TKSmartCardPINFormat](tksmartcardpinformat.md)
  The formatting properties for a PIN, such as character encoding and length constraints.
- [class TKSmartCardUserInteraction](tksmartcarduserinteraction.md)
  The base class for encapsulating user interaction with a Smart Card reader.
- [class TKSmartCardUserInteractionForPINOperation](tksmartcarduserinteractionforpinoperation.md)
  A representation of user interaction for secure PIN operations on a Smart Card reader.
- [class TKSmartCardUserInteractionForSecurePINChange](tksmartcarduserinteractionforsecurepinchange.md)
  A representation of the user interaction for secure PIN change operations on a Smart Card reader.
- [class TKSmartCardUserInteractionForSecurePINVerification](tksmartcarduserinteractionforsecurepinverification.md)
  A representation of the user interaction for secure PIN change verification on a Smart Card reader.
### Configuring APDU Behavior
- [var cla: UInt8](tksmartcard/cla.md)
  The CLA byte used for APDU transmission. `0x00` by default.
- [var useExtendedLength: Bool](tksmartcard/useextendedlength.md)
  Whether to use extended length APDU.
- [var useCommandChaining: Bool](tksmartcard/usecommandchaining.md)
  Whether to use command chaining of APDU with a data field longer than 255 bytes.
### Transmitting Data
- [func send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data?, le: Int?, reply: (Data?, UInt16, (any Error)?) -> Void)](tksmartcard/send(ins:p1:p2:data:le:reply:).md)
  Asynchronously transmits an APDU command to the card, returning the response in a completion handler.
- [func send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data?, le: Int?) throws -> (sw: UInt16, response: Data)](tksmartcard/send(ins:p1:p2:data:le:).md)
  Synchronously transmits an APDU command to the card and returns the response.
- [func withSession<T>(() throws -> T) throws -> T](tksmartcard/withsession(_:).md)
  Synchronously begins a session, executes the given closure, and ends the session.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Using Cryptographic Assets Stored on a Smart Card](using-cryptographic-assets-stored-on-a-smart-card.md)
  Access certificates, keys, and identities stored on a smart card as if they were part of the keychain.
- [class TKSmartCardSlotManager](tksmartcardslotmanager.md)
  An interface to all available smart card reader slots.
- [class TKSmartCardSlot](tksmartcardslot.md)
  A single smart card reader slot in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard)*