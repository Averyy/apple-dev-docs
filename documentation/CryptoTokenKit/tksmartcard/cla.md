# cla

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The CLA byte used for APDU transmission. `0x00` by default.

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
var cla: UInt8 { get set }
```

```objc
@property UInt8 cla;
```

## See Also

### Configuring APDU Behavior
- [var useExtendedLength: Bool](./useextendedlength.md)
  Whether to use extended length APDU.
- [var useCommandChaining: Bool](./usecommandchaining.md)
  Whether to use command chaining of APDU with a data field longer than 255 bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tksmartcard/cla)*