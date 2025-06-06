# integerValue(asTypeTruncatingIfNeeded:)

**Framework**: Core HID  
**Kind**: method

The raw value of the data cast as an integer type, with no transformations applied.

**Availability**:
- macOS 15.0+

## Declaration

```swift
func integerValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType where IntegerType : FixedWidthInteger
```

## Mentions

- [Communicating with human interface devices](communicatingwithhiddevices.md)

#### Return Value

The data cast as the requested type.

## Parameters

- `asTypeTruncatingIfNeeded`: The type to which to cast the underlying bytes, truncating or extending the bytes as necessary.

## See Also

- [var bytes: Data](hidelement/value/bytes.md)
  The data as an array of bytes.
- [func logicalValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType?](hidelement/value/logicalvalue(astypetruncatingifneeded:).md)
  The raw value of the data cast as an integer type and bound by the [`HIDElement`](hidelement.md)’s logical minimum and logical maximum values.
- [func physicalValue<IntegerType, FloatingType>(fromTypeTruncatingIfNeeded: IntegerType.Type, as: FloatingType.Type) -> FloatingType?](hidelement/value/physicalvalue(fromtypetruncatingifneeded:as:).md)
  The logical value of the data, shifted and scaled by the [`HIDElement`](hidelement.md)’s physical minimum, physical maximum and exponent.
- [var timestamp: SuspendingClock.Instant](hidelement/value/timestamp.md)
  The time that this data was received by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/value/integervalue(astypetruncatingifneeded:))*