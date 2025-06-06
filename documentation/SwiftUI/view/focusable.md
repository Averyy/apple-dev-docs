# focusable(_:)

**Framework**: SwiftUI  
**Kind**: method

Specifies if the view is focusable.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func focusable(_ isFocusable: Bool = true) -> some View
```

#### Return Value

A view that sets whether a view is focusable.

## Parameters

- `isFocusable`: A Boolean value that indicates whether this   view is focusable.

## See Also

- [func focusable(Bool, interactions: FocusInteractions) -> some View](view/focusable(_:interactions:).md)
  Specifies if the view is focusable, and if so, what focus-driven interactions it supports.
- [struct FocusInteractions](focusinteractions.md)
  Values describe different focus interactions that a view can support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/focusable(_:))*