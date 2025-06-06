# CTRubyPosition.count

**Framework**: Core Text  
**Kind**: case

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

#### Discussion

When you create a ruby annotation using [`CTRubyAnnotationCreate(_:_:_:_:)`](ctrubyannotationcreate(_:_:_:_:).md), use this constant to allocate an array of [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString) texts that contains a sufficient number of elements for each [`CTRubyPosition`](ctrubyposition.md).

## See Also

- [CTRubyPosition.before](ctrubyposition/before.md)
  The ruby text is positioned before the base text, appearing above horizontal text and to the right of vertical text.
- [CTRubyPosition.after](ctrubyposition/after.md)
  The ruby text is positioned after the base text, appearing below horizontal text and to the left of vertical text.
- [CTRubyPosition.interCharacter](ctrubyposition/intercharacter.md)
  The ruby text is positioned to the right of the base text, regardless of whether it’s horizontal or vertical.
- [CTRubyPosition.inline](ctrubyposition/inline.md)
  The ruby text follows the base text with no special styling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctrubyposition/count)*