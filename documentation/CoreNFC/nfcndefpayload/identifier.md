# identifier

**Framework**: Core NFC  
**Kind**: property

The identifier of the payload, as defined by the NDEF specification.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var identifier: Data { get set }
```

## See Also

- [var payload: Data](nfcndefpayload/payload.md)
  The payload, as defined by the NDEF specification.
- [var type: Data](nfcndefpayload/type.md)
  The type of the payload, as defined by the NDEF specification.
- [var typeNameFormat: NFCTypeNameFormat](nfcndefpayload/typenameformat.md)
  The Type Name Format field of the payload, as defined by the NDEF specification.
- [enum NFCTypeNameFormat](nfctypenameformat.md)
  The Type Name Format values that specify the content type for the payload data in an NFC NDEF message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefpayload/identifier)*