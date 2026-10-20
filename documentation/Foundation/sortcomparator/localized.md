# localized

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

A comparator that compares a string using a localized comparison in the current locale.

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
static var localized: String.Comparator { get }
```

Available when `Self` is `String.Comparator`.

## See Also

### Inspecting a Comparator
- [var order: SortOrder](./order.md)
  The sort order that the comparator uses to compare.
- [static var localizedStandard: String.Comparator](./localizedstandard.md)
  A comparator that compares a string using a localized, numeric comparison in the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/sortcomparator/localized)*