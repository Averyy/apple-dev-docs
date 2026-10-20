# sortedKeys

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

Specifies that the output sorts keys in lexicographic order.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
static var sortedKeys: JSONSerialization.WritingOptions { get }
```

```c
NSJSONWritingSortedKeys
```

## See Also

### Formatting JSON
- [static var fragmentsAllowed: JSONSerialization.WritingOptions](./fragmentsallowed.md)
  Specifies that the parser should allow top-level objects that aren’t arrays or dictionaries.
- [static var prettyPrinted: JSONSerialization.WritingOptions](./prettyprinted.md)
  Specifies that the output uses white space and indentation to make the resulting data more readable.
- [static var withoutEscapingSlashes: JSONSerialization.WritingOptions](./withoutescapingslashes.md)
  Specifies that the output doesn’t prefix slash characters with escape characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/jsonserialization/writingoptions/sortedkeys)*