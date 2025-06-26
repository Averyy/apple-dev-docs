# highPriorityGesture(_:name:isEnabled:)

**Framework**: FamilyControls  
**Kind**: method

Attaches a gesture to the view with a higher precedence than gestures defined by the view.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
nonisolated
func highPriorityGesture<T>(_ gesture: T, name: String, isEnabled: Bool = true) -> some View where T : Gesture
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
- `name`: A string that identifies the gesture. In iOS, the name can be   used to set up failure relationships between UIKit gesture   recognizers and this gesture.
- `isEnabled`: Whether the added gesture is enabled. The default value   is  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/highprioritygesture(_:name:isenabled:))*