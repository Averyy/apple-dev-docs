# GCControllerElement.SystemGestureState.enabled

**Framework**: Game Controller  
**Kind**: case

A state that sends input to your app only after a gesture recognizer doesn’t identify a gesture.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
case enabled
```

#### Discussion

If you enable system gestures, the system sends the input to the gesture recognizer and only sends it to your app if it doesn’t recognize a gesture. If it does recognize a gesture, it doesn’t send any input to your app.

## See Also

- [GCControllerElement.SystemGestureState.alwaysReceive](gccontrollerelement/systemgesturestate/alwaysreceive.md)
  A state that sends input to your app and a gesture recognizer simultaneously.
- [GCControllerElement.SystemGestureState.disabled](gccontrollerelement/systemgesturestate/disabled.md)
  A state that sends input to your app directly and not to a gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/systemgesturestate/enabled)*