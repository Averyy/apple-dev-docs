# String.Comparator

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A `String` comparison performed using the given comparison options and locale.

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
struct Comparator
```

## Topics

### Initializers
- [init(String.StandardComparator)](./comparator/init%28_%29.md)
  Creates a `String.Comparator` that represents the same comparison as the given `String.StandardComparator`.
- [init(options: String.CompareOptions, locale: Locale?, order: SortOrder)](./comparator/init%28options,locale,order%29.md)
  Creates a `String.Comparator` with the given `CompareOptions` and `Locale`.
### Instance Properties
- [let locale: Locale?](./comparator/locale.md)
  The locale to use for comparison if the comparator is localized, otherwise nil.
- [let options: String.CompareOptions](./comparator/options.md)
  The options to use for comparison.

## Relationships

### Conforms To
- [Decodable](../decodable.md)
- [Encodable](../encodable.md)
- [Equatable](../equatable.md)
- [Hashable](../hashable.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)
- [SortComparator](../../Foundation/sortcomparator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/comparator)*