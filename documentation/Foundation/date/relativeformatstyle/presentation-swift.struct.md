# Date.RelativeFormatStyle.Presentation

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A type that represents the style to use when formatting relative dates, such as “1 week ago” or “last week”.

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
struct Presentation
```

## Overview

Cases include `named` and `numeric`.

## Topics

### Modifying Relative Date Style Presentations
- [static var named: Date.RelativeFormatStyle.Presentation](./presentation-swift.struct/named.md)
  A style that uses named styles to describe relative dates, such as “yesterday”, “last week”, or “next week”.
- [static var numeric: Date.RelativeFormatStyle.Presentation](./presentation-swift.struct/numeric.md)
  A style that uses a numeric style to describe relative dates, such as “1 day ago” or “in 3 weeks”.
### Comparing Relative Date Style Presentations
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
- [Date.RelativeFormatStyle.UnitsStyle](./unitsstyle-swift.struct.md)
  A type that represents the style to use when formatting the units of relative dates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/relativeformatstyle/presentation-swift.struct)*