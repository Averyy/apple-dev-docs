# pinByteOffset

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The offset, in bytes, within the APDU template to mark the location for filling in the PIN.

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
var pinByteOffset: Int { get set }
```

```objc
@property NSInteger PINByteOffset;
```

## See Also

### Configuring the Operation
- [var pinFormat: TKSmartCardPINFormat](./pinformat.md)
  The PIN format.
- [var apduTemplate: Data?](./apdutemplate.md)
  The template into which the PIN is filled in. `nil` by default.
- [var smartCard: TKSmartCard?](./smartcard.md)
  A Smart Card to which the formatted APDU is sent in order to authenticate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/pinbyteoffset)*