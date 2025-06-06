# useExtendedLength

**Framework**: CryptoTokenKit  
**Kind**: property

Whether to use extended length APDU.

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
var useExtendedLength: Bool { get set }
```

#### Discussion

By default, this property is set to [`true`](https://developer.apple.com/documentation/swift/true) when the Smart Card slot supports transmitting extended length commands, and the ATR announces that extended length APDU is supported.

## See Also

- [var cla: UInt8](tksmartcard/cla.md)
  The CLA byte used for APDU transmission. `0x00` by default.
- [var useCommandChaining: Bool](tksmartcard/usecommandchaining.md)
  Whether to use command chaining of APDU with a data field longer than 255 bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/useextendedlength)*