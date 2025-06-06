# index(_:offsetByRuns:)

**Framework**: Foundation  
**Kind**: method

Returns the position of the run offset a given number of runs from a given string index.

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
func index(_ i: AttributedString.Index, offsetByRuns distance: Int) -> AttributedString.Index
```

#### Return Value

The position of the run offset `distance` runs from position `i`.

## Parameters

- `i`: The index of a position in the string.
- `distance`: The number of runs to advance by.

## See Also

- [var startIndex: AttributedString.Index](attributedstringprotocol/startindex.md)
  The position of the first character in a nonempty attributed string.
- [var endIndex: AttributedString.Index](attributedstringprotocol/endindex.md)
  A string’s past-the-end position — the position one greater than the last valid subscript argument.
- [func index(AttributedString.Index, offsetByCharacters: Int) -> AttributedString.Index](attributedstringprotocol/index(_:offsetbycharacters:).md)
  Returns the position of the character offset a given distance, measured in characters, from a given string index.
- [func index(AttributedString.Index, offsetByUnicodeScalars: Int) -> AttributedString.Index](attributedstringprotocol/index(_:offsetbyunicodescalars:).md)
  Returns the position of the Unicode scalar offset a given distance, measured in Unicode scalars, from a given string index.
- [func index(afterCharacter: AttributedString.Index) -> AttributedString.Index](attributedstringprotocol/index(aftercharacter:).md)
  Returns the position of the character immediately after another charcter indicated by an index.
- [func index(afterRun: AttributedString.Index) -> AttributedString.Index](attributedstringprotocol/index(afterrun:).md)
  Returns the position of the run immediately after a run indicated by an index.
- [func index(afterUnicodeScalar: AttributedString.Index) -> AttributedString.Index](attributedstringprotocol/index(afterunicodescalar:).md)
  Returns the position of the Unicode scalar immediately after a Unicode scalar indicated by an index.
- [func index(beforeCharacter: AttributedString.Index) -> AttributedString.Index](attributedstringprotocol/index(beforecharacter:).md)
  Returns the position of the character immediately before another charcter indicated by an index.
- [func index(beforeRun: AttributedString.Index) -> AttributedString.Index](attributedstringprotocol/index(beforerun:).md)
  Returns the position of the run immediately before a run indicated by an index.
- [func index(beforeUnicodeScalar: AttributedString.Index) -> AttributedString.Index](attributedstringprotocol/index(beforeunicodescalar:).md)
  Returns the position of the Unicode scalar immediately before a Unicode scalar indicated by an index.
- [AttributedString.Index](attributedstring/index.md)
  A type that represents the position of a character or code unit within an attributed string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringprotocol/index(_:offsetbyruns:))*