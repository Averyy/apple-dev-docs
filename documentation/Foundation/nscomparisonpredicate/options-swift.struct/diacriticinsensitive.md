# diacriticInsensitive

**Framework**: Foundation  
**Kind**: property

A diacritic-insensitive predicate.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var diacriticInsensitive: NSComparisonPredicate.Options { get }
```

#### Discussion

You represent this option in a predicate format string using a `[d]` following a string operation (for example, `"naïve" like[d] "naive"`).

## See Also

- [static var caseInsensitive: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/caseinsensitive.md)
  A case-insensitive predicate.
- [static var normalized: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/normalized.md)
  A predicate that indicates you’ve preprocessed the strings to compare.
- [static var caseInsensitive: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/caseinsensitive.md)
  A case-insensitive predicate.
- [static var normalized: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/normalized.md)
  A predicate that indicates you’ve preprocessed the strings to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/options-swift.struct/diacriticinsensitive)*