# animate(changes:completion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Animates changes using the animation in the current transaction.

**Availability**:
- macOS 15.0+

## Declaration

```swift
@backDeployed(before: macOS 15.4)
@MainActor @preconcurrency func animate(changes: () -> Void, completion: (() -> Void)? = nil)
```

Available when `View` conforms to `NSViewRepresentable`.

## Discussion

This combines [`animate(_:changes:completion:)`](../../AppKit/nsanimationcontext/animate%28_,changes,completion%29.md) with the current transaction’s animation. When you start a SwiftUI animation using [`withAnimation(_:_:)`](../withanimation%28_,_%29.md) and have a mutated SwiftUI state that causes the representable object to update, use this method to animate changes in the representable object using the same `Animation` timing.

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

struct MyRepresentable: NSViewRepresentable {
    @Binding var isCollapsed: Bool

    func updateNSView(_ nsView: NSViewType, context: Context) {
        if isCollapsed && !nsView.isCollapsed {
            context.animate {
                nsView.collapseSubview()
                nsView.layoutSubtreeIfNeeded()
            }
        }
    }
}
```

## Parameters

- `changes`: A closure that changes animatable properties.
- `completion`: A closure to execute after the animation completes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/nsviewrepresentablecontext/animate(changes:completion:))*