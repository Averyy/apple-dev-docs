# PlayAudioAction.EventParameterType

**Framework**: RealityKit  
**Kind**: typealias

The associated event parameter type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
typealias EventParameterType = Never
```

#### Discussion

Event parameters are used when more than one event interval is defined for a single action animation. Event parameters can vary for each event interval. The parameter data associated with each event will be returned to the event handler when it is called.

The default parameter type is `Never` so that it does not need to be defined for single event action animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/playaudioaction/eventparametertype)*