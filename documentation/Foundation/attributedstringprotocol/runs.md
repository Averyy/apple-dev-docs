# runs

**Framework**: Foundation  
**Kind**: property  
**Required**: Yes

The attributed runs of the attributed string, as a view into the underlying string.

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
var runs: AttributedString.Runs { get }
```

#### Discussion

Runs begin and end when the attributes for the characters change. Use this property to iterate over the runs with `for`-`in` syntax.

## See Also

- [var characters: AttributedString.CharacterView](attributedstringprotocol/characters.md)
  The characters of the attributed string, as a view into the underlying string.
- [var unicodeScalars: AttributedString.UnicodeScalarView](attributedstringprotocol/unicodescalars.md)
  The Unicode scalars of the attributed string, as a view into the underlying string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstringprotocol/runs)*