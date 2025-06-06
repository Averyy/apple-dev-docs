# slotNames

**Framework**: CryptoTokenKit  
**Kind**: property

A list of identifiers for all the Smart Card reader slots available to the system.

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
var slotNames: [String] { get }
```

#### Discussion

Use Key-Value Observing on this property to be notified for changes to available Smart Card reader slots. For more information, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

- [func getSlot(withName: String, reply: (TKSmartCardSlot?) -> Void)](tksmartcardslotmanager/getslot(withname:reply:).md)
  Asynchronously calls a block with a Smart Card reader slot for a specified name.
- [func slotNamed(String) -> TKSmartCardSlot?](tksmartcardslotmanager/slotnamed(_:).md)
  Returns the Smart Card slot with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/slotnames)*