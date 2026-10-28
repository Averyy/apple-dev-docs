# init(textMarkupAttributes:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

Creates a text style rule object with the specified style attributes.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
convenience init?(textMarkupAttributes: [String : Any] = [:])
```

```objc
- (instancetype) initWithTextMarkupAttributes:(NSDictionary<NSString *,id> *) textMarkupAttributes;
```

## Return Value

A text style rule object initialized with the specified attributes.

## Discussion

This method sets the [`textSelector`](./textselector.md) property of the style object to `nil`, which causes the rules to be applied to all of the text in the media item.

## Parameters

- `textMarkupAttributes`: A dictionary of style attributes. For a list of supported keys and values that you can include in this dictionary, see `CMTextMarkup.h`.

## See Also

### Creating and initializing style rules
- [class func textStyleRules(fromPropertyList: Any) -> [AVTextStyleRule]?](./textstylerules%28frompropertylist%29.md)
  Creates an array of text style rule objects from the specified property-list object.
- [init?(textMarkupAttributes: [String : Any], textSelector: String?)](./init%28textmarkupattributes,textselector%29.md)
  Creates a text style rule object with the specified style attributes and text range information.
- [+ textStyleRuleWithTextMarkupAttributes:](./textstylerulewithtextmarkupattributes_.md)
  Creates a new text style rule object using the style attributes in the specified dictionary.
- [+ textStyleRuleWithTextMarkupAttributes:textSelector:](./textstylerulewithtextmarkupattributes_textselector_.md)
  Creates a new text style rule object using the specified style attributes and text range information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtextstylerule/init(textmarkupattributes:))*