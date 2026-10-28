# useExtendedLength

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

Whether to use extended length APDU.

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
var useExtendedLength: Bool { get set }
```

```objc
@property BOOL useExtendedLength;
```

## Discussion

By default, this property is set to [`true`](../../Swift/true.md) when the Smart Card slot supports transmitting extended length commands, and the ATR announces that extended length APDU is supported.

## See Also

### Configuring APDU Behavior
- [var cla: UInt8](./cla.md)
  The CLA byte used for APDU transmission. `0x00` by default.
- [var useCommandChaining: Bool](./usecommandchaining.md)
  Whether to use command chaining of APDU with a data field longer than 255 bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/useextendedlength)*