# init(textMarkupAttributes:textSelector:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithTextMarkupAttributes:(NSDictionary<NSString *,id> *) textMarkupAttributes textSelector:(NSString *) textSelector;
```

#### Return Value

A text style rule object initialized with the specified attributes and range information.

## Parameters

- `textMarkupAttributes`: A dictionary of style attributes. For a list of supported keys and values that you can include in this dictionary, see `CMTextMarkup.h`.
- `textSelector`: A string contains an identifier for the ranges of text to which the style attributes should be applied. Eligible identifiers are determined by the media format and its corresponding text content. For example, the string could contain the CSS selectors used by the corresponding text in Web Video Text Tracks (WebVTT) markup. Specify `nil` if you want the style attributes to apply to all text in the item.

## See Also

### Creating and initializing style rules
- [class func textStyleRules(fromPropertyList: Any) -> [AVTextStyleRule]?](./textstylerules%28frompropertylist%29.md)
  Creates an array of text style rule objects from the specified property-list object.
- [convenience init?(textMarkupAttributes: [String : Any])](./init%28textmarkupattributes%29.md)
  Creates a text style rule object with the specified style attributes.
- [+ textStyleRuleWithTextMarkupAttributes:](./textstylerulewithtextmarkupattributes_.md)
  Creates a new text style rule object using the style attributes in the specified dictionary.
- [+ textStyleRuleWithTextMarkupAttributes:textSelector:](./textstylerulewithtextmarkupattributes_textselector_.md)
  Creates a new text style rule object using the specified style attributes and text range information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtextstylerule/init(textmarkupattributes:textselector:))*