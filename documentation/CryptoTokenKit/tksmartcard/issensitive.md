# isSensitive

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

Whether sessions established for the Smart Card should be considered sensitive. [`false`](../../Swift/false.md) by default.

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
var isSensitive: Bool { get set }
```

```objc
@property BOOL sensitive;
```

## Discussion

When this property is set to [`true`](../../Swift/true.md), any sessions established for the receiver will begin and end by sending a reset command to the Smart Card. This is recommended anytime potentially sensitive information is transferred.

## See Also

### Configuring the Smart Card
- [var slot: TKSmartCardSlot](./slot.md)
  The slot in which the Smart Card is inserted.
- [var isValid: Bool](./isvalid.md)
  Whether the Smart Card is valid and accessible from its slot.
- [var context: Any?](./context.md)
  User-specified information. This property is automatically set to `nil` if the Smart Card is removed or another `TKSmartCard` object begins a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/issensitive)*