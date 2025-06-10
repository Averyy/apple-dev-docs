# focused(_:equals:)

**Framework**: SwiftUI  
**Kind**: method

Modifies this view by binding its focus state to the given state value.

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
func focused<Value>(_ binding: FocusState<Value>.Binding, equals value: Value) -> some View where Value : Hashable
```

#### Return Value

The modified view.

#### Discussion

Use this modifier to cause the view to receive focus whenever the `binding` equals the `value`. Typically, you create an enumeration of fields that may receive focus, bind an instance of this enumeration, and assign its cases to focusable views.

The following example uses the cases of a `LoginForm` enumeration to bind the focus state of two [`TextField`](textfield.md) views. A sign-in button validates the fields and sets the bound `focusedField` value to any field that requires the user to correct a problem.

```swift
struct LoginForm {
    enum Field: Hashable {
        case usernameField
        case passwordField
    }

    @State private var username = ""
    @State private var password = ""
    @FocusState private var focusedField: Field?

    var body: some View {
        Form {
            TextField("Username", text: $username)
                .focused($focusedField, equals: .usernameField)

            SecureField("Password", text: $password)
                .focused($focusedField, equals: .passwordField)

            Button("Sign In") {
                if username.isEmpty {
                    focusedField = .usernameField
                } else if password.isEmpty {
                    focusedField = .passwordField
                } else {
                    handleLogin(username, password)
                }
            }
        }
    }
}
```

To control focus using a Boolean, use the [`focused(_:)`](view/focused(_:).md) method instead.

## Parameters

- `binding`: The state binding to register. When focus moves to the   modified view, the binding sets the bound value to the corresponding   match value. If a caller sets the state value programmatically to the   matching value, then focus moves to the modified view. When focus   leaves the modified view, the binding sets the bound value to   . If a caller sets the value to  , SwiftUI automatically   dismisses focus.
- `value`: The value to match against when determining whether the   binding should change.

## See Also

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
- [func searchFocused<V>(FocusState<V>.Binding, equals: V) -> some View](view/searchfocused(_:equals:).md)
  Modifies this view by binding the focus state of the search field associated with the nearest searchable modifier to the given value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/focused(_:equals:))*