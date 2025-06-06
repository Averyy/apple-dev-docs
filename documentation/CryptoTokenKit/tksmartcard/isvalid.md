# isValid

**Framework**: CryptoTokenKit  
**Kind**: property

Whether the Smart Card is valid and accessible from its slot.

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
var isValid: Bool { get }
```

#### Discussion

Use Key-Value-Observing to be notified for changes to accessibility, such as when a Smart Card is physically removed from its slot. For more information, see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## See Also

- [var slot: TKSmartCardSlot](tksmartcard/slot.md)
  The slot in which the Smart Card is inserted.
- [var isSensitive: Bool](tksmartcard/issensitive.md)
  Whether sessions established for the Smart Card should be considered sensitive. [`false`](https://developer.apple.com/documentation/swift/false) by default.
- [var context: Any?](tksmartcard/context.md)
  User-specified information. This property is automatically set to `nil` if the Smart Card is removed or another `TKSmartCard` object begins a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/isvalid)*