# abbreviated

**Framework**: Swift  
**Kind**: property  
**Role**: Type Property

An abbreviated unit name.

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
static var abbreviated: Duration.UnitsFormatStyle.UnitWidth { get }
```

#### Discussion

For example, `abbreviated` produces the unit label “3 hr” for a 3-hour duration in the `en_US` locale.

## See Also

### Duration unit widths
- [static var condensedAbbreviated: Duration.UnitsFormatStyle.UnitWidth](./condensedabbreviated.md)
  An abbreviated unit name, with condensed space between the value and name.
- [static var narrow: Duration.UnitsFormatStyle.UnitWidth](./narrow.md)
  The shortest possible unit name.
- [static var wide: Duration.UnitsFormatStyle.UnitWidth](./wide.md)
  The full unit name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/duration/unitsformatstyle/unitwidth-swift.struct/abbreviated)*