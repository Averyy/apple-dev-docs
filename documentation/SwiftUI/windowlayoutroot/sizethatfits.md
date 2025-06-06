# sizeThatFits(_:)

**Framework**: SwiftUI  
**Kind**: method

Asks the window’s content for its size.

**Availability**:
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
func sizeThatFits(_ proposal: ProposedViewSize) -> CGSize
```

#### Return Value

The size that the content chooses for itself, given the proposal from its container view.

## Parameters

- `proposal`: A proposed size for the subview. In SwiftUI,   views choose their own size, but can take a size proposal from   their parent view into account when doing so.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/windowlayoutroot/sizethatfits(_:))*