# characters

**Framework**: Foundation  
**Kind**: property

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

## See Also

- [AttributedString.CharacterView](attributedstring/characterview.md)
  A view into the underlying storage of the attributed string, as Unicode characters.
- [var unicodeScalars: AttributedString.UnicodeScalarView](attributedsubstring/unicodescalars.md)
  The Unicode scalars of the attributed string, as a view into the underlying string.
- [AttributedString.UnicodeScalarView](attributedstring/unicodescalarview.md)
  A view into the underlying storage of the attributed string, as Unicode scalars.
- [var runs: AttributedString.Runs](attributedsubstring/runs.md)
  The attributed runs of the attributed string, as a view into the underlying string.
- [AttributedString.Runs](attributedstring/runs-swift.struct.md)
  An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedsubstring/characters)*