# Date.FormatString

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

Use `Date.FormatString` with [`Date.VerbatimFormatStyle`](./verbatimformatstyle.md) or [`Date.ParseStrategy`](./parsestrategy.md) to create fixed-pattern format strings for dates. You build format strings using string interpolation with date field symbols:

```swift
let format: Date.FormatString = "\(year: .defaultDigits)-\(month: .twoDigits)-\(day: .twoDigits)"
```

## Topics

### Default Implementations
- [ExpressibleByStringInterpolation Implementations](./formatstring/expressiblebystringinterpolation-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringInterpolation](../../Swift/expressiblebystringinterpolation.md)
- [ExpressibleByStringLiteral](../../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/date/formatstring)*