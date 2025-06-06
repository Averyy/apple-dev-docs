# init(textMarkupAttributes:)

**Framework**: AVFoundation  
**Kind**: init

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

#### Return Value

A text style rule object initialized with the specified attributes.

#### Discussion

This method sets the [`textSelector`](avtextstylerule/textselector.md) property of the style object to `nil`, which causes the rules to be applied to all of the text in the media item.

## Parameters

- `textMarkupAttributes`: A dictionary of style attributes. For a list of supported keys and values that you can include in this dictionary, see  .

## See Also

- [class func textStyleRules(fromPropertyList: Any) -> [AVTextStyleRule]?](avtextstylerule/textstylerules(frompropertylist:).md)
  Creates an array of text style rule objects from the specified property-list object.
- [init?(textMarkupAttributes: [String : Any], textSelector: String?)](avtextstylerule/init(textmarkupattributes:textselector:).md)
  Creates a text style rule object with the specified style attributes and text range information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avtextstylerule/init(textmarkupattributes:))*