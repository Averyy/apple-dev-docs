# Date.RelativeFormatStyle.UnitsStyle

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that represents the style to use when formatting the units of relative dates.

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
struct UnitsStyle
```

## Overview

Cases include [`wide`](./unitsstyle-swift.struct/wide.md), [`narrow`](./unitsstyle-swift.struct/narrow.md), [`abbreviated`](./unitsstyle-swift.struct/abbreviated.md) and [`spellOut`](./unitsstyle-swift.struct/spellout.md).

## Topics

### Modifying a Relative Date Format Units Style
- [static var abbreviated: Date.RelativeFormatStyle.UnitsStyle](./unitsstyle-swift.struct/abbreviated.md)
  A style that uses abbreviated units, such as “2 mo. ago”.
- [static var narrow: Date.RelativeFormatStyle.UnitsStyle](./unitsstyle-swift.struct/narrow.md)
  A style that uses the shortest units, such as “2 mo. ago”.
- [static var spellOut: Date.RelativeFormatStyle.UnitsStyle](./unitsstyle-swift.struct/spellout.md)
  A style that spells out units, such as “two months ago”.
- [static var wide: Date.RelativeFormatStyle.UnitsStyle](./unitsstyle-swift.struct/wide.md)
  A style that uses full representation of units, such as “2 months ago”.
### Comparing Relative Date Format Units Styles
- [static func == (Date, Date) -> Bool](../eqeq%28_,_%29.md)
  Returns true if the two `Date` values represent the same point in time.

## Relationships

### Conforms To
- [Decodable](../../../Swift/decodable.md)
- [Encodable](../../../Swift/encodable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Supporting Types
- [Date.RelativeFormatStyle.Presentation](./presentation-swift.struct.md)
  A type that represents the style to use when formatting relative dates, such as “1 week ago” or “last week”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/relativeformatstyle/unitsstyle-swift.struct)*