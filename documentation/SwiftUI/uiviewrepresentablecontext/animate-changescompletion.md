# animate(changes:completion:)

**Framework**: SwiftUI  
**Kind**: method

Animates changes using the animation in the current transaction.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
@preconcurrency func animate(changes: () -> Void, completion: (() -> Void)? = nil)
```

#### Discussion

This combines [`animate(with:changes:completion:)`](https://developer.apple.com/documentation/UIKit/UIView/animate(with:changes:completion:)) with the current transaction’s animation. When you start a SwiftUI animation using [`withAnimation(_:_:)`](withanimation(_:_:).md) and have a mutated SwiftUI state that causes the representable object to update, use this method to animate changes in the representable object using the same `Animation` timing.

```swift
struct ContentView: View {
    @State private var isCollapsed = false
    var body: some View {
        ZStack {
            MyDetailView(isCollapsed: isCollapsed)
            MyRepresentable(isCollapsed: $isCollapsed)
            Button("Collapse Content") {
                withAnimation(.bouncy) {
                    isCollapsed = true
                }
            }
        }
    }
}

struct MyRepresentable: UIViewRepresentable {
    @Binding var isCollapsed: Bool

    func updateUIView(_ uiView: UIViewType, context: Context) {
        if isCollapsed && !uiView.isCollapsed {
            context.animate {
                uiView.collapseSubview()
                uiView.layout()
            }
        }
    }
}
```

## Parameters

- `changes`: A closure that changes animatable properties.
- `completion`: A closure to execute after the animation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/uiviewrepresentablecontext/animate(changes:completion:))*