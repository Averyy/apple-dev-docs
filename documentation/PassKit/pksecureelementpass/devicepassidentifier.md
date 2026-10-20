# devicePassIdentifier

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

An opaque value for the pass.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.2+

## Declaration

```swift
var devicePassIdentifier: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * devicePassIdentifier;
```

#### Discussion

> ❗ **Important**:  This property’s value is unique for each issuer. This property is available only to developers who work with Apple to enable this functionality.

## See Also

### Getting the hardware attributes
- [var deviceAccountIdentifier: String](./deviceaccountidentifier.md)
  The unique identifier for the device-specific account number.
- [var deviceAccountNumberSuffix: String](./deviceaccountnumbersuffix.md)
  A display-ready version of the device-specific account number.
- [var pairedTerminalIdentifier: String?](./pairedterminalidentifier.md)
  The unique identifier of the paired terminal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pksecureelementpass/devicepassidentifier)*