# onLongPressGesture(minimumDuration:perform:onPressingChanged:)

**Framework**: FamilyControls  
**Kind**: method

Adds an action to perform when this view recognizes a long press gesture.

**Availability**:
- tvOS 14.0+

## Declaration

```swift
nonisolated
func onLongPressGesture(minimumDuration: Double = 0.5, perform action: @escaping () -> Void, onPressingChanged: ((Bool) -> Void)? = nil) -> some View
```

## Parameters

- `minimumDuration`: The minimum duration of the long press that must   elapse before the gesture succeeds.
- `action`: The action to perform when a long press is recognized.
- `onPressingChanged`: A closure to run when the pressing state of the   gesture changes, passing the current state as a parameter.

## See Also

- [func onTapGesture(count: Int, perform: () -> Void) -> some View](familyactivitypicker/ontapgesture(count:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](familyactivitypicker/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func gesture<T>(T, including: GestureMask) -> some View](familyactivitypicker/gesture(_:including:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](familyactivitypicker/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func simultaneousGesture<T>(T, including: GestureMask) -> some View](familyactivitypicker/simultaneousgesture(_:including:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/onlongpressgesture(minimumduration:perform:onpressingchanged:))*