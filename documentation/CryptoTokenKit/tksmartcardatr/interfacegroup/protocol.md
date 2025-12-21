# protocol

**Framework**: CryptoTokenKit  
**Kind**: property

The protocol for this group.

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
var `protocol`: NSNumber? { get }
```

#### Discussion

This property returns an `NSNumber` object containing an `NSUInteger` value corresponding to a member of the [`TKSmartCardProtocol`](tksmartcardprotocol.md) enumeration.

This property is `nil` for the first interface group (global), as it has no assigned protocol.

## See Also

- [var ta: NSNumber?](tksmartcardatr/interfacegroup/ta.md)
  The TA interface byte of ATR group, or `nil` if TA is not present.
- [var tb: NSNumber?](tksmartcardatr/interfacegroup/tb.md)
  The TB interface byte of ATR group, or `nil` if TB is not present.
- [var tc: NSNumber?](tksmartcardatr/interfacegroup/tc.md)
  The TC interface byte of ATR group, or `nil` if TC is not present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcardatr/interfacegroup/protocol)*