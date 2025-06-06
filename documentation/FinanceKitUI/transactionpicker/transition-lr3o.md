# transition(_:)

**Framework**: FinanceKitUI  
**Kind**: method

Associates a transition with the view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func transition<T>(_ transition: T) -> some View where T : Transition
```

#### Discussion

When this view appears or disappears, the transition will be applied to it, allowing for animating it in and out.

The following code will conditionally show MyView, and when it appears or disappears, will use a custom RotatingFadeTransition transition to show it.

```None
if isActive {
    MyView()
        .transition(RotatingFadeTransition())
}
Button("Toggle") {
    withAnimation {
        isActive.toggle()
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/transactionpicker/transition(_:)-lr3o)*