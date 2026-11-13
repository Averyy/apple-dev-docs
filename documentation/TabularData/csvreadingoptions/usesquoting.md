# usesQuoting

**Framework**: TabularData  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether to enable quoting.

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
var usesQuoting: Bool
```

## Discussion

When `true`, the contents of a quoted field can contain special characters, such as the field delimiter and newlines. Defaults to `true`.

## See Also

### Handling quotes and escapes
- [var usesEscaping: Bool](./usesescaping.md)
  A Boolean value that indicates whether to enable escaping.
- [var escapeCharacter: Character](./escapecharacter.md)
  The character that precedes other characters, such as quotation marks, so that the parser interprets them as literal characters instead of special ones.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabulardata/csvreadingoptions/usesquoting)*