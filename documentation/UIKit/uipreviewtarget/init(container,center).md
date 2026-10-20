# init(container:center:)

**Framework**: UIKit  
**Kind**: init  
**Role**: Initializer

Creates a preview target object using the specified container view and center point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
convenience init(container: UIView, center: CGPoint)
```

```objc
- (instancetype) initWithContainer:(UIView *) container center:(CGPoint) center;
```

#### Return Value

A new preview target object with the specified container and configuration data.

## Parameters

- `container`: The container for the view being animated. This view must be in a window.
- `center`: The point in `container` at which to place the center of the view being animated. Specify this point in the coordinate system of `container`.

## See Also

### Creating a preview target object
- [init(container: UIView, center: CGPoint, transform: CGAffineTransform)](./init%28container,center,transform%29.md)
  Creates a preview target object using the specified container view and configuration details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewtarget/init(container:center:))*