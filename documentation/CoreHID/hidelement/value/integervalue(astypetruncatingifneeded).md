# integerValue(asTypeTruncatingIfNeeded:)

**Framework**: Core HID  
**Kind**: method  
**Role**: Instance Method

The raw value of the data cast as an integer type, with no transformations applied.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func integerValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType where IntegerType : FixedWidthInteger
```

## Mentions

- [Communicating with human interface devices](../../communicatingwithhiddevices.md)

## Return Value

The data cast as the requested type.

## Parameters

- `asTypeTruncatingIfNeeded`: The type to which to cast the underlying bytes, truncating or extending the bytes as necessary.

## See Also

### Get element data and values
- [var bytes: Data](./bytes.md)
  The data as an array of bytes.
- [func logicalValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType?](./logicalvalue%28astypetruncatingifneeded%29.md)
  The raw value of the data cast as an integer type and bound by the [`HIDElement`](../../hidelement.md)’s logical minimum and logical maximum values.
- [func physicalValue<IntegerType, FloatingType>(fromTypeTruncatingIfNeeded: IntegerType.Type, as: FloatingType.Type) -> FloatingType?](./physicalvalue%28fromtypetruncatingifneeded,as%29.md)
  The logical value of the data, shifted and scaled by the [`HIDElement`](../../hidelement.md)’s physical minimum, physical maximum and exponent.
- [var timestamp: SuspendingClock.Instant](./timestamp.md)
  The time that this data was received by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/value/integervalue(astypetruncatingifneeded:))*