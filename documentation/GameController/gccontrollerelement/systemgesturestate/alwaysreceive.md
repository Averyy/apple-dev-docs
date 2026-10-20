# GCControllerElement.SystemGestureState.alwaysReceive

**Framework**: Game Controller  
**Kind**: case  
**Role**: Case

A state that sends input to your app and a gesture recognizer simultaneously.

**Availability**:
- iOS 14.0+ - Deprecated in 27.0 (renamed: GCControllerElement.SystemGestureState.disabled)
- iPadOS 14.0+ - Deprecated in 27.0 (renamed: GCControllerElement.SystemGestureState.disabled)
- Mac Catalyst 14.0+ - Deprecated in 27.0 (renamed: GCControllerElement.SystemGestureState.disabled)
- macOS 11.0+ - Deprecated in 27.0 (renamed: GCControllerElement.SystemGestureState.disabled)
- tvOS 14.0+ - Deprecated in 27.0 (renamed: GCControllerElement.SystemGestureState.disabled)
- visionOS 1.0+ - Deprecated in 27.0 (renamed: GCControllerElement.SystemGestureState.disabled)

## Declaration

```swift
case alwaysReceive
```

```c
GCSystemGestureStateAlwaysReceive
```

#### Discussion

This state removes any delay in your app receiving the input but may trigger a simultaneous system gesture and in-app action.

## See Also

### States
- [GCControllerElement.SystemGestureState.enabled](./enabled.md)
  A state that sends input to your app only after a gesture recognizer doesn’t identify a gesture.
- [GCControllerElement.SystemGestureState.disabled](./disabled.md)
  A state that sends input to your app directly and not to a gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gccontrollerelement/systemgesturestate/alwaysreceive)*