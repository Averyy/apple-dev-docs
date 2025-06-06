# onLongTouchGesture(minimumDuration:perform:onTouchingChanged:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform when this view recognizes a remote long touch gesture. A long touch gesture is when the finger is on the remote touch surface without actually pressing.

**Availability**:
- tvOS 16.0+

## Declaration

```swift
nonisolated
func onLongTouchGesture(minimumDuration: Double = 0.5, perform action: @escaping () -> Void, onTouchingChanged: ((Bool) -> Void)? = nil) -> some View
```

## Parameters

- `minimumDuration`: The minimum duration of the long touch that must   elapse before the gesture succeeds.
- `action`: The action to perform when a long touch is recognized
- `onTouchingChanged`: A closure to run when the touching state of   the gesture changes, passing the current state as a parameter.

## See Also

- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](view/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](view/onlongpressgesture(minimumduration:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [struct LongPressGesture](longpressgesture.md)
  A gesture that succeeds when the user performs a long press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onlongtouchgesture(minimumduration:perform:ontouchingchanged:))*