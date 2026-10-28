# icSerialNumber

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The IC serial number assigned to the tag by the manufacturer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var icSerialNumber: Data { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * icSerialNumber;
```

## Discussion

The IC serial number comes from bits 1 through 48 of the [`identifier`](./identifier.md) data and is in big-endian byte order.

## See Also

### Getting Tag Information
- [var icManufacturerCode: Int](./icmanufacturercode.md)
  The IC manufacturer code of the tag.
- [var identifier: Data](./identifier.md)
  The unique hardware identifier of the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/icserialnumber)*