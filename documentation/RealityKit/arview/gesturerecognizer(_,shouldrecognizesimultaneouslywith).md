# gestureRecognizer(_:shouldRecognizeSimultaneouslyWith:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@MainActor
@preconcurrency @objc dynamic func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldRecognizeSimultaneouslyWith otherGestureRecognizer: UIGestureRecognizer) -> Bool
```

## See Also

### Adding gesture recognizers to entities
- [func installGestures(ARView.EntityGestures, for: any HasCollision) -> [any EntityGestureRecognizer]](./installgestures%28_,for%29.md)
  Installs standard gestures onto the given entity, configured to be recognized simultaneously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/gesturerecognizer(_:shouldrecognizesimultaneouslywith:))*