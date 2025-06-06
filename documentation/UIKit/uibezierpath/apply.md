# apply(_:)

**Framework**: UIKit  
**Kind**: method

Transforms all points in the path using the specified affine transform matrix.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func apply(_ transform: CGAffineTransform)
```

#### Discussion

This method applies the specified transform to the path’s points immediately. The modifications made to the path object are permanent. If you do not want to permanently modify a path object, you should consider applying the transform to a copy.

## Parameters

- `transform`: The transform matrix to apply to the path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibezierpath/apply(_:))*