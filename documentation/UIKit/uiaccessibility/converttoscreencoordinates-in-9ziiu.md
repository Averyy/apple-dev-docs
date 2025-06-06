# convertToScreenCoordinates(_:in:)

**Framework**: UIKit  
**Kind**: method

Converts the specified rectangle from view coordinates to screen coordinates.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
static func convertToScreenCoordinates(_ rect: CGRect, in view: UIView) -> CGRect
```

#### Return Value

The rectangle in screen coordinates.

#### Discussion

Use this function to convert accessibility frame rectangles to screen coordinates.

## Parameters

- `rect`: A rectangle specified in the coordinate system of the specified  .
- `view`: The view that contains the specified rectangle. This parameter must not be  .

## See Also

- [static func convertToScreenCoordinates(UIBezierPath, in: UIView) -> UIBezierPath](uiaccessibility/converttoscreencoordinates(_:in:)-6dx4a.md)
  Converts the specified path object to screen coordinates and returns a new path object with the results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/converttoscreencoordinates(_:in:)-9ziiu)*