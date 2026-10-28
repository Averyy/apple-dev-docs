# TKSmartCardSlotNFCSession

**Framework**: CryptoTokenKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface TKSmartCardSlotNFCSession : NSObject
```

## Overview

Lifetime of this session object is tied to the NFC smart card slot lifetime and once the NFC slot disappears (eg. after a user cancellation, calling end session, or an NFC timeout) the functions will start to fail and return `TKErrorCodeObjectNotFound` error.

## Topics

### Instance Properties
- [var slotName: String?](./tksmartcardslotnfcsession/slotname.md)
  Smart card slot name of the NFC slot that was created together with this session.
### Instance Methods
- [func end()](./tksmartcardslotnfcsession/end%28%29.md)
  Ends the NFC slot session and dismisses the system-presented NFC UI (if present).
- [func update(message: String) throws](./tksmartcardslotnfcsession/update%28message%29.md)
  Updates the message of the system-presented NFC UI.

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotnfcsession)*