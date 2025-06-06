# entity

**Framework**: RealityKit  
**Kind**: property

The entity the receiver is associated with

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
@preconcurrency var entity: (any HasCollision)? { get set }
```

## See Also

- [func canPrevent(UIGestureRecognizer) -> Bool](entityscalegesturerecognizer/canprevent(_:).md)
- [func touchesBegan(Set<UITouch>, with: UIEvent)](entityscalegesturerecognizer/touchesbegan(_:with:).md)
  Sent to the gesture recognizer when one or more fingers touch down on the associated entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entityscalegesturerecognizer/entity)*