# DateComponentsFormatter.UnitsStyle

**Framework**: Foundation  
**Kind**: enum  
**Role**: Enumeration

Constants for specifying how to represent quantities of time.

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
enum UnitsStyle
```

```c
enum NSDateComponentsFormatterUnitsStyle : NSInteger;
```

## Overview

All date and time values are localized and formatted according to the current user’s language preferences.

The following table shows how the quantity of 9 hours, 41 minutes, and 30 seconds is displayed in the U.S. English locale for each style:

| Style | Displayed result |
| --- | --- |
| [`DateComponentsFormatter.UnitsStyle.spellOut`](./unitsstyle-swift.enum/spellout.md) | “nine hours, forty-one minutes, thirty seconds” |
| [`DateComponentsFormatter.UnitsStyle.full`](./unitsstyle-swift.enum/full.md) | “9 hours, 41 minutes, 30 seconds” |
| [`DateComponentsFormatter.UnitsStyle.short`](./unitsstyle-swift.enum/short.md) | “9 hr, 41 min, 30 sec” |
| [`DateComponentsFormatter.UnitsStyle.brief`](./unitsstyle-swift.enum/brief.md) | “9hr 41min 30sec” |
| [`DateComponentsFormatter.UnitsStyle.abbreviated`](./unitsstyle-swift.enum/abbreviated.md) | “9h 41m 30s” |
| [`DateComponentsFormatter.UnitsStyle.positional`](./unitsstyle-swift.enum/positional.md) | “9:31:30” |

## Topics

### Styles
- [DateComponentsFormatter.UnitsStyle.spellOut](./unitsstyle-swift.enum/spellout.md)
  A style that spells out the units and quantities of time.
- [DateComponentsFormatter.UnitsStyle.full](./unitsstyle-swift.enum/full.md)
  A style that spells out the units of time, but not the quantities.
- [DateComponentsFormatter.UnitsStyle.short](./unitsstyle-swift.enum/short.md)
  A style that uses a shortened spelling for units.
- [DateComponentsFormatter.UnitsStyle.brief](./unitsstyle-swift.enum/brief.md)
  A style that uses a shortened spelling for units of time that is shorter than [`DateComponentsFormatter.UnitsStyle.short`](./unitsstyle-swift.enum/short.md).
- [DateComponentsFormatter.UnitsStyle.abbreviated](./unitsstyle-swift.enum/abbreviated.md)
  A style that uses the most abbreviated spelling for units of time.
- [DateComponentsFormatter.UnitsStyle.positional](./unitsstyle-swift.enum/positional.md)
  A style that uses the position of a unit of time to identify its value.
### Initializers
- [init?(rawValue: Int)](./unitsstyle-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [DateComponentsFormatter.ZeroFormattingBehavior](./zeroformattingbehavior-swift.struct.md)
  Formatting constants for when values contain zeroes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/datecomponentsformatter/unitsstyle-swift.enum)*