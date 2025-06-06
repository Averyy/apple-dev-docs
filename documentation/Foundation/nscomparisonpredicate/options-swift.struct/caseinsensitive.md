# caseInsensitive

**Framework**: Foundation  
**Kind**: property

A case-insensitive predicate.

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
static var caseInsensitive: NSComparisonPredicate.Options { get }
```

#### Discussion

You represent this option in a predicate format string using a `[c]` following a string operation (for example, `"NeXT" like[c] "next"`).

## See Also

- [static var diacriticInsensitive: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/diacriticinsensitive.md)
  A diacritic-insensitive predicate.
- [static var normalized: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/normalized.md)
  A predicate that indicates you’ve preprocessed the strings to compare.
- [static var diacriticInsensitive: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/diacriticinsensitive.md)
  A diacritic-insensitive predicate.
- [static var normalized: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/normalized.md)
  A predicate that indicates you’ve preprocessed the strings to compare.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/options-swift.struct/caseinsensitive)*