# Composing SwiftUI gestures

**Framework**: SwiftUI

Combine gestures to create complex interactions.

#### Overview

When you add multiple gestures to your app’s view hierarchy, you need to decide how the gestures interact with each other. You use gesture composition to define the order SwiftUI recognizes gestures. There are three gesture composition types:

- Simultaneous
- Sequenced
- Exclusive

When you combine gesture modifiers simultaneously, SwiftUI must recognize all subgesture patterns at the same time for it to recognize the combining gesture. When you sequence gesture modifiers one after the other, SwiftUI must recognize each subgesture in order. Finally, when you combine gestures exclusively, SwiftUI recognizes the entire gesture pattern when SwiftUI only recognizes one subgesture but not the others.

##### Sequence One Gesture After Another

When you sequence one gesture after another, SwiftUI recognizes the first gesture before it recognizes the second. For example, to require a long press before the user can drag a view, you sequence a [`DragGesture`](draggesture.md) after a [`LongPressGesture`](longpressgesture.md).

###### Model Sequenced Gesture States

To make it easier to track complicated states, use an enumeration that captures all of the states you need to configure your views. In the following example, there are three important states: no interaction (`inactive`), long press in progress (`pressing`), and dragging (`dragging`).

```swift
struct DraggableCircle: View {

    enum DragState {
        case inactive
        case pressing
        case dragging(translation: CGSize)
        
        var translation: CGSize {
            switch self {
            case .inactive, .pressing:
                return .zero
            case .dragging(let translation):
                return translation
            }
        }
        
        var isActive: Bool {
            switch self {
            case .inactive:
                return false
            case .pressing, .dragging:
                return true
            }
        }
        
        var isDragging: Bool {
            switch self {
            case .inactive, .pressing:
                return false
            case .dragging:
                return true
            }
        }
    }
    
    @GestureState private var dragState = DragState.inactive
    @State private var viewState = CGSize.zero
```

###### Create Gestures and Update the Ui State

When you sequence two gestures, the callbacks capture the state of both gestures. In the update callback, the new `value` uses an enumeration to represent the combination of the possible gesture states. The code below converts the underlying gesture states into the high-level `DragState` enumeration defined above.

```swift
var body: some View {
        let minimumLongPressDuration = 0.5
        let longPressDrag = LongPressGesture(minimumDuration: minimumLongPressDuration)
            .sequenced(before: DragGesture())
            .updating($dragState) { value, state, transaction in
                switch value {
                // Long press begins.
                case .first(true):
                    state = .pressing
                // Long press confirmed, dragging may begin.
                case .second(true, let drag):
                    state = .dragging(translation: drag?.translation ?? .zero)
                // Dragging ended or the long press cancelled.
                default:
                    state = .inactive
                }
            }
            .onEnded { value in
                guard case .second(true, let drag?) = value else { return }
                self.viewState.width += drag.translation.width
                self.viewState.height += drag.translation.height
            }
```

When the user begins pressing the view, the drag state changes to `pressing` and a shadow animates under the shape. After the user finishes the long press and the drag state changes to `dragging`, a border appears around the shape to indicate that the user may begin moving the view.

```swift
        return Circle()
            .fill(Color.blue)
            .overlay(dragState.isDragging ? Circle().stroke(Color.white, lineWidth: 2) : nil)
            .frame(width: 100, height: 100, alignment: .center)
            .offset(
                x: viewState.width + dragState.translation.width,
                y: viewState.height + dragState.translation.height
            )
            .animation(nil)
            .shadow(radius: dragState.isActive ? 8 : 0)
            .animation(.linear(duration: minimumLongPressDuration))
            .gesture(longPressDrag)
    }
}
```

## See Also

- [func simultaneousGesture<T>(T, including: GestureMask) -> some View](view/simultaneousgesture(_:including:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, isEnabled: Bool) -> some View](view/simultaneousgesture(_:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [func simultaneousGesture<T>(T, name: String, isEnabled: Bool) -> some View](view/simultaneousgesture(_:name:isenabled:).md)
  Attaches a gesture to the view to process simultaneously with gestures defined by the view.
- [struct SequenceGesture](sequencegesture.md)
  A gesture that’s a sequence of two gestures.
- [struct SimultaneousGesture](simultaneousgesture.md)
  A gesture containing two gestures that can happen at the same time with neither of them preceding the other.
- [struct ExclusiveGesture](exclusivegesture.md)
  A gesture that consists of two gestures where only one of them can succeed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/composing-swiftui-gestures)*