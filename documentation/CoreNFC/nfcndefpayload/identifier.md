# identifier

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property

The identifier of the payload, as defined by the NDEF specification.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var identifier: Data { get set }
```

```objc
@property (nonatomic, copy) NSData * identifier;
```

## See Also

### Getting Information About a Payload Record
- [var payload: Data](./payload.md)
  The payload, as defined by the NDEF specification.
- [var type: Data](./type.md)
  The type of the payload, as defined by the NDEF specification.
- [var typeNameFormat: NFCTypeNameFormat](./typenameformat.md)
  The Type Name Format field of the payload, as defined by the NDEF specification.
- [enum NFCTypeNameFormat](../nfctypenameformat.md)
  The Type Name Format values that specify the content type for the payload data in an NFC NDEF message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcndefpayload/identifier)*