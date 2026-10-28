# CATransform3DInvert(_:)

**Framework**: Core Animation  
**Kind**: func  
**Role**: Function

Inverts `t` and returns the result.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CATransform3DInvert(_ t: CATransform3D) -> CATransform3D
```

```c
extern CATransform3D CATransform3DInvert(CATransform3D t);
```

## Discussion

Returns the original matrix if `t` has no inverse.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransform3dinvert(_:))*