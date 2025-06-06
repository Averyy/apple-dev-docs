# inverted

**Framework**: RegexBuilder  
**Kind**: property

The inverse of this anchor, which matches at every position that this anchor does not.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
var inverted: Anchor { get }
```

#### Discussion

For the [`wordBoundary`](anchor/wordboundary.md) and [`textSegmentBoundary`](anchor/textsegmentboundary.md) anchors, the inverted version corresponds to `\B` and `\Y`, respectively.


---

*[View on Apple Developer](https://developer.apple.com/documentation/regexbuilder/anchor/inverted)*