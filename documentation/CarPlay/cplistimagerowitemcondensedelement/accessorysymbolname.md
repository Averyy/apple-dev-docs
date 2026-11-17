# accessorySymbolName

**Framework**: CarPlay  
**Kind**: property  
**Role**: Instance Property

The name of an image to display at the trailing edge of the element.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var accessorySymbolName: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * accessorySymbolName;
```

## Discussion

This property contains the name of an SF Symbol or the name of a custom image resource in your app’s main bundle. If the value of this property is `nil`, or if the system can’t find the image using the provided name, the element doesn’t display the image.

## See Also

### Getting the element’s content
- [var title: String](./title.md)
  The primary text for the element.
- [var subtitle: String?](./subtitle.md)
  The secondary text for the element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcondensedelement/accessorysymbolname)*