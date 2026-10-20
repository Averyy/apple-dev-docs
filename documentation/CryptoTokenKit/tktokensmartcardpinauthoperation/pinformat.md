# pinFormat

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The PIN format.

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
var pinFormat: TKSmartCardPINFormat { get set }
```

```objc
@property TKSmartCardPINFormat * PINFormat;
```

#### Discussion

By default, this property is set to a `TKSmartCardPINFormat` object initialized without any further configuration.

## See Also

### Configuring the Operation
- [var apduTemplate: Data?](./apdutemplate.md)
  The template into which the PIN is filled in. `nil` by default.
- [var pinByteOffset: Int](./pinbyteoffset.md)
  The offset, in bytes, within the APDU template to mark the location for filling in the PIN.
- [var smartCard: TKSmartCard?](./smartcard.md)
  A Smart Card to which the formatted APDU is sent in order to authenticate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/pinformat)*