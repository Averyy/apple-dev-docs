# onLongPressGesture(minimumDuration:perform:onPressingChanged:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Adds an action to perform when this view recognizes a long press gesture.

**Availability**:
- tvOS 14.0+

## Declaration

```swift
@export(implementation)
nonisolated func onLongPressGesture(minimumDuration: Double = 0.5, perform action: @escaping () -> Void, onPressingChanged: ((Bool) -> Void)? = nil) -> some View
```

## Parameters

- `minimumDuration`: The minimum duration of the long press that must elapse before the gesture succeeds.
- `action`: The action to perform when a long press is recognized.
- `onPressingChanged`: A closure to run when the pressing state of the gesture changes, passing the current state as a parameter.

## See Also

### Recognizing long-press gestures
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](./onlongpressgesture%28minimumduration,maximumdistance,perform,onpressingchanged%29.md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, inputKinds: GestureInputKinds, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](./onlongpressgesture%28minimumduration,maximumdistance,inputkinds,perform,onpressingchanged%29.md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongTouchGesture(minimumDuration: Double, perform: () -> Void, onTouchingChanged: ((Bool) -> Void)?) -> some View](./onlongtouchgesture%28minimumduration,perform,ontouchingchanged%29.md)
  Adds an action to perform when this view recognizes a remote long touch gesture. A long touch gesture is when the finger is on the remote touch surface without actually pressing.
- [struct LongPressGesture](../longpressgesture.md)
  A gesture that succeeds when the user performs a long press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onlongpressgesture(minimumduration:perform:onpressingchanged:))*