# AVCaption

**Framework**: AVFoundation  
**Kind**: class

An object that represents text to present over a time range.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVCaption
```

#### Overview

A caption contains a cue, which is a single sentence or paragraph of text for a time range in the video timeline. Within the active range, the caption may animate (for example, Karaoke lyrics) by rolling-up, changing visibility, or using other dynamic styling.

## Topics

### Creating a caption
- [init(String, timeRange: CMTimeRange)](avcaption/init(_:timerange:).md)
  Creates a caption that contains text and a time range.
### Accessing text and timing
- [var text: String](avcaption/text.md)
  The caption text.
- [var timeRange: CMTimeRange](avcaption/timerange.md)
  The time range over which the system presents the caption.
### Accessing the region
- [var region: AVCaptionRegion?](avcaption/region.md)
  The region in which the caption exists.
### Accessing font styles
- [func fontStyle(at: String.Index) -> (AVCaption.FontStyle, Range<String.Index>)](avcaption/fontstyle(at:).md)
  Returns the font style and range at the index position.
- [AVCaption.FontStyle](avcaption/fontstyle.md)
  Font styles for caption text.
- [func fontWeight(at: String.Index) -> (AVCaption.FontWeight, Range<String.Index>)](avcaption/fontweight(at:).md)
  Returns the font weight and range at the index position.
- [AVCaption.FontWeight](avcaption/fontweight.md)
  Font weights for a caption.
- [func decoration(at: String.Index) -> (AVCaption.Decoration, Range<String.Index>)](avcaption/decoration(at:).md)
  Returns the text decoration at the index position.
- [AVCaption.Decoration](avcaption/decoration.md)
  Text decorations for caption text.
### Accessing colors
- [func textColor(at: String.Index) -> (CGColor?, Range<String.Index>)](avcaption/textcolor(at:).md)
  Returns the text color at the index position.
- [func backgroundColor(at: String.Index) -> (CGColor?, Range<String.Index>)](avcaption/backgroundcolor(at:).md)
  Returns the background color at the index position.
### Accessing alignment
- [var textAlignment: AVCaption.TextAlignment](avcaption/textalignment-swift.property.md)
  The alignment for the caption text.
- [AVCaption.TextAlignment](avcaption/textalignment-swift.enum.md)
  Text alignment options for a caption.
### Accessing animation
- [var animation: AVCaption.Animation](avcaption/animation-swift.property.md)
  The animation that the system applies to this caption.
- [AVCaption.Animation](avcaption/animation-swift.enum.md)
  Animation options for a caption.
### Accessing advanced typography
- [func ruby(at: String.Index) -> (AVCaption.Ruby?, Range<String.Index>)](avcaption/ruby(at:).md)
  Returns the ruby text at the index position.
- [AVCaption.Ruby](avcaption/ruby.md)
  An object that presents ruby characters.
- [func textCombine(at: String.Index) -> (AVCaption.TextCombine, Range<String.Index>)](avcaption/textcombine(at:).md)
  Returns the text combine at the index position.
- [AVCaption.TextCombine](avcaption/textcombine.md)
  The caption’s supported rendering policy options.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [AVMutableCaption](avmutablecaption.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class AVMutableCaption](avmutablecaption.md)
  A mutable caption subclass that you use to create new captions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption)*