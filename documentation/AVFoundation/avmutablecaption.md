# AVMutableCaption

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

A mutable caption subclass that you use to create new captions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 15.0+
- macOS 12.0+

## Declaration

```swift
class AVMutableCaption
```

```objc
@interface AVMutableCaption : AVCaption
```

## Topics

### Configuring text and timing
- [var text: String](./avmutablecaption/text.md)
  The caption text.
- [var timeRange: CMTimeRange](./avmutablecaption/timerange.md)
  The time range over which the system presents the caption.
### Configuring the region
- [var region: AVCaptionRegion](./avmutablecaption/region.md)
  The region in which the caption exists.
### Configuring font styles
- [AVCaption.FontStyle](./avcaption/fontstyle.md)
  Font styles for caption text.
- [func setFontStyle(AVCaption.FontStyle, in: NSRange)](./avmutablecaption/setfontstyle%28_,in%29.md)
  Sets the font style for a range of text.
- [func removeFontStyle(in: NSRange)](./avmutablecaption/removefontstyle%28in%29.md)
  Removes a font style from a range of text.
- [AVCaption.FontWeight](./avcaption/fontweight.md)
  Font weights for a caption.
- [func setFontWeight(AVCaption.FontWeight, in: NSRange)](./avmutablecaption/setfontweight%28_,in%29.md)
  Sets the font weight for a range of text.
- [func removeFontWeight(in: NSRange)](./avmutablecaption/removefontweight%28in%29.md)
  Removes a font weight from a range of text.
- [AVCaption.Decoration](./avcaption/decoration.md)
  Text decorations for caption text.
- [func setDecoration(AVCaption.Decoration, in: NSRange)](./avmutablecaption/setdecoration%28_,in%29.md)
  Sets a decoration for a range of text.
- [func removeDecoration(in: NSRange)](./avmutablecaption/removedecoration%28in%29.md)
  Removes a decoration from a range of text.
- [- setFontStyle:inRange:](./avmutablecaption/setfontstyle_inrange_.md)
  Sets the font style for a range of text.
- [- removeFontStyleInRange:](./avmutablecaption/removefontstyleinrange_.md)
  Removes a font style from a range of text.
- [- setFontWeight:inRange:](./avmutablecaption/setfontweight_inrange_.md)
  Sets the font weight for a range of text.
- [- removeFontWeightInRange:](./avmutablecaption/removefontweightinrange_.md)
  Removes a font weight from a range of text.
- [- setDecoration:inRange:](./avmutablecaption/setdecoration_inrange_.md)
  Sets a decoration for a range of text.
- [- removeDecorationInRange:](./avmutablecaption/removedecorationinrange_.md)
  Removes a decoration from a range of text.
### Configuring colors
- [func setTextColor(CGColor, in: NSRange)](./avmutablecaption/settextcolor%28_,in%29.md)
  Sets the text color for a range of text.
- [func removeTextColor(in: NSRange)](./avmutablecaption/removetextcolor%28in%29.md)
  Removes the text color for a range of text.
- [func setBackgroundColor(CGColor, in: NSRange)](./avmutablecaption/setbackgroundcolor%28_,in%29.md)
  Sets the background color for a range of text.
- [func removeBackgroundColor(in: NSRange)](./avmutablecaption/removebackgroundcolor%28in%29.md)
  Removes a background color from a range of text.
- [- setTextColor:inRange:](./avmutablecaption/settextcolor_inrange_.md)
  Sets the text color for a range of text.
- [- removeTextColorInRange:](./avmutablecaption/removetextcolorinrange_.md)
  Removes the text color for a range of text.
- [- setBackgroundColor:inRange:](./avmutablecaption/setbackgroundcolor_inrange_.md)
  Sets the background color for a range of text.
- [- removeBackgroundColorInRange:](./avmutablecaption/removebackgroundcolorinrange_.md)
  Removes a background color from a range of text.
### Configuring alignment
- [var textAlignment: AVCaption.TextAlignment](./avmutablecaption/textalignment.md)
  The alignment of the caption text.
- [AVCaption.TextAlignment](./avcaption/textalignment-swift.enum.md)
  Text alignment options for a caption.
### Configuring animation
- [var animation: AVCaption.Animation](./avmutablecaption/animation.md)
  Animations to apply to the caption text.
- [AVCaption.Animation](./avcaption/animation-swift.enum.md)
  Animation options for a caption.
### Configuring advanced typography
- [AVCaption.Ruby](./avcaption/ruby.md)
  An object that presents ruby characters.
- [func setRuby(AVCaption.Ruby, in: NSRange)](./avmutablecaption/setruby%28_,in%29.md)
  Sets ruby text for a range.
- [func removeRuby(in: NSRange)](./avmutablecaption/removeruby%28in%29.md)
  Removes ruby text from a range.
- [AVCaption.TextCombine](./avcaption/textcombine.md)
  The caption’s supported rendering policy options.
- [func setTextCombine(AVCaption.TextCombine, in: NSRange)](./avmutablecaption/settextcombine%28_,in%29.md)
  Sets text combine for a range.
- [func removeTextCombine(in: NSRange)](./avmutablecaption/removetextcombine%28in%29.md)
  Removes text combine from a range.
- [- setRuby:inRange:](./avmutablecaption/setruby_inrange_.md)
  Sets ruby text for a range.
- [- removeRubyInRange:](./avmutablecaption/removerubyinrange_.md)
  Removes ruby text from a range.
- [- setTextCombine:inRange:](./avmutablecaption/settextcombine_inrange_.md)
  Sets text combine for a range.
- [- removeTextCombineInRange:](./avmutablecaption/removetextcombineinrange_.md)
  Removes text combine from a range of text.

## Relationships

### Inherits From
- [AVCaption](./avcaption.md)
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
- [class AVCaption](./avcaption.md)
  An object that represents text to present over a time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecaption)*