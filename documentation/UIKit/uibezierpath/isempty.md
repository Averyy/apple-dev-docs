# isEmpty

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the path has any valid elements.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isEmpty: Bool { get }
```

```objc
@property (readonly, getter=isEmpty) BOOL empty;
```

#### Discussion

Valid path elements include commands to move to a specified point, draw a line or curve segment, or close the path. Thus, a path is not considered empty even if all you do is call the [`move(to:)`](./move%28to%29.md) method.

## See Also

### Performing hit-testing
- [func contains(CGPoint) -> Bool](./contains%28_%29.md)
  Returns a Boolean value that indicates whether the specified point is within the region that the path encloses.
- [var bounds: CGRect](./bounds.md)
  The bounding rectangle of the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/isempty)*