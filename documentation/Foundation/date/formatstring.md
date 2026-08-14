# Date.FormatString

**Framework**: Foundation  
**Kind**: struct

A type that represents a fixed date format string using string interpolation.

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
struct FormatString
```

#### Overview

Use `Date.FormatString` with [`Date.VerbatimFormatStyle`](date/verbatimformatstyle.md) or [`Date.ParseStrategy`](date/parsestrategy.md) to create fixed-pattern format strings for dates. You build format strings using string interpolation with date field symbols:

```swift
let format: Date.FormatString = "\(year: .defaultDigits)-\(month: .twoDigits)-\(day: .twoDigits)"
```

## Topics

### Default Implementations
- [ExpressibleByStringInterpolation Implementations](date/formatstring/expressiblebystringinterpolation-implementations.md)

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringInterpolation](../swift/expressiblebystringinterpolation.md)
- [ExpressibleByStringLiteral](../swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstring)*