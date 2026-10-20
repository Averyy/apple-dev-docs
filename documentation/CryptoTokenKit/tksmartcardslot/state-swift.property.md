# state

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The current state of the Smart Card reader slot.

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
var state: TKSmartCardSlot.State { get }
```

```objc
@property (readonly) TKSmartCardSlotState state;
```

#### Discussion

Use Key-Value-Observing to be notified for changes to the state. For more information, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

### Getting the Slot State
- [TKSmartCardSlot.State](./state-swift.enum.md)
  All smart card slot states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslot/state-swift.property)*