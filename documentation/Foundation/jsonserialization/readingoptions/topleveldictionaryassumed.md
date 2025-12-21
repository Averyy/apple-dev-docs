# topLevelDictionaryAssumed

**Framework**: Foundation  
**Kind**: property

Specifies that the parser assumes the top level of the JSON data is a dictionary, even if it doesn’t begin and end with curly braces.

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
static var topLevelDictionaryAssumed: JSONSerialization.ReadingOptions { get }
```

#### Discussion

This is an extension to JSON5 that isn’t part of the specification. [`AttributedString`](attributedstring.md) uses this option, along with [`json5Allowed`](jsonserialization/readingoptions/json5allowed.md), to support the use of JSON5 inside Markdown strings that use multiple custom attributes. Using [`topLevelDictionaryAssumed`](jsonserialization/readingoptions/topleveldictionaryassumed.md) allows for the following syntax in the parentheses of the custom attribute markup:

```other
This is a [Markdown](https://commonmark.org) string with a ^[custom attribute](factor: 10, other: true).
```

Without [`topLevelDictionaryAssumed`](jsonserialization/readingoptions/topleveldictionaryassumed.md), the markup would have to use explicit enclosing braces to declare the contents of the parentheses to be a dictionary:

```other
This is a [Markdown](https://commonmark.org) string with a ^[custom attribute]({factor: 10, other: true}).
```

When you use braces, you must use matched pairs. This means that with [`topLevelDictionaryAssumed`](jsonserialization/readingoptions/topleveldictionaryassumed.md) set, the syntax `({…})` and `(…)` are both legal, but `({…)` and `(…})` are not.

## See Also

- [static var mutableContainers: JSONSerialization.ReadingOptions](jsonserialization/readingoptions/mutablecontainers.md)
  Specifies that arrays and dictionaries in the returned object are mutable.
- [static var mutableLeaves: JSONSerialization.ReadingOptions](jsonserialization/readingoptions/mutableleaves.md)
  Specifies that leaf strings in the JSON object graph are mutable.
- [static var fragmentsAllowed: JSONSerialization.ReadingOptions](jsonserialization/readingoptions/fragmentsallowed.md)
  Specifies that the parser allows top-level objects that aren’t arrays or dictionaries.
- [static var json5Allowed: JSONSerialization.ReadingOptions](jsonserialization/readingoptions/json5allowed.md)
  Specifies that reading serialized JSON data supports the JSON5 syntax.
- [static var allowFragments: JSONSerialization.ReadingOptions](jsonserialization/readingoptions/allowfragments.md)
  A deprecated option that specifies that the parser should allow top-level objects that aren’t arrays or dictionaries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonserialization/readingoptions/topleveldictionaryassumed)*