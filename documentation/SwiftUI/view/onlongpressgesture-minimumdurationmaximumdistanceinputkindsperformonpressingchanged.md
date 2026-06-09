# onLongPressGesture(minimumDuration:maximumDistance:inputKinds:perform:onPressingChanged:)

**Framework**: SwiftUI  
**Kind**: method

Adds an action to perform when this view recognizes a long press gesture.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func onLongPressGesture(minimumDuration: Double = 0.5, maximumDistance: CGFloat = 10, inputKinds: GestureInputKinds = .all, perform action: @escaping () -> Void, onPressingChanged: ((Bool) -> Void)? = nil) -> some View
```

## Parameters

- `minimumDuration`: The minimum duration of the long press that must elapse before the gesture succeeds.
- `maximumDistance`: The maximum distance that the fingers or cursor performing the long press can move before the gesture fails.
- `inputKinds`: A set of input kinds that this gesture recognizes. If not specified, the gesture will recognize all applicable input kinds that a person can use to perform it.
- `action`: The action to perform when a long press is recognized.
- `onPressingChanged`: A closure to run when the pressing state of the gesture changes, passing the current state as a parameter.

## See Also

- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](view/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](view/onlongpressgesture(minimumduration:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongTouchGesture(minimumDuration: Double, perform: () -> Void, onTouchingChanged: ((Bool) -> Void)?) -> some View](view/onlongtouchgesture(minimumduration:perform:ontouchingchanged:).md)
  Adds an action to perform when this view recognizes a remote long touch gesture. A long touch gesture is when the finger is on the remote touch surface without actually pressing.
- [struct LongPressGesture](longpressgesture.md)
  A gesture that succeeds when the user performs a long press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/onlongpressgesture(minimumduration:maximumdistance:inputkinds:perform:onpressingchanged:))*