# bounds

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The bounding rectangle of the path.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var bounds: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect bounds;
```

#### Discussion

The value in this property represents the smallest rectangle that completely encloses all points in the path, including any control points for Bézier and quadratic curves.

## See Also

### Performing hit-testing
- [func contains(CGPoint) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether the specified point is within the region that the path encloses.
- [var isEmpty: Bool](./isempty.md)
  A Boolean value that indicates whether the path has any valid elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/bounds)*