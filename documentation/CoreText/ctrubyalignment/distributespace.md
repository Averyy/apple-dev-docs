# CTRubyAlignment.distributeSpace

**Framework**: Core Text  
**Kind**: case

Distributes the ruby text evenly over the width of the base text, adding space before the first and after the last character.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case distributeSpace
```

#### Discussion

If the width of the ruby text is less than the width of the base text, Core Text evenly distributes the ruby text over the width of the base text. A certain amount of space, usually half of the intercharacter width of the ruby text, appears before the first and after the last character.

If the width of the base text is less than the width of the ruby text, Core Text similarly aligns the base text to the width of the ruby text.

## See Also

- [CTRubyAlignment.auto](ctrubyalignment/auto.md)
  Core Text automatically determines the alignment.
- [CTRubyAlignment.start](ctrubyalignment/start.md)
  Aligns the ruby text with the starting edge of the base text.
- [CTRubyAlignment.center](ctrubyalignment/center.md)
  Centers the ruby text within the width of the base text.
- [CTRubyAlignment.end](ctrubyalignment/end.md)
  Aligns the ruby text with the ending edge of the base text.
- [CTRubyAlignment.distributeLetter](ctrubyalignment/distributeletter.md)
  Distributes the ruby text evenly over the width of the base text, aligning the first and last characters of the ruby text with the first and last characters of the base text.
- [CTRubyAlignment.lineEdge](ctrubyalignment/lineedge.md)
  Aligns the ruby text to an adjacent line edge.
- [CTRubyAlignment.invalid](ctrubyalignment/invalid.md)
  The alignment is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrubyalignment/distributespace)*