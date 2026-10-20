# CTRubyAlignment.lineEdge

**Framework**: Core Text  
**Kind**: case  
**Role**: Case

Aligns the ruby text to an adjacent line edge.

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
case lineEdge
```

```c
kCTRubyAlignmentLineEdge
```

#### Discussion

If the ruby text is adjacent to a line edge, Core Text aligns the end of the ruby text adjacent to the line edge to that line edge. This only applies if the width of the ruby text is greater than the width of the base text; otherwise, the alignment is [`CTRubyAlignment.auto`](./auto.md).

If the ruby text isn’t adjacent to a line edge, the alignment is [`CTRubyAlignment.auto`](./auto.md).

## See Also

### Constants
- [CTRubyAlignment.auto](./auto.md)
  Core Text automatically determines the alignment.
- [CTRubyAlignment.start](./start.md)
  Aligns the ruby text with the starting edge of the base text.
- [CTRubyAlignment.center](./center.md)
  Centers the ruby text within the width of the base text.
- [CTRubyAlignment.end](./end.md)
  Aligns the ruby text with the ending edge of the base text.
- [CTRubyAlignment.distributeLetter](./distributeletter.md)
  Distributes the ruby text evenly over the width of the base text, aligning the first and last characters of the ruby text with the first and last characters of the base text.
- [CTRubyAlignment.distributeSpace](./distributespace.md)
  Distributes the ruby text evenly over the width of the base text, adding space before the first and after the last character.
- [CTRubyAlignment.invalid](./invalid.md)
  The alignment is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrubyalignment/lineedge)*