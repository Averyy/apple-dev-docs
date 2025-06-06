# timestamp

**Framework**: Core HID  
**Kind**: property

The time that this data was received by the system.

**Availability**:
- macOS 15.0+

## Declaration

```swift
var timestamp: SuspendingClock.Instant
```

#### Discussion

The data should only be considered valid at this time, it’s possible for the [`HIDElement`](hidelement.md) to have been updated after this.

## See Also

- [var bytes: Data](hidelement/value/bytes.md)
  The data as an array of bytes.
- [func integerValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType](hidelement/value/integervalue(astypetruncatingifneeded:).md)
  The raw value of the data cast as an integer type, with no transformations applied.
- [func logicalValue<IntegerType>(asTypeTruncatingIfNeeded: IntegerType.Type) -> IntegerType?](hidelement/value/logicalvalue(astypetruncatingifneeded:).md)
  The raw value of the data cast as an integer type and bound by the [`HIDElement`](hidelement.md)’s logical minimum and logical maximum values.
- [func physicalValue<IntegerType, FloatingType>(fromTypeTruncatingIfNeeded: IntegerType.Type, as: FloatingType.Type) -> FloatingType?](hidelement/value/physicalvalue(fromtypetruncatingifneeded:as:).md)
  The logical value of the data, shifted and scaled by the [`HIDElement`](hidelement.md)’s physical minimum, physical maximum and exponent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehid/hidelement/value/timestamp)*