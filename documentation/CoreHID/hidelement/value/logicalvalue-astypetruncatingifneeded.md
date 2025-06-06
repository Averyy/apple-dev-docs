# logicalValue(asTypeTruncatingIfNeeded:)

**Framework**: Core HID  
**Kind**: method

The raw value of the data cast as an integer type and bound by the [`HIDElement`](hidelement.md)’s logical minimum and logical maximum values.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func logicalValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType? where IntegerType : FixedWidthInteger
```

#### Return Value

The data cast as the requested type, or nil if out of bounds.

#### Discussion

If the raw value is out of bounds, this returns `nil`. For example, if the logical minimum and logical maximum are specified as `1` and `127` respectively, and the raw value is `0`, the logical value is undefined.

## Parameters

- `asTypeTruncatingIfNeeded`: The type to which to cast the underlying bytes before applying bounds, truncating or extending the bytes as necessary.

## See Also

- [var bytes: Data](hidelement/value/bytes.md)
  The data as an array of bytes.
- [func integerValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType](hidelement/value/integervalue(astypetruncatingifneeded:).md)
  The raw value of the data cast as an integer type, with no transformations applied.
- [func physicalValue<IntegerType, FloatingType>(fromTypeTruncatingIfNeeded: IntegerType.Type, as: FloatingType.Type) -> FloatingType?](hidelement/value/physicalvalue(fromtypetruncatingifneeded:as:).md)
  The logical value of the data, shifted and scaled by the [`HIDElement`](hidelement.md)’s physical minimum, physical maximum and exponent.
- [var timestamp: SuspendingClock.Instant](hidelement/value/timestamp.md)
  The time that this data was received by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/value/logicalvalue(astypetruncatingifneeded:))*