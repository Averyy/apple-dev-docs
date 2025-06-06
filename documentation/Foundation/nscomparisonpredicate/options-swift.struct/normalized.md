# normalized

**Framework**: Foundation  
**Kind**: property

A predicate that indicates you’ve preprocessed the strings to compare.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var normalized: NSComparisonPredicate.Options { get }
```

#### Discussion

This option supersedes `NSCaseInsensitivePredicateOption` and `NSDiacriticInsensitivePredicateOption`, and is a performance optimization option.

You represent this option in a predicate format string using a `[n]` following a string operation (for example, `"WXYZlan" matches[n] ".lan"`).

## See Also

- [static var caseInsensitive: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/caseinsensitive.md)
  A case-insensitive predicate.
- [static var diacriticInsensitive: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/diacriticinsensitive.md)
  A diacritic-insensitive predicate.
- [static var caseInsensitive: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/caseinsensitive.md)
  A case-insensitive predicate.
- [static var diacriticInsensitive: NSComparisonPredicate.Options](nscomparisonpredicate/options-swift.struct/diacriticinsensitive.md)
  A diacritic-insensitive predicate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nscomparisonpredicate/options-swift.struct/normalized)*