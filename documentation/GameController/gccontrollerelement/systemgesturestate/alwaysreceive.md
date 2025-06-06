# GCControllerElement.SystemGestureState.alwaysReceive

**Framework**: Game Controller  
**Kind**: case

A state that sends input to your app and a gesture recognizer simultaneously.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case alwaysReceive
```

#### Discussion

This state removes any delay in your app receiving the input but may trigger a simultaneous system gesture and in-app action.

## See Also

- [GCControllerElement.SystemGestureState.enabled](gccontrollerelement/systemgesturestate/enabled.md)
  A state that sends input to your app only after a gesture recognizer doesn’t identify a gesture.
- [GCControllerElement.SystemGestureState.disabled](gccontrollerelement/systemgesturestate/disabled.md)
  A state that sends input to your app directly and not to a gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/systemgesturestate/alwaysreceive)*