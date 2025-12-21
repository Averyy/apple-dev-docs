# DataDetector.Match

**Framework**: DataDetection  
**Kind**: struct

A representation of a match that includes common properties and an enumeration that represents the match type and its specific semantic components.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Match
```

## Topics

### Match details
- [let details: DataDetector.Match.SemanticDetails](datadetector/match/details.md)
  A property that contains the type and semantic data found in a match.
- [let preferredHighlightStyle: DataDetector.Match.HighlightStyle](datadetector/match/preferredhighlightstyle.md)
  A value that suggests a highlight style for a match.
- [let range: Range<String.Index>?](datadetector/match/range.md)
  The range of characters in the original text corresponding to the match.
### Values that describe highlighting and semantic details of matches
- [DataDetector.Match.HighlightStyle](datadetector/match/highlightstyle.md)
  Values that suggest how to style a highlighted item.
- [DataDetector.Match.SemanticDetails](datadetector/match/semanticdetails.md)
  An enumeration of types of matches returned by the scanner.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [DataDetector.MatchType](datadetector/matchtype.md)
  A set of types of matches that the system can find in a string.
- [DataDetector.Options](datadetector/options.md)
  A set of options you can use to refine the behavior of text scanning, and better interpret the semantic domain of the matches.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match)*