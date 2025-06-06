# localizedStandard

**Framework**: Foundation  
**Kind**: property

A comparator that compares a string using a localized, numeric comparison in the current locale.

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
static var localizedStandard: String.Comparator { get }
```

#### Discussion

Compares [`String`](https://developer.apple.com/documentation/Swift/String) in a manner similar to the Finder.

## See Also

- [var order: SortOrder](sortcomparator/order.md)
  The sort order that the comparator uses to compare.
- [static var localized: String.Comparator](sortcomparator/localized.md)
  A comparator that compares a string using a localized comparison in the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/sortcomparator/localizedstandard)*