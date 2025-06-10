# focused(_:)

**Framework**: SwiftUI  
**Kind**: method

Modifies this view by binding its focus state to the given Boolean state value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func focused(_ condition: FocusState<Bool>.Binding) -> some View
```

#### Return Value

The modified view.

#### Discussion

Use this modifier to cause the view to receive focus whenever the `condition` value is `true`. You can use this modifier to observe the focus state of a single view, or programmatically set and remove focus from the view.

In the following example, a single [`TextField`](textfield.md) accepts a user’s desired `username`. The text field binds its focus state to the Boolean value `usernameFieldIsFocused`. A “Submit” button’s action verifies whether the name is available. If the name is unavailable, the button sets `usernameFieldIsFocused` to `true`, which causes focus to return to the text field, so the user can enter a different name.

```swift
@State private var username: String = ""
@FocusState private var usernameFieldIsFocused: Bool
@State private var showUsernameTaken = false

var body: some View {
    VStack {
        TextField("Choose a username.", text: $username)
            .focused($usernameFieldIsFocused)
        if showUsernameTaken {
            Text("That username is taken. Please choose another.")
        }
        Button("Submit") {
            showUsernameTaken = false
            if !isUserNameAvailable(username: username) {
                usernameFieldIsFocused = true
                showUsernameTaken = true
            }
        }
    }
}
```

To control focus by matching a value, use the [`focused(_:equals:)`](view/focused(_:equals:).md) method instead.

## Parameters

- `condition`: The focus state to bind. When focus moves   to the view, the binding sets the bound value to  . If a caller   sets the value to    programmatically, then focus moves to the   modified view. When focus leaves the modified view, the binding   sets the value to  . If a caller sets the value to  ,   SwiftUI automatically dismisses focus.

## See Also

- [func focused<Value>(FocusState<Value>.Binding, equals: Value) -> some View](view/focused(_:equals:).md)
  Modifies this view by binding its focus state to the given state value.
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
- [func searchFocused<V>(FocusState<V>.Binding, equals: V) -> some View](view/searchfocused(_:equals:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/focused(_:))*