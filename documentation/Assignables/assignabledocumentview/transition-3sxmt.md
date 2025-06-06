# transition(_:)

**Framework**: Assignables  
**Kind**: method

Associates a transition with the view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func transition(_ t: AnyTransition) -> some View
```

#### Discussion

When this view appears or disappears, the transition will be applied to it, allowing for animating it in and out.

The following code will conditionally show MyView, and when it appears or disappears, will use a slide transition to show it.

```None
if isActive {
    MyView()
        .transition(.slide)
}
Button("Toggle") {
    withAnimation {
        isActive.toggle()
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/transition(_:)-3sxmt)*