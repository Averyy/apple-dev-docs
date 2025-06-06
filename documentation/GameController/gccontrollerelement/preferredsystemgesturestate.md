# preferredSystemGestureState

**Framework**: Game Controller  
**Kind**: property

The preferred state for handling input when the user binds the element to a system gesture.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var preferredSystemGestureState: GCControllerElement.SystemGestureState { get set }
```

#### Discussion

In rare situations, you may use this property to disable system gestures. However, the system isn’t guaranteed to respect this property. The default value for this property is [`GCControllerElement.SystemGestureState.enabled`](gccontrollerelement/systemgesturestate/enabled.md).

## See Also

- [var isBoundToSystemGesture: Bool](gccontrollerelement/isboundtosystemgesture.md)
  A Boolean value that indicates whether the user binds the element to a system gesture.
- [GCControllerElement.SystemGestureState](gccontrollerelement/systemgesturestate.md)
  A state for handling input when an element is part of a system gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/preferredsystemgesturestate)*