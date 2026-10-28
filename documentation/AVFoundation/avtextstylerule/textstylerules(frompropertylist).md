# textStyleRules(fromPropertyList:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Creates an array of text style rule objects from the specified property-list object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
class func textStyleRules(fromPropertyList plist: Any) -> [AVTextStyleRule]?
```

```objc
+ (NSArray<AVTextStyleRule *> *) textStyleRulesFromPropertyList:(id) plist;
```

## Return Value

An array of `AVTextStyleRule` objects corresponding to the style information in the property-list object.

## Discussion

Use this method to create new text style rule objects based on data you previously converted to a property-list format using the [`propertyList(for:)`](./propertylist%28for%29.md) class method.

## Parameters

- `plist`: A property-list object containing the text style data.

## See Also

### Creating and initializing style rules
- [convenience init?(textMarkupAttributes: [String : Any])](./init%28textmarkupattributes%29.md)
  Creates a text style rule object with the specified style attributes.
- [init?(textMarkupAttributes: [String : Any], textSelector: String?)](./init%28textmarkupattributes,textselector%29.md)
  Creates a text style rule object with the specified style attributes and text range information.
- [+ textStyleRuleWithTextMarkupAttributes:](./textstylerulewithtextmarkupattributes_.md)
  Creates a new text style rule object using the style attributes in the specified dictionary.
- [+ textStyleRuleWithTextMarkupAttributes:textSelector:](./textstylerulewithtextmarkupattributes_textselector_.md)
  Creates a new text style rule object using the specified style attributes and text range information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtextstylerule/textstylerules(frompropertylist:))*