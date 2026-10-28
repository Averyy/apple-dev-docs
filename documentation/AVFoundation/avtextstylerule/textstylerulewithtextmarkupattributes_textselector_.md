# textStyleRuleWithTextMarkupAttributes:textSelector:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Creates a new text style rule object using the specified style attributes and text range information.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
+ (AVTextStyleRule *) textStyleRuleWithTextMarkupAttributes:(NSDictionary<NSString *,id> *) textMarkupAttributes textSelector:(NSString *) textSelector;
```

## Return Value

A new text style rule object with the specified attributes and range information.

## Parameters

- `textMarkupAttributes`: A dictionary of style attributes. For a list of supported keys and values that you can include in this dictionary, see `CMTextMarkup.h`.
- `textSelector`: A string contains an identifier for the ranges of text to which the style attributes should be applied. Eligible identifiers are determined by the media format and its corresponding text content. For example, the string could contain the CSS selectors used by the corresponding text in Web Video Text Tracks (WebVTT) markup. Specify `nil` if you want the style attributes to apply to all text in the item.

## See Also

### Creating and initializing style rules
- [class func textStyleRules(fromPropertyList: Any) -> [AVTextStyleRule]?](./textstylerules%28frompropertylist%29.md)
  Creates an array of text style rule objects from the specified property-list object.
- [+ textStyleRuleWithTextMarkupAttributes:](./textstylerulewithtextmarkupattributes_.md)
  Creates a new text style rule object using the style attributes in the specified dictionary.
- [convenience init?(textMarkupAttributes: [String : Any])](./init%28textmarkupattributes%29.md)
  Creates a text style rule object with the specified style attributes.
- [init?(textMarkupAttributes: [String : Any], textSelector: String?)](./init%28textmarkupattributes,textselector%29.md)
  Creates a text style rule object with the specified style attributes and text range information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtextstylerule/textstylerulewithtextmarkupattributes:textselector:)*