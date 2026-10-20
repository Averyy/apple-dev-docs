# DateComponentsFormatter.UnitsStyle.abbreviated

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

A style that uses the most abbreviated spelling for units of time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case abbreviated
```

```c
NSDateComponentsFormatterUnitsStyleAbbreviated
```

#### Discussion

This style represents the shortest representation of units and quantities of time.

For example, the quantity of 3 years, 9 months, 26 days, 19 hours, and 17 seconds is displayed in the U.S. English locale as “3y 9mo 26d 19h 17s”.

## See Also

### Styles
- [DateComponentsFormatter.UnitsStyle.spellOut](./spellout.md)
  A style that spells out the units and quantities of time.
- [DateComponentsFormatter.UnitsStyle.full](./full.md)
  A style that spells out the units of time, but not the quantities.
- [DateComponentsFormatter.UnitsStyle.short](./short.md)
  A style that uses a shortened spelling for units.
- [DateComponentsFormatter.UnitsStyle.brief](./brief.md)
  A style that uses a shortened spelling for units of time that is shorter than [`DateComponentsFormatter.UnitsStyle.short`](./short.md).
- [DateComponentsFormatter.UnitsStyle.positional](./positional.md)
  A style that uses the position of a unit of time to identify its value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/unitsstyle-swift.enum/abbreviated)*