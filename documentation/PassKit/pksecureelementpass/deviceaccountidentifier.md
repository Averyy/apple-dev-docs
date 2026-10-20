# deviceAccountIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The unique identifier for the device-specific account number.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var deviceAccountIdentifier: String { get }
```

```objc
@property (strong, readonly) NSString * deviceAccountIdentifier;
```

## See Also

### Getting the hardware attributes
- [var deviceAccountNumberSuffix: String](./deviceaccountnumbersuffix.md)
  A display-ready version of the device-specific account number.
- [var devicePassIdentifier: String?](./devicepassidentifier.md)
  An opaque value for the pass.
- [var pairedTerminalIdentifier: String?](./pairedterminalidentifier.md)
  The unique identifier of the paired terminal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksecureelementpass/deviceaccountidentifier)*