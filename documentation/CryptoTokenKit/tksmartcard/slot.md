# slot

**Framework**: CryptoTokenKit  
**Kind**: property

The slot in which the Smart Card is inserted.

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
var slot: TKSmartCardSlot { get }
```

## See Also

- [var isValid: Bool](tksmartcard/isvalid.md)
  Whether the Smart Card is valid and accessible from its slot.
- [var isSensitive: Bool](tksmartcard/issensitive.md)
  Whether sessions established for the Smart Card should be considered sensitive. [`false`](https://developer.apple.com/documentation/swift/false) by default.
- [var context: Any?](tksmartcard/context.md)
  User-specified information. This property is automatically set to `nil` if the Smart Card is removed or another `TKSmartCard` object begins a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/slot)*