# range

**Framework**: DataDetection  
**Kind**: property

The range of characters in the original text corresponding to the match.

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
let range: Range<String.Index>?
```

#### Discussion

Use this range to add visual highlighting or interactive UI controls to the displayed text.

To extract semantic information from a match, examine its details properties.

> **Note**: Don’t use this range to infer semantic information from the matched string. Some values might be more complex to interpret than a direct usage of the matched string and may need interpretation, for example, a phone number with a spelled-out extension, such as “(415) 555-1212 ext. 9876”.

## See Also

- [let details: DataDetector.Match.SemanticDetails](datadetector/match/details.md)
  A property that contains the type and semantic data found in a match.
- [let preferredHighlightStyle: DataDetector.Match.HighlightStyle](datadetector/match/preferredhighlightstyle.md)
  A value that suggests a highlight style for a match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/datadetection/datadetector/match/range)*