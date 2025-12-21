# TKSmartCardSlotNFCSession

**Framework**: CryptoTokenKit  
**Kind**: class

NFC session that’s related to NFC smart card slot which was created.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
class TKSmartCardSlotNFCSession
```

#### Overview

Lifetime of this session object is tied to the NFC smart card slot lifetime and once the NFC slot disappears (eg. after a user cancellation, calling end session, or an NFC timeout) the functions will start to fail and return `TKErrorCodeObjectNotFound` error.

## Topics

### Instance Properties
- [var slotName: String?](tksmartcardslotnfcsession/slotname.md)
  Smart card slot name of the NFC slot that was created together with this session.
### Instance Methods
- [func end()](tksmartcardslotnfcsession/end.md)
  Ends the NFC slot session and dismisses the system-presented NFC UI (if present).
- [func update(message: String) throws](tksmartcardslotnfcsession/update(message:).md)
  Updates the message of the system-presented NFC UI.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotnfcsession)*