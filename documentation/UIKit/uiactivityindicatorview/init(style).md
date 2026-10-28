# init(style:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates an activity indicator.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
init(style: UIActivityIndicatorView.Style)
```

```objc
- (instancetype) initWithActivityIndicatorStyle:(UIActivityIndicatorViewStyle) style;
```

## Return Value

An initialized [`UIActivityIndicatorView`](../uiactivityindicatorview.md) object.

## Discussion

[`UIActivityIndicatorView`](../uiactivityindicatorview.md) sizes the returned instance according to the specified `style`. You can set and retrieve the style of an activity indicator through the [`style`](./style-swift.property.md) property.

## Parameters

- `style`: A constant that specifies the style of the object to be created. See [`UIActivityIndicatorView.Style`](./style-swift.enum.md) for descriptions of the style constants.

## See Also

### Creating an activity indicator
- [init(frame: CGRect)](./init%28frame%29.md)
  Creates an activity indicator with the specified frame rectangle.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Creates an activity indicator from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiactivityindicatorview/init(style:))*