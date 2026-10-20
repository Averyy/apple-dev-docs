# withoutEscapingSlashes

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Specifies that the output doesn’t prefix slash characters with escape characters.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
static var withoutEscapingSlashes: JSONSerialization.WritingOptions { get }
```

```c
NSJSONWritingWithoutEscapingSlashes
```

## See Also

### Formatting JSON
- [static var fragmentsAllowed: JSONSerialization.WritingOptions](./fragmentsallowed.md)
  Specifies that the parser should allow top-level objects that aren’t arrays or dictionaries.
- [static var prettyPrinted: JSONSerialization.WritingOptions](./prettyprinted.md)
  Specifies that the output uses white space and indentation to make the resulting data more readable.
- [static var sortedKeys: JSONSerialization.WritingOptions](./sortedkeys.md)
  Specifies that the output sorts keys in lexicographic order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonserialization/writingoptions/withoutescapingslashes)*