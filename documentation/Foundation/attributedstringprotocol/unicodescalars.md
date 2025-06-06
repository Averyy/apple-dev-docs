# unicodeScalars

**Framework**: Foundation  
**Kind**: property  
**Required**: Yes

The Unicode scalars of the attributed string, as a view into the underlying string.

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
var unicodeScalars: AttributedString.UnicodeScalarView { get }
```

#### Discussion

Use this property when you want to split the attributed string by Unicode scalar instead of grapheme cluster. This is useful when you need to carefully control insertion points or render the content.

You can also use this property to mutate the attributed string, using [`RangeReplaceableCollection`](https://developer.apple.com/documentation/Swift/RangeReplaceableCollection) methods, such as `insert(_:at:)` and [`append(_:)`](https://developer.apple.com/documentation/Swift/RangeReplaceableCollection/append(_:)). Inserted characters inherit any attributes present at the insertion point.

## See Also

- [var characters: AttributedString.CharacterView](attributedstringprotocol/characters.md)
  The characters of the attributed string, as a view into the underlying string.
- [var runs: AttributedString.Runs](attributedstringprotocol/runs.md)
  The attributed runs of the attributed string, as a view into the underlying string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringprotocol/unicodescalars)*