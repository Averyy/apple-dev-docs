# convertToScreenCoordinates(_:in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Converts the specified path object to screen coordinates and returns a new path object with the results.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
static func convertToScreenCoordinates(_ path: UIBezierPath, in view: UIView) -> UIBezierPath
```

```c
extern UIBezierPath *UIAccessibilityConvertPathToScreenCoordinates(UIBezierPath *path, UIView *view);
```

#### Return Value

A new path object that has the same shape as `path` but whose points are specified in screen coordinates.

#### Discussion

This function adjusts the points of the path you provide to values that the accessibility system can use. You can use it to convert path objects in use by your app’s user interface before handing them to the accessibility system.

## Parameters

- `path`: The path object that you want to convert. The coordinate values used to create this path object should be relative to the coordinate system of the specified `view`. This parameter must not be `nil`.
- `view`: The view whose coordinate system was used to define the path. This parameter must not be `nil`.

## See Also

### Conversions
- [static func convertToScreenCoordinates(CGRect, in: UIView) -> CGRect](./converttoscreencoordinates%28_,in%29-9ziiu.md)
  Converts the specified rectangle from view coordinates to screen coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibility/converttoscreencoordinates(_:in:)-6dx4a)*