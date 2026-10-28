# Measurement.AttributedStyle

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

Available when `UnitType` inherits `Dimension`.

## Overview

Use either the [`formatted()`](./formatted%28%29.md) or the [`formatted(_:)`](./formatted%28_%29.md) instance method of [`Measurement`](../measurement.md) to create an attributed string representation of a measurement.

The [`formatted()`](./formatted%28%29.md) method generates a string using the default measurement format style.

## Topics

### Formatting a Measurement
- [func format(Measurement<UnitType>) -> AttributedString](./attributedstyle/format%28_%29.md)
  Creates a string representation of a measurement.
### Modififying a Measurement Attributed Style
- [func locale(Locale) -> Measurement<UnitType>.AttributedStyle](./attributedstyle/locale%28_%29.md)
  Modifies the measurement format style to use the specified locale.
### Comparing Measurement Attributed Styles
- [static func == <LeftHandSideType, RightHandSideType>(Measurement<LeftHandSideType>, Measurement<RightHandSideType>) -> Bool](./eqeq%28_,_%29.md)
  Compare two measurements of the same `Dimension`.
### Structures
- [Measurement.AttributedStyle.ByteCount](./attributedstyle/bytecount.md)
  A format style that converts byte counts into attributed strings.
### Subscripts
- [subscript<T>(dynamicMember _: KeyPath<Measurement<UnitType>.FormatStyle, T>) -> T](./attributedstyle/subscript%28dynamicmember%29-83rva.md)
- [subscript<T>(dynamicMember _: WritableKeyPath<Measurement<UnitType>.FormatStyle, T>) -> T](./attributedstyle/subscript%28dynamicmember%29-c2b1.md)

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [FormatStyle](../formatstyle.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Formatting a Measurement
- [func formatted() -> String](./formatted%28%29.md)
  Generates a locale-aware string representation of a measurement using the default measurement format style.
- [func formatted<S>(S) -> S.FormatOutput](./formatted%28_%29.md)
  Generates a locale-aware string representation of a measurement using the provided measurement format style.
- [Measurement.FormatStyle](./formatstyle.md)
  A type that provides localized representations of measurements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/measurement/attributedstyle)*