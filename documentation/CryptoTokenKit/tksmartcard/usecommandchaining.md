# useCommandChaining

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property BOOL useCommandChaining;
```

#### Discussion

By default, this property is set to [`true`](../../Swift/true.md) when the Smart Card ATR announces that command chaining is supported.

## See Also

### Configuring APDU Behavior
- [var cla: UInt8](./cla.md)
  The CLA byte used for APDU transmission. `0x00` by default.
- [var useExtendedLength: Bool](./useextendedlength.md)
  Whether to use extended length APDU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/usecommandchaining)*