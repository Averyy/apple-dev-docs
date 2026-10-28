# TKSmartCard

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface TKSmartCard : NSObject
```

## Overview

This class provides an interface for managing sessions with a smart card, transmitting requests, and facilitating user interaction.

You can create a [`TKSmartCard`](./tksmartcard.md) object when a smart card is inserted into a slot, by calling the [`makeSmartCard()`](./tksmartcardslot/makesmartcard%28%29.md) method on the corresponding [`TKSmartCardSlot`](./tksmartcardslot.md) object. To start communicating with the smart card, call the [`beginSession(reply:)`](./tksmartcard/beginsession%28reply%29.md) method on the [`TKSmartCard`](./tksmartcard.md) object. Once an exclusive session has been established, you transmit data using the [`transmit(_:reply:)`](./tksmartcard/transmit%28_,reply%29.md) method. After you’ve finished communicating with a smart card, you call the [`endSession()`](./tksmartcard/endsession%28%29.md) method.

If the smart card is physically removed from its slot, the session object becomes invalid, and any further calls to [`transmit(_:reply:)`](./tksmartcard/transmit%28_,reply%29.md) will return an error. You can use Key-Value Observing on the [`isValid`](./tksmartcard/isvalid.md) property to be notified when a smart card is invalidated, due to being removed from the slot or another reason.

## Topics

### Configuring the Smart Card
- [var slot: TKSmartCardSlot](./tksmartcard/slot.md)
  The slot in which the Smart Card is inserted.
- [var isValid: Bool](./tksmartcard/isvalid.md)
  Whether the Smart Card is valid and accessible from its slot.
- [var isSensitive: Bool](./tksmartcard/issensitive.md)
  Whether sessions established for the Smart Card should be considered sensitive. [`false`](../Swift/false.md) by default.
- [var context: Any?](./tksmartcard/context.md)
  User-specified information. This property is automatically set to `nil` if the Smart Card is removed or another `TKSmartCard` object begins a session.
### Setting the Communication Protocol
- [var allowedProtocols: TKSmartCardProtocol](./tksmartcard/allowedprotocols.md)
  The protocols allowed for communication with the Smart Card. [`any`](./tksmartcardprotocol/any.md) by default.
- [var currentProtocol: TKSmartCardProtocol](./tksmartcard/currentprotocol.md)
  The protocol used for communication with the Smart Card. Returns [`TKSmartCardProtocolNone`](./tksmartcardprotocol/tksmartcardprotocolnone.md) if no session is currently established.
- [struct TKSmartCardProtocol](./tksmartcardprotocol.md)
  Smart Card transmission protocols.
### Communicating with the Smart Card
- [func beginSession(reply: (Bool, (any Error)?) -> Void)](./tksmartcard/beginsession%28reply%29.md)
  Begins a session with the Smart Card.
- [func transmit(Data, reply: (Data?, (any Error)?) -> Void)](./tksmartcard/transmit%28_,reply%29.md)
  Transmits data in Application Protocol Data Unit (APDU) format to the Smart Card.
- [func endSession()](./tksmartcard/endsession%28%29.md)
  Completes any pending transmissions and ends the session to the Smart Card.
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
- [class TKSmartCardUserInteractionForSecurePINChange](./tksmartcarduserinteractionforsecurepinchange.md)
  A representation of the user interaction for secure PIN change operations on a Smart Card reader.
- [class TKSmartCardUserInteractionForSecurePINVerification](./tksmartcarduserinteractionforsecurepinverification.md)
  A representation of the user interaction for secure PIN change verification on a Smart Card reader.
### Configuring APDU Behavior
- [var cla: UInt8](./tksmartcard/cla.md)
  The CLA byte used for APDU transmission. `0x00` by default.
- [var useExtendedLength: Bool](./tksmartcard/useextendedlength.md)
  Whether to use extended length APDU.
- [var useCommandChaining: Bool](./tksmartcard/usecommandchaining.md)
  Whether to use command chaining of APDU with a data field longer than 255 bytes.
### Transmitting Data
- [func send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data?, le: Int?, reply: (Data?, UInt16, (any Error)?) -> Void)](./tksmartcard/send%28ins,p1,p2,data,le,reply%29.md)
  Asynchronously transmits an APDU command to the card, returning the response in a completion handler.
- [func withSession<T>(() throws -> T) throws -> T](./tksmartcard/withsession%28_%29.md)
  Synchronously begins a session, executes the given closure, and ends the session.
- [- sendIns:p1:p2:data:le:reply:](./tksmartcard/sendins_p1_p2_data_le_reply_.md)
  Asynchronously transmits an APDU command to the card, returning the response in a completion handler.
- [- sendIns:p1:p2:data:le:sw:error:](./tksmartcard/sendins_p1_p2_data_le_sw_error_.md)
  Synchronously transmits an APDU command to the card and returns the response.
- [- inSessionWithError:executeBlock:](./tksmartcard/insessionwitherror_executeblock_.md)
  Synchronously begins a session, executes the given block, and ends the session.
### Instance Methods
- [func send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data?, le: Int?) throws -> (sw: UInt16, response: Data)](./tksmartcard/send%28ins,p1,p2,data,le%29-1kbga.md)
  Synchronously sends an APDU command to the smart card.
- [func send(ins: UInt8, p1: UInt8, p2: UInt8, data: Data?, le: Int?) async throws -> (sw: UInt16, response: Data)](./tksmartcard/send%28ins,p1,p2,data,le%29-6dore.md)
  Asynchronously sends an APDU command to the smart card.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Smart Cards
- [Using Cryptographic Assets Stored on a Smart Card](./using-cryptographic-assets-stored-on-a-smart-card.md)
  Access certificates, keys, and identities stored on a smart card as if they were part of the keychain.
- [class TKSmartCardSlotManager](./tksmartcardslotmanager.md)
  An interface to all available smart card reader slots.
- [class TKSmartCardSlot](./tksmartcardslot.md)
  A single smart card reader slot in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard)*