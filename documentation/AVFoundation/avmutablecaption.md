# AVMutableCaption

**Framework**: AVFoundation  
**Kind**: class

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

## Topics

### Configuring text and timing
- [var text: String](avmutablecaption/text.md)
  The caption text.
- [var timeRange: CMTimeRange](avmutablecaption/timerange.md)
  The time range over which the system presents the caption.
### Configuring the region
- [var region: AVCaptionRegion](avmutablecaption/region.md)
  The region in which the caption exists.
### Configuring font styles
- [AVCaption.FontStyle](avcaption/fontstyle.md)
  Font styles for caption text.
- [func setFontStyle(AVCaption.FontStyle, in: NSRange)](avmutablecaption/setfontstyle(_:in:).md)
  Sets the font style for a range of text.
- [func removeFontStyle(in: NSRange)](avmutablecaption/removefontstyle(in:).md)
  Removes a font style from a range of text.
- [AVCaption.FontWeight](avcaption/fontweight.md)
  Font weights for a caption.
- [func setFontWeight(AVCaption.FontWeight, in: NSRange)](avmutablecaption/setfontweight(_:in:).md)
  Sets the font weight for a range of text.
- [func removeFontWeight(in: NSRange)](avmutablecaption/removefontweight(in:).md)
  Removes a font weight from a range of text.
- [AVCaption.Decoration](avcaption/decoration.md)
  Text decorations for caption text.
- [func setDecoration(AVCaption.Decoration, in: NSRange)](avmutablecaption/setdecoration(_:in:).md)
  Sets a decoration for a range of text.
- [func removeDecoration(in: NSRange)](avmutablecaption/removedecoration(in:).md)
  Removes a decoration from a range of text.
### Configuring colors
- [func setTextColor(CGColor, in: NSRange)](avmutablecaption/settextcolor(_:in:).md)
  Sets the text color for a range of text.
- [func removeTextColor(in: NSRange)](avmutablecaption/removetextcolor(in:).md)
  Removes the text color for a range of text.
- [func setBackgroundColor(CGColor, in: NSRange)](avmutablecaption/setbackgroundcolor(_:in:).md)
  Sets the background color for a range of text.
- [func removeBackgroundColor(in: NSRange)](avmutablecaption/removebackgroundcolor(in:).md)
  Removes a background color from a range of text.
### Configuring alignment
- [var textAlignment: AVCaption.TextAlignment](avmutablecaption/textalignment.md)
  The alignment of the caption text.
- [AVCaption.TextAlignment](avcaption/textalignment-swift.enum.md)
  Text alignment options for a caption.
### Configuring animation
- [var animation: AVCaption.Animation](avmutablecaption/animation.md)
  Animations to apply to the caption text.
- [AVCaption.Animation](avcaption/animation-swift.enum.md)
  Animation options for a caption.
### Configuring advanced typography
- [AVCaption.Ruby](avcaption/ruby.md)
  An object that presents ruby characters.
- [func setRuby(AVCaption.Ruby, in: NSRange)](avmutablecaption/setruby(_:in:).md)
  Sets ruby text for a range.
- [func removeRuby(in: NSRange)](avmutablecaption/removeruby(in:).md)
  Removes ruby text from a range.
- [AVCaption.TextCombine](avcaption/textcombine.md)
  The caption’s supported rendering policy options.
- [func setTextCombine(AVCaption.TextCombine, in: NSRange)](avmutablecaption/settextcombine(_:in:).md)
  Sets text combine for a range.
- [func removeTextCombine(in: NSRange)](avmutablecaption/removetextcombine(in:).md)
  Removes text combine from a range.

## Relationships

### Inherits From
- [AVCaption](avcaption.md)
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

- [class AVCaption](avcaption.md)
  An object that represents text to present over a time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutablecaption)*