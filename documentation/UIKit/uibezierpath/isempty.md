# isEmpty

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the path has any valid elements.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isEmpty: Bool { get }
```

#### Discussion

Valid path elements include commands to move to a specified point, draw a line or curve segment, or close the path. Thus, a path is not considered empty even if all you do is call the [`move(to:)`](uibezierpath/move(to:).md) method.

## See Also

- [func contains(CGPoint) -> Bool](uibezierpath/contains(_:).md)
  Returns a Boolean value that indicates whether the specified point is within the region that the path encloses.
- [var bounds: CGRect](uibezierpath/bounds.md)
  The bounding rectangle of the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/isempty)*