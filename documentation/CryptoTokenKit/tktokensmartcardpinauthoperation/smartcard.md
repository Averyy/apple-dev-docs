# smartCard

**Framework**: CryptoTokenKit  
**Kind**: property

A Smart Card to which the formatted APDU is sent in order to authenticate.

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
var smartCard: TKSmartCard? { get set }
```

#### Discussion

This property is only used if the [`apduTemplate`](tktokensmartcardpinauthoperation/apdutemplate.md) property has a set value.

## See Also

- [var pinFormat: TKSmartCardPINFormat](tktokensmartcardpinauthoperation/pinformat.md)
  The PIN format.
- [var apduTemplate: Data?](tktokensmartcardpinauthoperation/apdutemplate.md)
  The template into which the PIN is filled in. `nil` by default.
- [var pinByteOffset: Int](tktokensmartcardpinauthoperation/pinbyteoffset.md)
  The offset, in bytes, within the APDU template to mark the location for filling in the PIN.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/smartcard)*