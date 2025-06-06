# setActionQueue(_:action:)

**Framework**: AVFoundation  
**Kind**: method

Sets the action to perform on the specified dispatch queue when the control’s value changes.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+

## Declaration

```swift
@nonobjc
func setActionQueue(_ actionQueue: DispatchQueue, action: @escaping (Float) -> ())
```

## Mentions

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md)

#### Discussion

If the action modifies a property of the camera system, the specified dispatch queue must represent the camera system’s same exclusive execution context (see [`isSameExclusiveExecutionContext(other:)`](https://developer.apple.com/documentation/Swift/SerialExecutor/isSameExclusiveExecutionContext(other:)-3ptya)).

## Parameters

- `actionQueue`: A dispatch queue on which to call the action.
- `action`: The action to perform in response to changes to the slider’s value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcaptureslider/setactionqueue(_:action:))*