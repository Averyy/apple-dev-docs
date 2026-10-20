# GCControllerElement.SystemGestureState

**Framework**: Game Controller  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum GCSystemGestureState : NSInteger;
```

## Topics

### States
- [GCControllerElement.SystemGestureState.enabled](./systemgesturestate/enabled.md)
  A state that sends input to your app only after a gesture recognizer doesn’t identify a gesture.
- [GCControllerElement.SystemGestureState.alwaysReceive](./systemgesturestate/alwaysreceive.md)
  A state that sends input to your app and a gesture recognizer simultaneously.
- [GCControllerElement.SystemGestureState.disabled](./systemgesturestate/disabled.md)
  A state that sends input to your app directly and not to a gesture recognizer.
### Initializers
- [init?(rawValue: Int)](./systemgesturestate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling system gesture input
- [var isBoundToSystemGesture: Bool](./isboundtosystemgesture.md)
  A Boolean value that indicates whether the user binds the element to a system gesture.
- [var preferredSystemGestureState: GCControllerElement.SystemGestureState](./preferredsystemgesturestate.md)
  The preferred state for handling input when the user binds the element to a system gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/systemgesturestate)*