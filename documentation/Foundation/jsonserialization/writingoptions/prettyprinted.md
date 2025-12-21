# prettyPrinted

**Framework**: Foundation  
**Kind**: property

Specifies that the output uses white space and indentation to make the resulting data more readable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var prettyPrinted: JSONSerialization.WritingOptions { get }
```

#### Discussion

If this option isn’t set, the serialization generates the most compact possible JSON representation.

## See Also

- [static var fragmentsAllowed: JSONSerialization.WritingOptions](jsonserialization/writingoptions/fragmentsallowed.md)
  Specifies that the parser should allow top-level objects that aren’t arrays or dictionaries.
- [static var sortedKeys: JSONSerialization.WritingOptions](jsonserialization/writingoptions/sortedkeys.md)
  Specifies that the output sorts keys in lexicographic order.
- [static var withoutEscapingSlashes: JSONSerialization.WritingOptions](jsonserialization/writingoptions/withoutescapingslashes.md)
  Specifies that the output doesn’t prefix slash characters with escape characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonserialization/writingoptions/prettyprinted)*