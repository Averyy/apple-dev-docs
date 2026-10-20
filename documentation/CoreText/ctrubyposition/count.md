# CTRubyPosition.count

**Framework**: Core Text  
**Kind**: case  
**Role**: Case

A constant that accounts for all ruby positions during ruby annotation creation.

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
case count
```

```c
kCTRubyPositionCount
```

#### Discussion

When you create a ruby annotation using [`CTRubyAnnotationCreate(_:_:_:_:)`](../ctrubyannotationcreate%28_,_,_,_%29.md), use this constant to allocate an array of [`CFString`](../../CoreFoundation/cfstring.md) texts that contains a sufficient number of elements for each [`CTRubyPosition`](../ctrubyposition.md).

## See Also

### Constants
- [CTRubyPosition.before](./before.md)
  The ruby text is positioned before the base text, appearing above horizontal text and to the right of vertical text.
- [CTRubyPosition.after](./after.md)
  The ruby text is positioned after the base text, appearing below horizontal text and to the left of vertical text.
- [CTRubyPosition.interCharacter](./intercharacter.md)
  The ruby text is positioned to the right of the base text, regardless of whether it’s horizontal or vertical.
- [CTRubyPosition.inline](./inline.md)
  The ruby text follows the base text with no special styling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrubyposition/count)*