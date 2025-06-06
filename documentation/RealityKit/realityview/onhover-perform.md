# onHover(perform:)

**Framework**: RealityKit  
**Kind**: method

Adds an action to perform when the user moves the pointer over or away from the view’s frame.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst ?+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
nonisolated
func onHover(perform action: @escaping (Bool) -> Void) -> some View
```

#### Return Value

A view that triggers `action` when the pointer enters or exits this view’s frame.

#### Discussion

Calling this method defines a region for detecting pointer movement with the size and position of this view.

## Parameters

- `action`: The action to perform whenever the pointer enters or   exits this view’s frame. If the pointer is in the view’s frame, the    closure passes   as a parameter; otherwise,  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityview/onhover(perform:))*