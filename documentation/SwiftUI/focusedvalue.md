# FocusedValue

**Framework**: SwiftUI  
**Kind**: struct

A property wrapper for observing values from the focused view or one of its ancestors.

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
@propertyWrapper
struct FocusedValue<Value>
```

## Mentions

- [Building and customizing the menu bar with SwiftUI](building-and-customizing-the-menu-bar-with-swiftui.md)

#### Overview

If multiple views publish values using the same key, the wrapped property will reflect the value from the view closest to focus.

## Topics

### Creating the value
- [init(_:)](focusedvalue/init(_:).md)
  A new property wrapper for the given key path.
### Getting the value
- [var wrappedValue: Value?](focusedvalue/wrappedvalue.md)
  The value for the focus key given the current scope and state of the focused view hierarchy.

## Relationships

### Conforms To
- [DynamicProperty](dynamicproperty.md)

## See Also

- [func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View](view/focused(_:equals:).md)
  Modifies this view by binding its focus state to the given state value.
- [func focused(FocusState<Bool>.Binding) -> some View](view/focused(_:).md)
  Modifies this view by binding its focus state to the given Boolean state value.
- [var isFocused: Bool](environmentvalues/isfocused.md)
  Returns whether the nearest focusable ancestor has focus.
- [struct FocusState](focusstate.md)
  A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.
- [macro Entry()](entry().md)
  Creates an environment values, transaction, container values, or focused values entry.
- [protocol FocusedValueKey](focusedvaluekey.md)
  A protocol for identifier types used when publishing and observing focused values.
- [struct FocusedBinding](focusedbinding.md)
  A convenience property wrapper for observing and automatically unwrapping state bindings from the focused view or one of its ancestors.
- [func searchFocused(FocusState<Bool>.Binding) -> some View](view/searchfocused(_:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given Boolean value.
- [func searchFocused<V>(FocusState<V>.Binding, equals: V) -> some View](view/searchfocused(_:equals:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusedvalue)*