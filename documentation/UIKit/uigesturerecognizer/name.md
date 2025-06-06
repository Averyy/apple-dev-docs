# name

**Framework**: UIKit  
**Kind**: property

The unique name of the gesture recognizer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var name: String? { get set }
```

#### Discussion

Assign a string to this property that uniquely identifies the gesture recognizer. Use this name to distinguish one gesture recognizer from another during debugging, or to specify a relationship between gestures in SwiftUI and UIKit.

For example, you can assign a SwiftUI gesture a name when you create it using [`gesture(_:name:isEnabled:)`](https://developer.apple.com/documentation/SwiftUI/View/gesture(_:name:isEnabled:)), as the following code shows:

```swift
// SwiftUI code
struct TapGestureView: View {
    @State private var tapLocation: CGPoint = .zero

    var tap: some Gesture {
        DragGesture(minimumDistance: 0, coordinateSpace: .local)
            .onEnded { event in
                tapLocation = event.location
            }
    }

    var body: some View {
        Text("Tap location: \(tapLocation.debugDescription)")
            .frame(width: 120, height: 120)
            .background(Color.gray)
            .gesture(tap, name: "MyTap")
    }
}
```

Then, you can use this [`name`](uigesturerecognizer/name.md) property to refer to the gesture from UIKit. For example, you might do this in your implementation of [`gestureRecognizer(_:shouldRequireFailureOf:)`](uigesturerecognizerdelegate/gesturerecognizer(_:shouldrequirefailureof:).md), as the following code shows:

```swift
// UIKit code
class ViewController: UIViewController, UIGestureRecognizerDelegate {  
 
    func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, 
        shouldRequireFailureOf other: UIGestureRecognizer) -> Bool {
        return other.name == "MyTap"
    }

    // ...
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/name)*