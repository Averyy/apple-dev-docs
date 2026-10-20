# TKSmartCardSlot.State

**Framework**: CryptoTokenKit  
**Kind**: enum  
**Role**: Enumeration

All smart card slot states.

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
enum State
```

```c
enum TKSmartCardSlotState : NSInteger;
```

## Topics

### Constants
- [TKSmartCardSlot.State.missing](./state-swift.enum/missing.md)
- [TKSmartCardSlot.State.empty](./state-swift.enum/empty.md)
- [TKSmartCardSlot.State.probing](./state-swift.enum/probing.md)
- [TKSmartCardSlot.State.muteCard](./state-swift.enum/mutecard.md)
- [TKSmartCardSlot.State.validCard](./state-swift.enum/validcard.md)
### Initializers
- [init?(rawValue: Int)](./state-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the Slot State
- [var state: TKSmartCardSlot.State](./state-swift.property.md)
  The current state of the Smart Card reader slot.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/state-swift.enum)*