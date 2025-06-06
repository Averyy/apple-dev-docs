# focusable(_:)

**Framework**: FamilyControls  
**Kind**: method

Specifies if the view is focusable.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 12.0+
- tvOS 15.0+
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

- [func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View](familyactivitypicker/focused(_:equals:).md)
  Modifies this view by binding its focus state to the given state value.
- [func focused(FocusState<Bool>.Binding) -> some View](familyactivitypicker/focused(_:).md)
  Modifies this view by binding its focus state to the given Boolean state value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/familycontrols/familyactivitypicker/focusable(_:))*