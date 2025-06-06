# focusable(_:onFocusChange:)

**Framework**: App Intents  
**Kind**: method

Specifies if the view is focusable and, if so, adds an action to perform when the view comes into focus.

**Availability**:
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func focusable(_ isFocusable: Bool = true, onFocusChange: @escaping (Bool) -> Void = { _ in }) -> some View
```

#### Return Value

A view that sets whether a view is focusable, and triggers `onFocusChange` when the view gains or loses focus.

## Parameters

- `isFocusable`: A Boolean value that indicates whether this view is   focusable.
- `onFocusChange`: A closure that’s called whenever this view either   gains or loses focus. The Boolean parameter to   is    when the view is in focus; otherwise, it’s  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/focusable(_:onfocuschange:))*