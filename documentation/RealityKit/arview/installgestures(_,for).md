# installGestures(_:for:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Installs standard gestures onto the given entity, configured to be recognized simultaneously.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+

## Declaration

```swift
@discardableResult
@MainActor @preconcurrency func installGestures(_ gestures: ARView.EntityGestures = .all, for entity: any HasCollision) -> [any EntityGestureRecognizer]
```

#### Return Value

The set of gesture recognizers created to handle the requested gestures.

## Parameters

- `gestures`: The gesture types to install.
- `entity`: The entity with which to associate the gesture recognizers.

## See Also

### Adding gesture recognizers to entities
- [func gestureRecognizer(UIGestureRecognizer, shouldRecognizeSimultaneouslyWith: UIGestureRecognizer) -> Bool](./gesturerecognizer%28_,shouldrecognizesimultaneouslywith%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/arview/installgestures(_:for:))*