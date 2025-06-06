# DateComponentsFormatter.UnitsStyle.positional

**Framework**: Foundation  
**Kind**: case

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

#### Discussion

This style is most commonly used for time values where the hour, minute, and second values are separated by colons. You can use the zero formatting behaviors ([`DateComponentsFormatter.ZeroFormattingBehavior`](datecomponentsformatter/zeroformattingbehavior-swift.struct.md)) to further modify the formatting of this value.

For example, one hour and ten minutes is displayed in the U.S. English locale as “1:10:00”.

> **Note**:  This style may fall back to the behavior of [`DateComponentsFormatter.UnitsStyle.abbreviated`](datecomponentsformatter/unitsstyle-swift.enum/abbreviated.md) when attempting to display large time quantities.

 This style may fall back to the behavior of [`DateComponentsFormatter.UnitsStyle.abbreviated`](datecomponentsformatter/unitsstyle-swift.enum/abbreviated.md) when attempting to display large time quantities.

## See Also

- [DateComponentsFormatter.UnitsStyle.spellOut](datecomponentsformatter/unitsstyle-swift.enum/spellout.md)
  A style that spells out the units and quantities of time.
- [DateComponentsFormatter.UnitsStyle.full](datecomponentsformatter/unitsstyle-swift.enum/full.md)
  A style that spells out the units of time, but not the quantities.
- [DateComponentsFormatter.UnitsStyle.short](datecomponentsformatter/unitsstyle-swift.enum/short.md)
  A style that uses a shortened spelling for units.
- [DateComponentsFormatter.UnitsStyle.brief](datecomponentsformatter/unitsstyle-swift.enum/brief.md)
  A style that uses a shortened spelling for units of time that is shorter than [`DateComponentsFormatter.UnitsStyle.short`](datecomponentsformatter/unitsstyle-swift.enum/short.md).
- [DateComponentsFormatter.UnitsStyle.abbreviated](datecomponentsformatter/unitsstyle-swift.enum/abbreviated.md)
  A style that uses the most abbreviated spelling for units of time.
- [DateComponentsFormatter.UnitsStyle.spellOut](datecomponentsformatter/unitsstyle-swift.enum/spellout.md)
  A style that spells out the units and quantities of time.
- [DateComponentsFormatter.UnitsStyle.full](datecomponentsformatter/unitsstyle-swift.enum/full.md)
  A style that spells out the units of time, but not the quantities.
- [DateComponentsFormatter.UnitsStyle.short](datecomponentsformatter/unitsstyle-swift.enum/short.md)
  A style that uses a shortened spelling for units.
- [DateComponentsFormatter.UnitsStyle.brief](datecomponentsformatter/unitsstyle-swift.enum/brief.md)
  A style that uses a shortened spelling for units of time that is shorter than [`DateComponentsFormatter.UnitsStyle.short`](datecomponentsformatter/unitsstyle-swift.enum/short.md).
- [DateComponentsFormatter.UnitsStyle.abbreviated](datecomponentsformatter/unitsstyle-swift.enum/abbreviated.md)
  A style that uses the most abbreviated spelling for units of time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/unitsstyle-swift.enum/positional)*