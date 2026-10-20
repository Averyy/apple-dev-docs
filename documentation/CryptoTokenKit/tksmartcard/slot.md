# slot

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The slot in which the Smart Card is inserted.

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
var slot: TKSmartCardSlot { get }
```

```objc
@property (nonatomic, readonly) TKSmartCardSlot * slot;
```

## See Also

### Configuring the Smart Card
- [var isValid: Bool](./isvalid.md)
  Whether the Smart Card is valid and accessible from its slot.
- [var isSensitive: Bool](./issensitive.md)
  Whether sessions established for the Smart Card should be considered sensitive. [`false`](../../Swift/false.md) by default.
- [var context: Any?](./context.md)
  User-specified information. This property is automatically set to `nil` if the Smart Card is removed or another `TKSmartCard` object begins a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/slot)*