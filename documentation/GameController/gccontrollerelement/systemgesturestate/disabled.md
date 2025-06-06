# GCControllerElement.SystemGestureState.disabled

**Framework**: Game Controller  
**Kind**: case

A state that sends input to your app directly and not to a gesture recognizer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case disabled
```

#### Discussion

This state gives your app full control of the input for this element.

## See Also

- [GCControllerElement.SystemGestureState.enabled](gccontrollerelement/systemgesturestate/enabled.md)
  A state that sends input to your app only after a gesture recognizer doesn’t identify a gesture.
- [GCControllerElement.SystemGestureState.alwaysReceive](gccontrollerelement/systemgesturestate/alwaysreceive.md)
  A state that sends input to your app and a gesture recognizer simultaneously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/systemgesturestate/disabled)*