# gesture(_:including:)

**Framework**: FamilyControls  
**Kind**: method

Attaches a gesture to the view with a lower precedence than gestures defined by the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func gesture<T>(_ gesture: T, including mask: GestureMask = .all) -> some View where T : Gesture
```

#### Discussion

Use this method when you need to attach a gesture to a view. The example below defines a custom gesture that prints a message to the console and attaches it to the view’s `VStack`. Inside the `VStack` a red heart `Image` defines its own `TapGesture` handler that also prints a message to the console, and blue rectangle with no custom gesture handlers. Tapping or clicking the image prints a message to the console from the tap gesture handler on the image, while tapping or clicking  the rectangle inside the `VStack` prints a message in the console from the enclosing vertical stack gesture handler.

```swift
struct GestureExample: View {
    @State private var message = "Message"
    let newGesture = TapGesture().onEnded {
        print("Tap on VStack.")
    }

    var body: some View {
        VStack(spacing:25) {
            Image(systemName: "heart.fill")
                .resizable()
                .frame(width: 75, height: 75)
                .padding()
                .foregroundColor(.red)
                .onTapGesture {
                    print("Tap on image.")
                }
            Rectangle()
                .fill(Color.blue)
        }
        .gesture(newGesture)
        .frame(width: 200, height: 200)
        .border(Color.purple)
    }
}
```

## Parameters

- `gesture`: A gesture to attach to the view.
- `mask`: A value that controls how adding this gesture to the view   affects other gestures recognized by the view and its subviews.   Defaults to  .

## See Also

- [func onTapGesture(count: Int, perform: () -> Void) -> some View](familyactivitypicker/ontapgesture(count:perform:).md)
  Adds an action to perform when this view recognizes a tap gesture.
- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](familyactivitypicker/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](familyactivitypicker/onlongpressgesture(minimumduration:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func highPriorityGesture<T>(T, including: GestureMask) -> some View](familyactivitypicker/highprioritygesture(_:including:).md)
  Attaches a gesture to the view with a higher precedence than gestures defined by the view.
- [func simultaneousGesture<T>(T, including: GestureMask) -> some View](familyactivitypicker/simultaneousgesture(_:including:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/gesture(_:including:))*