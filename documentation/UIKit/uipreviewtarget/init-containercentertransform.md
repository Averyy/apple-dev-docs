# init(container:center:transform:)

**Framework**: UIKit  
**Kind**: init

Creates a preview target object using the specified container view and configuration details.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
init(container: UIView, center: CGPoint, transform: CGAffineTransform)
```

#### Return Value

A new preview target object with the specified container and configuration data.

## Parameters

- `container`: The container for the view being animated. This view must be in a window.
- `center`: The point in   at which to place the center of the view being animated. Specify this point in the coordinate system of  .
- `transform`: An affine transform to apply to the view being animated. You might use this transform to scale or rotate the view.

## See Also

- [convenience init(container: UIView, center: CGPoint)](uipreviewtarget/init(container:center:).md)
  Creates a preview target object using the specified container view and center point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewtarget/init(container:center:transform:))*