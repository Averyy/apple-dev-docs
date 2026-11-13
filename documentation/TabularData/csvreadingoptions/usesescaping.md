# usesEscaping

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to enable escaping.

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
var usesEscaping: Bool
```

## Discussion

When `true`, you can escape special characters, such as the field delimiter, by prefixing them with the escape character, which is the backslash (`\`) by default. Defaults to `false`.

## See Also

### Handling quotes and escapes
- [var usesQuoting: Bool](./usesquoting.md)
  A Boolean value that indicates whether to enable quoting.
- [var escapeCharacter: Character](./escapecharacter.md)
  The character that precedes other characters, such as quotation marks, so that the parser interprets them as literal characters instead of special ones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvreadingoptions/usesescaping)*