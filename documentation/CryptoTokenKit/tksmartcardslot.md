# TKSmartCardSlot

**Framework**: CryptoTokenKit  
**Kind**: class

A single smart card reader slot in the system.

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
class TKSmartCardSlot
```

#### Overview

Use the [`TKSmartCardSlotManager`](tksmartcardslotmanager.md) class to manage all the smart card reader slots available to the system. You can retrieve the names of available smart card reader slots for a system using the [`slotNames`](tksmartcardslotmanager/slotnames.md) property of a manager object, and access instances of [`TKSmartCardSlot`](tksmartcardslot.md) using the  [`getSlot(withName:reply:)`](tksmartcardslotmanager/getslot(withname:reply:).md) method.

## Topics

### Instantiating Smart Cards
- [func makeSmartCard() -> TKSmartCard?](tksmartcardslot/makesmartcard.md)
  Creates a new [`TKSmartCard`](tksmartcard.md) object representing the currently inserted Smart Card.
### Getting the Slot State
- [var state: TKSmartCardSlot.State](tksmartcardslot/state-swift.property.md)
  The current state of the Smart Card reader slot.
- [TKSmartCardSlot.State](tksmartcardslot/state-swift.enum.md)
  All smart card slot states.
### Getting the Slot Configuration
- [var name: String](tksmartcardslot/name.md)
  The name of the Smart Card reader slot.
- [var maxInputLength: Int](tksmartcardslot/maxinputlength.md)
  The maximum length of input APDU (Application Protocol Data Unit) that the Smart Card reader slot is able to transfer to the Smart Card.
- [var maxOutputLength: Int](tksmartcardslot/maxoutputlength.md)
  The maximum length of output APDU (Application Protocol Data Unit) that the Smart Card reader slot is able to transfer from the Smart Card.
### Reading the Answer to Reset
- [var atr: TKSmartCardATR?](tksmartcardslot/atr.md)
  The ATR (Answer to Reset) of the inserted Smart Card, or `nil` if no Smart Card is inserted or the inserted Smart Card is mute.
- [class TKSmartCardATR](tksmartcardatr.md)
  A parsed ATR (Answer To Reset) message from a Smart Card.

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
- [class TKSmartCard](tksmartcard.md)
  A representation of a smart card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot)*