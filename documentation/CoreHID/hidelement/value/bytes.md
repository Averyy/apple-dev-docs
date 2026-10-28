# bytes

**Framework**: Core HID  
**Kind**: property  
**Role**: Instance Property

The data as an array of bytes.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var bytes: Data
```

## Mentions

- [Communicating with human interface devices](../../communicatingwithhiddevices.md)

## Discussion

The size of the data must be the [`element`](./element.md)s [`reportSize`](../reportsize.md), rounded up to the next byte.

## See Also

### Get element data and values
- [func integerValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType](./integervalue%28astypetruncatingifneeded%29.md)
  The raw value of the data cast as an integer type, with no transformations applied.
- [func logicalValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType?](./logicalvalue%28astypetruncatingifneeded%29.md)
  The raw value of the data cast as an integer type and bound by the [`HIDElement`](../../hidelement.md)’s logical minimum and logical maximum values.
- [func physicalValue<IntegerType, FloatingType>(fromTypeTruncatingIfNeeded: IntegerType.Type, as: FloatingType.Type) -> FloatingType?](./physicalvalue%28fromtypetruncatingifneeded,as%29.md)
  The logical value of the data, shifted and scaled by the [`HIDElement`](../../hidelement.md)’s physical minimum, physical maximum and exponent.
- [var timestamp: SuspendingClock.Instant](./timestamp.md)
  The time that this data was received by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/value/bytes)*