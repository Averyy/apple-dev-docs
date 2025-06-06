# init(container:center:)

**Framework**: UIKit  
**Kind**: init

Creates a preview target object using the specified container view and center point.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(container: UIView, center: CGPoint)
```

#### Return Value

A new preview target object with the specified container and configuration data.

## Parameters

- `container`: The container for the view being animated. This view must be in a window.
- `center`: The point in   at which to place the center of the view being animated. Specify this point in the coordinate system of  .

## See Also

- [init(container: UIView, center: CGPoint, transform: CGAffineTransform)](uipreviewtarget/init(container:center:transform:).md)
  Creates a preview target object using the specified container view and configuration details.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewtarget/init(container:center:))*