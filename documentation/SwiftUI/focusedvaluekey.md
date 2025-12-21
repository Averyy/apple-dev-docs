# FocusedValueKey

**Framework**: SwiftUI  
**Kind**: protocol

A protocol for identifier types used when publishing and observing focused values.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
protocol FocusedValueKey
```

#### Overview

Unlike [`EnvironmentKey`](environmentkey.md), `FocusedValueKey` has no default value requirement, because the default value for a key is always `nil`.

Use the `Entry` macro to create custom focused values by extending `FocusedValues` with new properties:

```swift
extension FocusedValues {
    @Entry var selectedItem: Item?
}
```

Alternatively it is possible to create a focused value key by manually creating a type that conforms to this protocol:

```swift
struct SelectedItemKey: FocusedValueKey {
    typealias Value = Item
}
```

Then extend [`FocusedValues`](focusedvalues.md) to add a computed property for your key:

```swift
extension FocusedValues {
    var selectedItem: Item? {
        get { self[SelectedItemKey.self] }
        set { self[SelectedItemKey.self] = newValue }
    }
}
```

## Topics

### Specifying the value type
- [associatedtype Value](focusedvaluekey/value.md)

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
- [struct FocusedBinding](focusedbinding.md)
  A convenience property wrapper for observing and automatically unwrapping state bindings from the focused view or one of its ancestors.
- [func searchFocused(FocusState<Bool>.Binding) -> some View](view/searchfocused(_:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [func searchFocused<V>(FocusState<V>.Binding, equals: V) -> some View](view/searchfocused(_:equals:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusedvaluekey)*