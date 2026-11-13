# escapeCharacter

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

The character that precedes other characters, such as quotation marks, so that the parser interprets them as literal characters instead of special ones.

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
var escapeCharacter: Character { get }
```

## Discussion

Defaults to backslash(`\`).

## See Also

### Handling quotes and escapes
- [var usesQuoting: Bool](./usesquoting.md)
  A Boolean value that indicates whether to enable quoting.
- [var usesEscaping: Bool](./usesescaping.md)
  A Boolean value that indicates whether to enable escaping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvreadingoptions/escapecharacter)*