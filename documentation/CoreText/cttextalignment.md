# CTTextAlignment

**Framework**: Core Text  
**Kind**: enum

Constants that specify text alignment.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum CTTextAlignment
```

## Topics

### Constants
- [CTTextAlignment.left](cttextalignment/left.md)
  Text is visually left-aligned.
- [CTTextAlignment.right](cttextalignment/right.md)
  Text is visually right-aligned.
- [CTTextAlignment.center](cttextalignment/center.md)
  Text is visually center-aligned.
- [CTTextAlignment.justified](cttextalignment/justified.md)
  Text is fully justified.
- [CTTextAlignment.natural](cttextalignment/natural.md)
  Text uses the natural alignment of the text’s script.
### Initializers
- [init(NSTextAlignment)](cttextalignment/init(_:).md)
  Converts a UIKit text alignment constant value to the matching constant value that Core Text uses.
- [init?(rawValue: UInt8)](cttextalignment/init(rawvalue:).md)
### Deprecated
- [static var kCTLeftTextAlignment: CTTextAlignment](cttextalignment/kctlefttextalignment.md)
  Text is visually left-aligned.
- [static var kCTRightTextAlignment: CTTextAlignment](cttextalignment/kctrighttextalignment.md)
  Text is visually right-aligned.
- [static var kCTCenterTextAlignment: CTTextAlignment](cttextalignment/kctcentertextalignment.md)
  Text is visually center-aligned.
- [static var kCTJustifiedTextAlignment: CTTextAlignment](cttextalignment/kctjustifiedtextalignment.md)
  Text is fully justified.
- [static var kCTNaturalTextAlignment: CTTextAlignment](cttextalignment/kctnaturaltextalignment.md)
  Text uses the natural alignment of the text’s script.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum CTLineBreakMode](ctlinebreakmode.md)
  These constants specify what happens when a line is too long for its frame.
- [enum CTWritingDirection](ctwritingdirection.md)
  These constants specify the writing direction.
- [enum CTParagraphStyleSpecifier](ctparagraphstylespecifier.md)
  Constants used to query and modify a paragraph style object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttextalignment)*