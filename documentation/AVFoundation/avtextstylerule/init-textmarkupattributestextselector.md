# init(textMarkupAttributes:textSelector:)

**Framework**: AVFoundation  
**Kind**: init

Creates a text style rule object with the specified style attributes and text range information.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init?(textMarkupAttributes: [String : Any] = [:], textSelector: String?)
```

#### Return Value

A text style rule object initialized with the specified attributes and range information.

## Parameters

- `textMarkupAttributes`: A dictionary of style attributes. For a list of supported keys and values that you can include in this dictionary, see  .
- `textSelector`: A string contains an identifier for the ranges of text to which the style attributes should be applied. Eligible identifiers are determined by the media format and its corresponding text content. For example, the string could contain the CSS selectors used by the corresponding text in Web Video Text Tracks (WebVTT) markup. Specify   if you want the style attributes to apply to all text in the item.

## See Also

- [class func textStyleRules(fromPropertyList: Any) -> [AVTextStyleRule]?](avtextstylerule/textstylerules(frompropertylist:).md)
  Creates an array of text style rule objects from the specified property-list object.
- [convenience init?(textMarkupAttributes: [String : Any])](avtextstylerule/init(textmarkupattributes:).md)
  Creates a text style rule object with the specified style attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtextstylerule/init(textmarkupattributes:textselector:))*