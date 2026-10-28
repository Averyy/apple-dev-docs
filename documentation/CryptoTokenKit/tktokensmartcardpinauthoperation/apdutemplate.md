# apduTemplate

**Framework**: CryptoTokenKit  
**Kind**: property  
**Role**: Instance Property

The template into which the PIN is filled in. `nil` by default.

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
var apduTemplate: Data? { get set }
```

```objc
@property (copy, nullable) NSData * APDUTemplate;
```

## Discussion

If `nil`, the system will not attempt to authenticate by sending the formatted APDU to the Smart Card. Instead, the token itself is expected to perform the authentication. You are encouraged to provide an APDU template, if possible, as it allows the use of a hardware interface for secure PIN entry, provided one exists.

## See Also

### Configuring the Operation
- [var pinFormat: TKSmartCardPINFormat](./pinformat.md)
  The PIN format.
- [var pinByteOffset: Int](./pinbyteoffset.md)
  The offset, in bytes, within the APDU template to mark the location for filling in the PIN.
- [var smartCard: TKSmartCard?](./smartcard.md)
  A Smart Card to which the formatted APDU is sent in order to authenticate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptotokenkit/tktokensmartcardpinauthoperation/apdutemplate)*