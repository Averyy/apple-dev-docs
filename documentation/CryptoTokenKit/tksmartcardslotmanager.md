# TKSmartCardSlotManager

**Framework**: CryptoTokenKit  
**Kind**: class

An interface to all available smart card reader slots.

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
class TKSmartCardSlotManager
```

#### Overview

Get a list of all known smart card reader slots in the system using the [`slotNames`](tksmartcardslotmanager/slotnames.md) property, and access individual slots by name using the [`getSlot(withName:reply:)`](tksmartcardslotmanager/getslot(withname:reply:).md) method.

> ❗ **Important**:  The [`com.apple.security.smartcard`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.smartcard) entitlement is required in order to use `TKSmartCardSlotManager`.

## Topics

### Creating a Card Slot Manager
- [class var `default`: TKSmartCardSlotManager?](tksmartcardslotmanager/default.md)
  The shared singleton Smart Card reader slot manager.
### Accessing Smart Card Slots
- [var slotNames: [String]](tksmartcardslotmanager/slotnames.md)
  A list of identifiers for all the Smart Card reader slots available to the system.
- [func getSlot(withName: String, reply: (TKSmartCardSlot?) -> Void)](tksmartcardslotmanager/getslot(withname:reply:).md)
  Asynchronously calls a block with a Smart Card reader slot for a specified name.
- [func slotNamed(String) -> TKSmartCardSlot?](tksmartcardslotmanager/slotnamed(_:).md)
  Returns the Smart Card slot with a given name.
### Instance Methods
- [func createNFCSlot(message: String?, completion: (TKSmartCardSlotNFCSession?, (any Error)?) -> Void)](tksmartcardslotmanager/createnfcslot(message:completion:).md)
  Creates an NFC smart card slot using the device’s hardware and presents a system UI.
- [func isNFCSupported() -> Bool](tksmartcardslotmanager/isnfcsupported.md)
  Determines whether NFC (Near Field Communication) is supported on this device.

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
- [class TKSmartCardSlot](tksmartcardslot.md)
  A single smart card reader slot in the system.
- [class TKSmartCard](tksmartcard.md)
  A representation of a smart card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager)*