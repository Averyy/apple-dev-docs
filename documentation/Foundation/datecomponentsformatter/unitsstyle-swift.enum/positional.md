# DateComponentsFormatter.UnitsStyle.positional

**Framework**: Foundation  
**Kind**: case  
**Role**: Case

A style that uses the position of a unit of time to identify its value.

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
case positional
```

```c
NSDateComponentsFormatterUnitsStylePositional
```

#### Discussion

This style is most commonly used for time values where the hour, minute, and second values are separated by colons. You can use the zero formatting behaviors ([`DateComponentsFormatter.ZeroFormattingBehavior`](../zeroformattingbehavior-swift.struct.md)) to further modify the formatting of this value.

For example, one hour and ten minutes is displayed in the U.S. English locale as “1:10:00”.

> **Note**:  This style may fall back to the behavior of [`DateComponentsFormatter.UnitsStyle.abbreviated`](./abbreviated.md) when attempting to display large time quantities.

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
- [DateComponentsFormatter.UnitsStyle.abbreviated](./abbreviated.md)
  A style that uses the most abbreviated spelling for units of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/unitsstyle-swift.enum/positional)*