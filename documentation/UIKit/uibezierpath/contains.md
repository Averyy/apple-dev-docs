# contains(_:)

**Framework**: UIKit  
**Kind**: method

Returns a Boolean value that indicates whether the specified point is within the region that the path encloses.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func contains(_ point: CGPoint) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the point is considered to be within the path’s enclosed area or [`false`](https://developer.apple.com/documentation/Swift/false) if it is not.

#### Discussion

The receiver contains the specified point if that point is in a portion of a closed subpath that would normally be painted during a fill operation. This method uses the value of the [`usesEvenOddFillRule`](uibezierpath/usesevenoddfillrule.md) property to determine which parts of the subpath would be filled.

A point is not considered to be enclosed by the path if it is inside an open subpath, regardless of whether that area would be painted during a fill operation. Therefore, to determine mouse hits on open paths, you must create a copy of the path object and explicitly close any subpaths (using the [`close()`](uibezierpath/close().md) method) before calling this method.

## Parameters

- `point`: The point to test against the path, specified in the path object’s coordinate system.

## See Also

- [var isEmpty: Bool](uibezierpath/isempty.md)
  A Boolean value that indicates whether the path has any valid elements.
- [var bounds: CGRect](uibezierpath/bounds.md)
  The bounding rectangle of the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/contains(_:))*