# textStyleRules(fromPropertyList:)

**Framework**: AVFoundation  
**Kind**: method

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

#### Return Value

An array of `AVTextStyleRule` objects corresponding to the style information in the property-list object.

#### Discussion

Use this method to create new text style rule objects based on data you previously converted to a property-list format using the [`propertyList(for:)`](avtextstylerule/propertylist(for:).md) class method.

## Parameters

- `plist`: A property-list object containing the text style data.

## See Also

- [convenience init?(textMarkupAttributes: [String : Any])](avtextstylerule/init(textmarkupattributes:).md)
  Creates a text style rule object with the specified style attributes.
- [init?(textMarkupAttributes: [String : Any], textSelector: String?)](avtextstylerule/init(textmarkupattributes:textselector:).md)
  Creates a text style rule object with the specified style attributes and text range information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtextstylerule/textstylerules(frompropertylist:))*