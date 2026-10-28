# runs

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

Runs begin and end when the attributes for the characters change. Use this property to iterate over the runs with `for`-`in` syntax.

## See Also

### Accessing Views into the Attributed String
- [var characters: AttributedString.CharacterView](./characters.md)
  The characters of the attributed string, as a view into the underlying string.
- [AttributedString.CharacterView](./characterview.md)
  A view into the underlying storage of the attributed string, as Unicode characters.
- [var unicodeScalars: AttributedString.UnicodeScalarView](./unicodescalars.md)
  The Unicode scalars of the attributed string, as a view into the underlying string.
- [AttributedString.UnicodeScalarView](./unicodescalarview.md)
  A view into the underlying storage of the attributed string, as Unicode scalars.
- [AttributedString.Runs](./runs-swift.struct.md)
  An iterable view into segments of the attributed string, each of which indicates where a run of identical attributes begins or ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/attributedstring/runs-swift.property)*