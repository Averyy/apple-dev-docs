# slotNames

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

A list of identifiers for all the Smart Card reader slots available to the system.

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
var slotNames: [String] { get }
```

```objc
@property (readonly) NSArray<NSString *> * slotNames;
```

#### Discussion

Use Key-Value Observing on this property to be notified for changes to available Smart Card reader slots. For more information, see [Key-Value Observing Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

### Accessing Smart Card Slots
- [func getSlot(withName: String, reply: (TKSmartCardSlot?) -> Void)](./getslot%28withname,reply%29.md)
  Asynchronously calls a block with a Smart Card reader slot for a specified name.
- [func slotNamed(String) -> TKSmartCardSlot?](./slotnamed%28_%29.md)
  Returns the Smart Card slot with a given name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardslotmanager/slotnames)*