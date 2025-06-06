# characters

**Framework**: Foundation  
**Kind**: property  
**Required**: Yes

The characters of the attributed string, as a view into the underlying string.

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
var characters: AttributedString.CharacterView { get }
```

#### Discussion

Use the [`characters`](attributedstringprotocol/characters.md) view when you want to look for specific string content. You can then use the resulting ranges to set attributes for specific parts of the [`AttributedString`](attributedstring.md) or [`AttributedSubstring`](attributedsubstring.md).

You can also use this property to mutate the attributed string, using [`RangeReplaceableCollection`](https://developer.apple.com/documentation/Swift/RangeReplaceableCollection) methods, such as `insert(_:at:)` and [`append(_:)`](https://developer.apple.com/documentation/Swift/RangeReplaceableCollection/append(_:)). Inserted characters inherit any attributes present at the insertion point.

## See Also

- [var unicodeScalars: AttributedString.UnicodeScalarView](attributedstringprotocol/unicodescalars.md)
  The Unicode scalars of the attributed string, as a view into the underlying string.
- [var runs: AttributedString.Runs](attributedstringprotocol/runs.md)
  The attributed runs of the attributed string, as a view into the underlying string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringprotocol/characters)*