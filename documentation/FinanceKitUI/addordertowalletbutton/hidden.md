# hidden()

**Framework**: FinanceKitUI  
**Kind**: method

Hides this view unconditionally.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func hidden() -> some View
```

#### Return Value

A hidden view.

#### Discussion

Hidden views are invisible and can’t receive or respond to interactions. However, they do remain in the view hierarchy and affect layout. Use this modifier if you want to include a view for layout purposes, but don’t want it to display.

```None
HStack {
    Image(systemName: "a.circle.fill")
    Image(systemName: "b.circle.fill")
    Image(systemName: "c.circle.fill")
        .hidden()
    Image(systemName: "d.circle.fill")
}
```

The third circle takes up space, because it’s still present, but SwiftUI doesn’t draw it onscreen.

If you want to conditionally include a view in the view hierarchy, use an `if` statement instead:

```None
VStack {
    HStack {
        Image(systemName: "a.circle.fill")
        Image(systemName: "b.circle.fill")
        if !isHidden {
            Image(systemName: "c.circle.fill")
        }
        Image(systemName: "d.circle.fill")
    }
    Toggle("Hide", isOn: $isHidden)
}
```

Depending on the current value of the `isHidden` state variable in the example above, controlled by the `Toggle` instance, SwiftUI draws the circle or completely omits it from the layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekitui/addordertowalletbutton/hidden())*