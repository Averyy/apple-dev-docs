# gesture(_:name:isEnabled:)

**Framework**: RealityKit  
**Kind**: method

Attaches a gesture to the view with a lower precedence than gestures defined by the view.

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
func gesture<T>(_ gesture: T, name: String, isEnabled: Bool = true) -> some View where T : Gesture
```

#### Discussion

Use this method when you need to attach a gesture to a view. The example below defines a custom gesture that prints a message to the console and attaches it to the view’s `VStack`. Inside the `VStack` a red heart `Image` defines its own `TapGesture` handler that also prints a message to the console, and blue rectangle with no custom gesture handlers. Tapping or clicking the image prints a message to the console from the tap gesture handler on the image, while tapping or clicking  the rectangle inside the `VStack` prints a message in the console from the enclosing vertical stack gesture handler.

You can also use the `isEnabled` parameter to conditionally disable the gesture.

```None
struct GestureExample: View {
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
        .gesture(newGesture, isEnabled: isGestureEnabled)
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

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/resolvedmodel3d/gesture(_:name:isenabled:))*