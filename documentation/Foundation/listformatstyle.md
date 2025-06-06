# ListFormatStyle

**Framework**: Foundation  
**Kind**: struct

A type that formats lists of items with a separator and conjunction appropriate for a given locale.

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
struct ListFormatStyle<Style, Base> where Style : FormatStyle, Base : Sequence, Style.FormatInput == Base.Element, Style.FormatOutput == String
```

#### Overview

A list format style creates human readable text from a [`Sequence`](https://developer.apple.com/documentation/Swift/Sequence) of values. Customize the formatting behavior of the list using the [`width`](listformatstyle/width-swift.property.md), [`listType`](listformatstyle/listtype-swift.property.md), and [`locale`](listformatstyle/locale.md) properties. The system automatically caches unique configurations of [`ListFormatStyle`](listformatstyle.md) to enhance performance.

Use either [`formatted()`](https://developer.apple.com/documentation/Swift/Sequence/formatted()) or [`formatted(_:)`](https://developer.apple.com/documentation/Swift/Sequence/formatted(_:)), both instance methods of [`Sequence`](https://developer.apple.com/documentation/Swift/Sequence), to create a string representation of the items.

The [`formatted()`](https://developer.apple.com/documentation/Swift/Sequence/formatted()) method applies the default list format style to a sequence of strings. For example:

```swift
["Kristin", "Paul", "Ana", "Bill"].formatted()
// Kristin, Paul, Ana, and Bill
```

You can customize a list’s `type` and `width` properties.

- The [`listType`](listformatstyle/listtype-swift.property.md) property specifies the semantics of the list.
- The [`width`](listformatstyle/width-swift.property.md) property determines the size of the returned string.

The [`formatted(_:)`](https://developer.apple.com/documentation/Swift/Sequence/formatted(_:)) method to applies a custom list format style. You can use the static factory method [`list(type:width:)`](formatstyle/list(type:width:).md) to create a custom list format style as a parameter to the method.

This example formats a sequence with a [`ListFormatStyle.ListType.and`](listformatstyle/listtype-swift.enum/and.md) list type and [`ListFormatStyle.Width.short`](listformatstyle/width-swift.enum/short.md) width:

```swift
["Kristin", "Paul", "Ana", "Bill"].formatted(.list(type: .and, width: .short))
// Kristin, Paul, Ana, & Bill
```

You can provide a member format style to transform each list element to a string in applications where the elements aren’t already strings. For example, the following code sample uses an [`IntegerFormatStyle`](integerformatstyle.md) to convert a range of integer values into a list:

```swift
(5201719 ... 5201722).formatted(.list(memberStyle: IntegerFormatStyle(), type: .or, width: .standard))
// For locale: en_US: 5,201,719, 5,201,720, 5,201,721, or 5,201,722
// For locale: fr_CA: 5 201 719, 5 201 720, 5 201 721, ou 5 201 722
```

> **Note**:  The generated string is locale-dependent and incorporates linguistic and cultural conventions of the user.

 The generated string is locale-dependent and incorporates linguistic and cultural conventions of the user.

You can create and reuse a list format style instance to format similar sequences. For example:

```swift
let percentStyle = ListFormatStyle<FloatingPointFormatStyle.Percent, StrideThrough<Double>>(memberStyle: .percent)
stride(from: 7.5, through: 9.0, by: 0.5).formatted(percentStyle)
// 7.5%, 8%, 8.5%, and 9%
stride(from: 89.0, through: 95.0, by: 2.0).formatted(percentStyle)
// 89%, 91%, 93%, and 95%
```

## Topics

### Creating a list format style
- [init(memberStyle: Style)](listformatstyle/init(memberstyle:).md)
  Creates an instance using the provided format style.
### Modifying a list format style
- [var width: ListFormatStyle<Style, Base>.Width](listformatstyle/width-swift.property.md)
  The size of the list.
- [ListFormatStyle.Width](listformatstyle/width-swift.enum.md)
  The type representing the width of a list.
- [var listType: ListFormatStyle<Style, Base>.ListType](listformatstyle/listtype-swift.property.md)
  The type of the list.
- [ListFormatStyle.ListType](listformatstyle/listtype-swift.enum.md)
  A type that describes whether the returned list contains cumulative or alternative elements.
- [var locale: Locale](listformatstyle/locale.md)
  The locale to use when formatting items in the list.
### Applying currency styles
- [IntegerFormatStyle.Currency](integerformatstyle/currency.md)
  A format style that converts between integer currency values and their textual representations.
### Applying measurement styles
- [Measurement.FormatStyle](measurement/formatstyle.md)
  A type that provides localized representations of measurements.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [FormatStyle](formatstyle.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol FormatStyle](formatstyle.md)
  A type that converts a given data type into a representation in another type, such as a string.
- [struct IntegerFormatStyle](integerformatstyle.md)
  A structure that converts between integer values and their textual representations.
- [struct FloatingPointFormatStyle](floatingpointformatstyle.md)
  A structure that converts between floating-point values and their textual representations.
- [Decimal.FormatStyle](decimal/formatstyle.md)
  A structure that converts between decimal values and their textual representations.
- [struct StringStyle](stringstyle.md)
- [struct FormatStyle](url/formatstyle.md)
  A structure that converts between URL instances and their textual representations.
- [struct FormatStyleCapitalizationContext](formatstylecapitalizationcontext.md)
  The capitalization formatting context used when formatting dates and times.
- [Format Style Configurations](format-style-configurations.md)
  Behaviors for traits like numeric precision, rounding, and scale, used for formatting and parsing numeric values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/listformatstyle)*