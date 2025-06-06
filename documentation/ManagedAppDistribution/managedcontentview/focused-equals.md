# focused(_:equals:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Modifies this view by binding its focus state to the given state value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+

## Declaration

```swift
nonisolated
func focused<Value>(_ binding: FocusState<Value>.Binding, equals value: Value) -> some View where Value : Hashable
```

#### Return Value

The modified view.

#### Discussion

Use this modifier to cause the view to receive focus whenever the the `binding` equals the `value`. Typically, you create an enumeration of fields that may receive focus, bind an instance of this enumeration, and assign its cases to focusable views.

The following example uses the cases of a `LoginForm` enumeration to bind the focus state of two `TextField` views. A sign-in button validates the fields and sets the bound `focusedField` value to any field that requires the user to correct a problem.

```None
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

To control focus using a Boolean, use the `View/focused(_:)` method instead.

## Parameters

- `binding`: The state binding to register. When focus moves to the   modified view, the binding sets the bound value to the corresponding   match value. If a caller sets the state value programmatically to the   matching value, then focus moves to the modified view. When focus   leaves the modified view, the binding sets the bound value to   . If a caller sets the value to  , SwiftUI automatically   dismisses focus.
- `value`: The value to match against when determining whether the   binding should change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedcontentview/focused(_:equals:))*