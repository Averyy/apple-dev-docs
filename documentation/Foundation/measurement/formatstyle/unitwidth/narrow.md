# narrow

**Framework**: Foundation  
**Kind**: property

The shortest unit width.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static var narrow: Measurement<UnitType>.FormatStyle.UnitWidth { get }
```

#### Discussion

This width may condense the spacing between the value and the unit; for example, `37.20Cal` or `37,2L`.

## See Also

- [static var wide: Measurement<UnitType>.FormatStyle.UnitWidth](measurement/formatstyle/unitwidth/wide.md)
  A unit width that shows the full unit name.
- [static var abbreviated: Measurement<UnitType>.FormatStyle.UnitWidth](measurement/formatstyle/unitwidth/abbreviated.md)
  An abbreviated unit width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/formatstyle/unitwidth/narrow)*