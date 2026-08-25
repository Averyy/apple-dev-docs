# AVTextStyleRule

**Framework**: AVFoundation  
**Kind**: class

An object that represents the text styling rules to apply to a media item’s textual content.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class AVTextStyleRule
```

#### Overview

You use text style objects to format subtitles, closed captions, and other text-related content of the item. The system applies these rules to all or part of the text of the media item.

## Topics

### Creating and initializing style rules
- [class func textStyleRules(fromPropertyList: Any) -> [AVTextStyleRule]?](avtextstylerule/textstylerules(frompropertylist:).md)
  Creates an array of text style rule objects from the specified property-list object.
- [convenience init?(textMarkupAttributes: [String : Any])](avtextstylerule/init(textmarkupattributes:).md)
  Creates a text style rule object with the specified style attributes.
- [init?(textMarkupAttributes: [String : Any], textSelector: String?)](avtextstylerule/init(textmarkupattributes:textselector:).md)
  Creates a text style rule object with the specified style attributes and text range information.
### Accessing the style attributes
- [var textMarkupAttributes: [String : Any]](avtextstylerule/textmarkupattributes.md)
  A dictionary of text style attributes to apply to the text.
- [var textSelector: String?](avtextstylerule/textselector.md)
  A string that identifies the text the style attributes apply to.
### Exporting the style rules
- [class func propertyList(for: [AVTextStyleRule]) -> Any](avtextstylerule/propertylist(for:).md)
  Converts one or more text style rules into a serializable property list object.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [var textStyleRules: [AVTextStyleRule]?](avplayeritem/textstylerules.md)
  An array of text style rules that specify the formatting and presentation of Web Video Text Tracks (WebVTT) subtitles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtextstylerule)*