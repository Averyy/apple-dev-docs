# unicodeScalars

**Framework**: Foundation  
**Kind**: property

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
var unicodeScalars: AttributedString.UnicodeScalarView { get set }
```

#### Discussion

Use this property when you want to split the attributed string by Unicode scalar instead of grapheme cluster. This is useful when you need to carefully control insertion points or render the content.

You can also use this property to mutate the attributed string, using [`RangeReplaceableCollection`](https://developer.apple.com/documentation/swift/rangereplaceablecollection) methods, such as `insert(_:at:)` and [`append(_:)`](https://developer.apple.com/documentation/swift/rangereplaceablecollection/append(_:)). Inserted characters inherit any attributes present at the insertion point.

## See Also

- [var characters: AttributedString.CharacterView](attributedstring/characters.md)
  The characters of the attributed string, as a view into the underlying string.
- [AttributedString.CharacterView](attributedstring/characterview.md)
  A view into the underlying storage of the attributed string, as Unicode characters.
- [AttributedString.UnicodeScalarView](attributedstring/unicodescalarview.md)
  A view into the underlying storage of the attributed string, as Unicode scalars.
- [var runs: AttributedString.Runs](attributedstring/runs-swift.property.md)
  The attributed runs of the attributed string, as a view into the underlying string.
- [AttributedString.Runs](attributedstring/runs-swift.struct.md)
  An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/unicodescalars)*