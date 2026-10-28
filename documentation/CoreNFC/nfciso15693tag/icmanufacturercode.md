# icManufacturerCode

**Framework**: Core NFC  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The IC manufacturer code of the tag.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var icManufacturerCode: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger icManufacturerCode;
```

## Discussion

The IC manufacturer code comes from bits 49 through 56 of the [`identifier`](./identifier.md) data, in accordance with ISO/IEC 7816-6:2004.

## See Also

### Getting Tag Information
- [var icSerialNumber: Data](./icserialnumber.md)
  The IC serial number assigned to the tag by the manufacturer.
- [var identifier: Data](./identifier.md)
  The unique hardware identifier of the tag.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfciso15693tag/icmanufacturercode)*