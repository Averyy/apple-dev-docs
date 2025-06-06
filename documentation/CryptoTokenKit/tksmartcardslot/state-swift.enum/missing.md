# TKSmartCardSlot.State.missing

**Framework**: CryptoTokenKit  
**Kind**: case

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
case missing
```

#### Discussion

The Smart Card reader slot is no longer known to the system.

> ❗ **Important**:  This is the terminal state of a `TKSmartCardSlotThis` instance; once it has reached this state, the Smart Card reader slot cannot be reinitialized.

 This is the terminal state of a `TKSmartCardSlotThis` instance; once it has reached this state, the Smart Card reader slot cannot be reinitialized.

## See Also

- [TKSmartCardSlot.State.empty](tksmartcardslot/state-swift.enum/empty.md)
- [TKSmartCardSlot.State.probing](tksmartcardslot/state-swift.enum/probing.md)
- [TKSmartCardSlot.State.muteCard](tksmartcardslot/state-swift.enum/mutecard.md)
- [TKSmartCardSlot.State.validCard](tksmartcardslot/state-swift.enum/validcard.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/state-swift.enum/missing)*