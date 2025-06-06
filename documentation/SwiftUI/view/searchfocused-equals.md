# searchFocused(_:equals:)

**Framework**: SwiftUI  
**Kind**: method

Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
nonisolated
func searchFocused<V>(_ binding: FocusState<V>.Binding, equals value: V) -> some View where V : Hashable
```

#### Return Value

The modified view.

#### Discussion

To control focus by matching a simple boolean condition, use the [`searchFocused(_:)`](view/searchfocused(_:).md) modifier instead.

For more information about using searchable modifiers, refer to [`Adding a search interface to your app`](adding-a-search-interface-to-your-app.md).

## Parameters

- `binding`: The state binding to register. When focus moves to the   associated search field, the binding sets the bound value to the   corresponding match value. If a caller sets the state value   programmatically to the matching value, then focus moves to the   search field. When focus leaves the search field, the binding sets   the bound value to  . If a caller sets the value to  ,   SwiftUI automatically dismisses focus.
- `value`: The value to match against when determining whether the   binding should change.

## See Also

- [func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View](view/focused(_:equals:).md)
  Modifies this view by binding its focus state to the given state value.
- [func focused(FocusState<Bool>.Binding) -> some View](view/focused(_:).md)
  Modifies this view by binding its focus state to the given Boolean state value.
- [var isFocused: Bool](environmentvalues/isfocused.md)
  Returns whether the nearest focusable ancestor has focus.
- [struct FocusState](focusstate.md)
  A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.
- [struct FocusedValue](focusedvalue.md)
  A property wrapper for observing values from the focused view or one of its ancestors.
- [macro Entry()](entry().md)
  Creates an environment values, transaction, container values, or focused values entry.
- [protocol FocusedValueKey](focusedvaluekey.md)
  A protocol for identifier types used when publishing and observing focused values.
- [struct FocusedBinding](focusedbinding.md)
  A convenience property wrapper for observing and automatically unwrapping state bindings from the focused view or one of its ancestors.
- [func searchFocused(FocusState<Bool>.Binding) -> some View](view/searchfocused(_:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/searchfocused(_:equals:))*