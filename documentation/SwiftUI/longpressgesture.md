# LongPressGesture

**Framework**: SwiftUI  
**Kind**: struct

A gesture that succeeds when the user performs a long press.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
struct LongPressGesture
```

## Mentions

- [Adding interactivity with gestures](adding-interactivity-with-gestures.md)
- [Composing SwiftUI gestures](composing-swiftui-gestures.md)

#### Overview

To recognize a long-press gesture on a view, create and configure the gesture, then add it to the view using the [`gesture(_:including:)`](view/gesture(_:including:).md) modifier.

Add a long-press gesture to a [`Circle`](circle.md) to animate its color from blue to red, and then change it to green when the gesture ends:

```swift
struct LongPressGestureView: View {
    @GestureState private var isDetectingLongPress = false
    @State private var completedLongPress = false

    var longPress: some Gesture {
        LongPressGesture(minimumDuration: 3)
            .updating($isDetectingLongPress) { currentState, gestureState,
                    transaction in
                gestureState = currentState
                transaction.animation = Animation.easeIn(duration: 2.0)
            }
            .onEnded { finished in
                self.completedLongPress = finished
            }
    }

    var body: some View {
        Circle()
            .fill(self.isDetectingLongPress ?
                Color.red :
                (self.completedLongPress ? Color.green : Color.blue))
            .frame(width: 100, height: 100, alignment: .center)
            .gesture(longPress)
    }
}
```

## Topics

### Creating a long press gesture
- [init(minimumDuration: Double)](longpressgesture/init(minimumduration:).md)
  Creates a long-press gesture with a minimum duration
- [init(minimumDuration: Double, maximumDistance: CGFloat)](longpressgesture/init(minimumduration:maximumdistance:).md)
  Creates a long-press gesture with a minimum duration and a maximum distance that the interaction can move before the gesture fails.
- [var minimumDuration: Double](longpressgesture/minimumduration.md)
  The minimum duration of the long press that must elapse before the gesture succeeds.
- [var maximumDistance: CGFloat](longpressgesture/maximumdistance.md)
  The maximum distance that the long press can move before the gesture fails.

## Relationships

### Conforms To
- [Gesture](gesture.md)

## See Also

- [func onLongPressGesture(minimumDuration: Double, maximumDistance: CGFloat, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](view/onlongpressgesture(minimumduration:maximumdistance:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongPressGesture(minimumDuration: Double, perform: () -> Void, onPressingChanged: ((Bool) -> Void)?) -> some View](view/onlongpressgesture(minimumduration:perform:onpressingchanged:).md)
  Adds an action to perform when this view recognizes a long press gesture.
- [func onLongTouchGesture(minimumDuration: Double, perform: () -> Void, onTouchingChanged: ((Bool) -> Void)?) -> some View](view/onlongtouchgesture(minimumduration:perform:ontouchingchanged:).md)
  Adds an action to perform when this view recognizes a remote long touch gesture. A long touch gesture is when the finger is on the remote touch surface without actually pressing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/longpressgesture)*