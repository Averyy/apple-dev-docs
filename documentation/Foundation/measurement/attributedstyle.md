# Measurement.AttributedStyle

**Framework**: Foundation  
**Kind**: struct

A type that provides localized representations of measurements with an attributed string.

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
@dynamicMemberLookup
struct AttributedStyle
```

#### Overview

Use either the [`formatted()`](measurement/formatted().md) or the [`formatted(_:)`](measurement/formatted(_:).md) instance method of [`Measurement`](measurement.md) to create an attributed string representation of a measurement.

The [`formatted()`](measurement/formatted().md) method generates a string using the default measurement format style.

## Topics

### Comparing Measurement Attributed Styles
- [static func == <LeftHandSideType, RightHandSideType>(Measurement<LeftHandSideType>, Measurement<RightHandSideType>) -> Bool](measurement/==(_:_:).md)
  Compare two measurements of the same `Dimension`.
### Structures
- [Measurement.AttributedStyle.ByteCount](measurement/attributedstyle/bytecount.md)
  A format style that converts byte counts into attributed strings.
### Subscripts
- [subscript<T>(dynamicMember _: KeyPath<Measurement<UnitType>.FormatStyle, T>) -> T](measurement/attributedstyle/subscript(dynamicmember:)-83rva.md)
- [subscript<T>(dynamicMember _: WritableKeyPath<Measurement<UnitType>.FormatStyle, T>) -> T](measurement/attributedstyle/subscript(dynamicmember:)-c2b1.md)

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func formatted() -> String](measurement/formatted.md)
  Generates a locale-aware string representation of a measurement using the default measurement format style.
- [func formatted<S>(S) -> S.FormatOutput](measurement/formatted(_:).md)
  Generates a locale-aware string representation of a measurement using the provided measurement format style.
- [Measurement.FormatStyle](measurement/formatstyle.md)
  A type that provides localized representations of measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/attributedstyle)*