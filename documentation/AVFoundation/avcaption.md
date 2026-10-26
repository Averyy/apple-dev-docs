# AVCaption

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVCaption : NSObject
```

#### Overview

A caption contains a cue, which is a single sentence or paragraph of text for a time range in the video timeline. Within the active range, the caption may animate (for example, Karaoke lyrics) by rolling-up, changing visibility, or using other dynamic styling.

## Topics

### Creating a caption
- [init(String, timeRange: CMTimeRange)](./avcaption/init%28_,timerange%29.md)
  Creates a caption that contains text and a time range.
### Accessing text and timing
- [var text: String](./avcaption/text.md)
  The caption text.
- [var timeRange: CMTimeRange](./avcaption/timerange.md)
  The time range over which the system presents the caption.
### Accessing the region
- [var region: AVCaptionRegion?](./avcaption/region.md)
  The region in which the caption exists.
### Accessing font styles
- [func fontStyle(at: String.Index) -> (AVCaption.FontStyle, Range<String.Index>)](./avcaption/fontstyle%28at%29.md)
  Returns the font style and range at the index position.
- [AVCaption.FontStyle](./avcaption/fontstyle.md)
  Font styles for caption text.
- [func fontWeight(at: String.Index) -> (AVCaption.FontWeight, Range<String.Index>)](./avcaption/fontweight%28at%29.md)
  Returns the font weight and range at the index position.
- [AVCaption.FontWeight](./avcaption/fontweight.md)
  Font weights for a caption.
- [func decoration(at: String.Index) -> (AVCaption.Decoration, Range<String.Index>)](./avcaption/decoration%28at%29.md)
  Returns the text decoration at the index position.
- [AVCaption.Decoration](./avcaption/decoration.md)
  Text decorations for caption text.
- [- fontStyleAtIndex:range:](./avcaption/fontstyleatindex_range_.md)
  Returns the font style and range at the index position.
- [- fontWeightAtIndex:range:](./avcaption/fontweightatindex_range_.md)
  Returns the font weight and range at the index position.
- [- decorationAtIndex:range:](./avcaption/decorationatindex_range_.md)
  Returns the text decoration at the index position.
### Accessing colors
- [func textColor(at: String.Index) -> (CGColor?, Range<String.Index>)](./avcaption/textcolor%28at%29.md)
  Returns the text color at the index position.
- [func backgroundColor(at: String.Index) -> (CGColor?, Range<String.Index>)](./avcaption/backgroundcolor%28at%29.md)
  Returns the background color at the index position.
- [- textColorAtIndex:range:](./avcaption/textcoloratindex_range_.md)
  Returns the text color at the index position.
- [- backgroundColorAtIndex:range:](./avcaption/backgroundcoloratindex_range_.md)
  Returns the background color at the index position.
### Accessing alignment
- [var textAlignment: AVCaption.TextAlignment](./avcaption/textalignment-swift.property.md)
  The alignment for the caption text.
- [AVCaption.TextAlignment](./avcaption/textalignment-swift.enum.md)
  Text alignment options for a caption.
### Accessing animation
- [var animation: AVCaption.Animation](./avcaption/animation-swift.property.md)
  The animation that the system applies to this caption.
- [AVCaption.Animation](./avcaption/animation-swift.enum.md)
  Animation options for a caption.
### Accessing advanced typography
- [func ruby(at: String.Index) -> (AVCaption.Ruby?, Range<String.Index>)](./avcaption/ruby%28at%29.md)
  Returns the ruby text at the index position.
- [AVCaption.Ruby](./avcaption/ruby.md)
  An object that presents ruby characters.
- [func textCombine(at: String.Index) -> (AVCaption.TextCombine, Range<String.Index>)](./avcaption/textcombine%28at%29.md)
  Returns the text combine at the index position.
- [AVCaption.TextCombine](./avcaption/textcombine.md)
  The caption’s supported rendering policy options.
- [- rubyAtIndex:range:](./avcaption/rubyatindex_range_.md)
  Returns the ruby text at the index position.
- [- textCombineAtIndex:range:](./avcaption/textcombineatindex_range_.md)
  Returns the text combine at the index position.
### Initializers
- [init?(coder: NSCoder)](./avcaption/init%28coder%29.md)
- [init(text: String, timeRange: CMTimeRange)](./avcaption/init%28text,timerange%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [AVMutableCaption](./avmutablecaption.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSMutableCopying](../Foundation/nsmutablecopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Captions
- [class AVMutableCaption](./avmutablecaption.md)
  A mutable caption subclass that you use to create new captions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaption)*