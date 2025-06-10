# GCControllerElement.SystemGestureState

**Framework**: Game Controller  
**Kind**: enum

A state for handling input when an element is part of a system gesture.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum SystemGestureState
```

## Topics

### States
- [GCControllerElement.SystemGestureState.enabled](gccontrollerelement/systemgesturestate/enabled.md)
  A state that sends input to your app only after a gesture recognizer doesn’t identify a gesture.
- [GCControllerElement.SystemGestureState.alwaysReceive](gccontrollerelement/systemgesturestate/alwaysreceive.md)
  A state that sends input to your app and a gesture recognizer simultaneously.
- [GCControllerElement.SystemGestureState.disabled](gccontrollerelement/systemgesturestate/disabled.md)
  A state that sends input to your app directly and not to a gesture recognizer.
### Initializers
- [init?(rawValue: Int)](gccontrollerelement/systemgesturestate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isBoundToSystemGesture: Bool](gccontrollerelement/isboundtosystemgesture.md)
  A Boolean value that indicates whether the user binds the element to a system gesture.
- [var preferredSystemGestureState: GCControllerElement.SystemGestureState](gccontrollerelement/preferredsystemgesturestate.md)
  The preferred state for handling input when the user binds the element to a system gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/systemgesturestate)*