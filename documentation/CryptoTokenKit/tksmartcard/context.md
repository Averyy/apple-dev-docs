# context

**Framework**: CryptoTokenKit  
**Kind**: property

User-specified information. This property is automatically set to `nil` if the Smart Card is removed or another `TKSmartCard` object begins a session.

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
var context: Any? { get set }
```

## See Also

- [var slot: TKSmartCardSlot](tksmartcard/slot.md)
  The slot in which the Smart Card is inserted.
- [var isValid: Bool](tksmartcard/isvalid.md)
  Whether the Smart Card is valid and accessible from its slot.
- [var isSensitive: Bool](tksmartcard/issensitive.md)
  Whether sessions established for the Smart Card should be considered sensitive. [`false`](https://developer.apple.com/documentation/Swift/false) by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/context)*