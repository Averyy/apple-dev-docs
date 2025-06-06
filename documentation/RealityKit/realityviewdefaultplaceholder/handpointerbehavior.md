# handPointerBehavior(_:)

**Framework**: RealityKit  
**Kind**: method

Sets the behavior of the hand pointer while the user is interacting with the view.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
nonisolated
func handPointerBehavior(_ behavior: HandPointerBehavior?) -> some View
```

#### Return Value

A view that applies the given behavior to the hand pointer.

## Parameters

- `behavior`: The behavior to apply to the hand pointer.   If  , the hand pointer behavior will be inherited from the view’s   ancestors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/handpointerbehavior(_:))*