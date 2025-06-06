# valueLengthLimits

**Framework**: Swift  
**Kind**: property

The padding or truncating behavior of the unit value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var valueLengthLimits: Range<Int>?
```

#### Discussion

For example, set this to `2...` to force 2-digit padding on all units.

## See Also

- [var allowedUnits: Set<Duration.UnitsFormatStyle.Unit>](duration/unitsformatstyle/allowedunits.md)
  The units that may be included in the output string.
- [Duration.UnitsFormatStyle.Unit](duration/unitsformatstyle/unit.md)
  A unit to use in formatting a duration.
- [var maximumUnitCount: Int?](duration/unitsformatstyle/maximumunitcount.md)
  The maximum number of time units to include in the output string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/unitsformatstyle/valuelengthlimits)*