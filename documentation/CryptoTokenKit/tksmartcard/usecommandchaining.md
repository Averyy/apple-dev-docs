# useCommandChaining

**Framework**: CryptoTokenKit  
**Kind**: property

Whether to use command chaining of APDU with a data field longer than 255 bytes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var useCommandChaining: Bool { get set }
```

#### Discussion

By default, this property is set to [`true`](https://developer.apple.com/documentation/Swift/true) when the Smart Card ATR announces that command chaining is supported.

## See Also

- [var cla: UInt8](tksmartcard/cla.md)
  The CLA byte used for APDU transmission. `0x00` by default.
- [var useExtendedLength: Bool](tksmartcard/useextendedlength.md)
  Whether to use extended length APDU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/usecommandchaining)*