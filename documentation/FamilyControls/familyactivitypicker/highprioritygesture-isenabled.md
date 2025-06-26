# highPriorityGesture(_:isEnabled:)

**Framework**: FamilyControls  
**Kind**: method

Attaches a gesture to the view with a higher precedence than gestures defined by the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func highPriorityGesture<T>(_ gesture: T, isEnabled: Bool) -> some View where T : Gesture
```

#### Discussion

Use this method when you need to define a high priority gesture to take precedence over the view’s existing gestures. The example below defines a custom gesture that prints a message to the console and attaches it to the view’s `VStack`. Inside the `VStack` a red heart `Image` defines its own `TapGesture` handler that also prints a message to the console, and a blue rectangle with no custom gesture handlers. Tapping or clicking any of the views results in a console message from the high priority gesture attached to the enclosing `VStack`.

You can also use the `isEnabled` parameter to conditionally disable the gesture.

```swift
struct HighPriorityGestureExample: View {
    @State private var message = "Message"
    var isGestureEnabled: Bool
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
        .highPriorityGesture(
            newGesture, isEnabled: isGestureEnabled)
        .frame(width: 200, height: 200)
        .border(Color.purple)
    }
}
```

## Parameters

- `gesture`: A gesture to attach to the view.
- `isEnabled`: Whether the added gesture is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/highprioritygesture(_:isenabled:))*