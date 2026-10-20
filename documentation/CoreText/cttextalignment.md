# CTTextAlignment

**Framework**: Core Text  
**Kind**: enum  
**Role**: Enumeration

Constants that specify text alignment.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum CTTextAlignment
```

```c
enum CTTextAlignment : uint8_t;
```

## Topics

### Constants
- [CTTextAlignment.left](./cttextalignment/left.md)
  Text is visually left-aligned.
- [CTTextAlignment.right](./cttextalignment/right.md)
  Text is visually right-aligned.
- [CTTextAlignment.center](./cttextalignment/center.md)
  Text is visually center-aligned.
- [CTTextAlignment.justified](./cttextalignment/justified.md)
  Text is fully justified.
- [CTTextAlignment.natural](./cttextalignment/natural.md)
  Text uses the natural alignment of the text’s script.
### Initializers
- [init(NSTextAlignment)](./cttextalignment/init%28_%29.md)
  Converts a UIKit text alignment constant value to the matching constant value that Core Text uses.
- [init?(rawValue: UInt8)](./cttextalignment/init%28rawvalue%29.md)
### Deprecated
- [static var kCTLeftTextAlignment: CTTextAlignment](./cttextalignment/kctlefttextalignment.md)
  Text is visually left-aligned.
- [static var kCTRightTextAlignment: CTTextAlignment](./cttextalignment/kctrighttextalignment.md)
  Text is visually right-aligned.
- [static var kCTCenterTextAlignment: CTTextAlignment](./cttextalignment/kctcentertextalignment.md)
  Text is visually center-aligned.
- [static var kCTJustifiedTextAlignment: CTTextAlignment](./cttextalignment/kctjustifiedtextalignment.md)
  Text is fully justified.
- [static var kCTNaturalTextAlignment: CTTextAlignment](./cttextalignment/kctnaturaltextalignment.md)
  Text uses the natural alignment of the text’s script.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Constants
- [enum CTLineBreakMode](./ctlinebreakmode.md)
  These constants specify what happens when a line is too long for its frame.
- [enum CTWritingDirection](./ctwritingdirection.md)
  These constants specify the writing direction.
- [enum CTParagraphStyleSpecifier](./ctparagraphstylespecifier.md)
  Constants used to query and modify a paragraph style object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/cttextalignment)*