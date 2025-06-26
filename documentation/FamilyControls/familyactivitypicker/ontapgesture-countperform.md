# onTapGesture(count:perform:)

**Framework**: FamilyControls  
**Kind**: method

Adds an action to perform when this view recognizes a tap gesture.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 16.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func onTapGesture(count: Int = 1, perform action: @escaping () -> Void) -> some View
```

#### Discussion

Use this method to perform the specified `action` when the user clicks or taps on the view or container `count` times.

> **Note**: If you create a control that’s functionally equivalent to a `Button`, use `ButtonStyle` to create a customized button instead.

In the example below, the color of the heart images changes to a random color from the `colors` array whenever the user clicks or taps on the view twice:

```swift
struct TapGestureExample: View {
    let colors: [Color] = [.gray, .red, .orange, .yellow,
                           .green, .blue, .purple, .pink]
    @State private var fgColor: Color = .gray

    var body: some View {
        Image(systemName: "heart.fill")
            .resizable()
            .frame(width: 200, height: 200)
            .foregroundColor(fgColor)
            .onTapGesture(count: 2) {
                fgColor = colors.randomElement()!
            }
    }
}
```

## Parameters

- `count`: The number of taps or clicks required to trigger the action   closure provided in  . Defaults to  .
- `action`: The action to perform.

## See Also

- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](familyactivitypicker/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](familyactivitypicker/onlongpressgesture(minimumduration:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func gesture<T>(T, including: GestureMask) -> some View](familyactivitypicker/gesture(_:including:).md)
  Attaches a gesture to the view with a lower precedence than gestures defined by the view.
- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](familyactivitypicker/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func simultaneousGesture<T>(T, including: GestureMask) -> some View](familyactivitypicker/simultaneousgesture(_:including:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/ontapgesture(count:perform:))*