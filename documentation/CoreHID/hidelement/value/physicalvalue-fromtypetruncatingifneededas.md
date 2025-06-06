# physicalValue(fromTypeTruncatingIfNeeded:as:)

**Framework**: Core HID  
**Kind**: method

The logical value of the data, shifted and scaled by the [`HIDElement`](hidelement.md)’s physical minimum, physical maximum and exponent.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func physicalValue<IntegerType, FloatingType>(fromTypeTruncatingIfNeeded: IntegerType.Type, as: FloatingType.Type) -> FloatingType? where IntegerType : FixedWidthInteger, FloatingType : BinaryFloatingPoint
```

#### Return Value

The calculated value cast as the requested type, or nil if out of bounds.

#### Discussion

The [`logicalValue(asTypeTruncatingIfNeeded:)`](hidelement/value/logicalvalue(astypetruncatingifneeded:).md) is first retrieved with the specified type. If the logical value is undefined, such as when the raw value is out of bounds, the physical value is also undefined.

More information and example calculations for physical values can be found in the HID specification: See the HID specification for more details: [`https://www.usb.org/hid`](https://developer.apple.comhttps://www.usb.org/hid).

## Parameters

- `fromTypeTruncatingIfNeeded`: The type to cast the underlying bytes to before bounding, shifting and scaling; truncating or extending the bytes as necessary.
- `as`: The type to cast the calculated floating point result to before returning.

## See Also

- [var bytes: Data](hidelement/value/bytes.md)
  The data as an array of bytes.
- [func integerValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType](hidelement/value/integervalue(astypetruncatingifneeded:).md)
  The raw value of the data cast as an integer type, with no transformations applied.
- [func logicalValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType?](hidelement/value/logicalvalue(astypetruncatingifneeded:).md)
  The raw value of the data cast as an integer type and bound by the [`HIDElement`](hidelement.md)’s logical minimum and logical maximum values.
- [var timestamp: SuspendingClock.Instant](hidelement/value/timestamp.md)
  The time that this data was received by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/value/physicalvalue(fromtypetruncatingifneeded:as:))*