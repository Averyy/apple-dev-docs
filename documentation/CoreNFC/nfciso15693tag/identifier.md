# identifier

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The unique hardware identifier of the tag.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var identifier: Data { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * identifier;
```

## Discussion

The [`identifier`](./identifier.md) data is in big-endian byte order.

## See Also

### Getting Tag Information
- [var icManufacturerCode: Int](./icmanufacturercode.md)
  The IC manufacturer code of the tag.
- [var icSerialNumber: Data](./icserialnumber.md)
  The IC serial number assigned to the tag by the manufacturer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/identifier)*