# FocusState

**Framework**: SwiftUI  
**Kind**: struct

A property wrapper type that can read and write a value that SwiftUI updates as the placement of focus within the scene changes.

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
@frozen
@propertyWrapper struct FocusState<Value> where Value : Hashable
```

#### Overview

Use this property wrapper in conjunction with [`focused(_:equals:)`](view/focused(_:equals:).md) and [`focused(_:)`](view/focused(_:).md) to describe views whose appearance and contents relate to the location of focus in the scene. When focus enters the modified view, the wrapped value of this property updates to match a given prototype value. Similarly, when focus leaves, the wrapped value of this property resets to `nil` or `false`. Setting the property’s value programmatically has the reverse effect, causing focus to move to the view associated with the updated value.

In the following example of a simple login screen, when the user presses the Sign In button and one of the fields is still empty, focus moves to that field. Otherwise, the sign-in process proceeds.

```swift
struct LoginForm {
    enum Field: Hashable {
        case username
        case password
    }

    @State private var username = ""
    @State private var password = ""
    @FocusState private var focusedField: Field?

    var body: some View {
        Form {
            TextField("Username", text: $username)
                .focused($focusedField, equals: .username)

            SecureField("Password", text: $password)
                .focused($focusedField, equals: .password)

            Button("Sign In") {
                if username.isEmpty {
                    focusedField = .username
                } else if password.isEmpty {
                    focusedField = .password
                } else {
                    handleLogin(username, password)
                }
            }
        }
    }
}
```

To allow for cases where focus is completely absent from a view tree, the wrapped value must be either an optional or a Boolean. Set the focus binding to `false` or `nil` as appropriate to remove focus from all bound fields. You can also use this to remove focus from a [`TextField`](textfield.md) and thereby dismiss the keyboard.

##### Avoid Ambiguous Focus Bindings

The same view can have multiple focus bindings. In the following example, setting `focusedField` to either `name` or `fullName` causes the field to receive focus:

```swift
struct ContentView: View {
    enum Field: Hashable {
        case name
        case fullName
    }
    @FocusState private var focusedField: Field?

    var body: some View {
        TextField("Full Name", ...)
            .focused($focusedField, equals: .name)
            .focused($focusedField, equals: .fullName)
    }
}
```

On the other hand, binding the same value to two views is ambiguous. In the following example, two separate fields bind focus to the `name` value:

```swift
struct ContentView: View {
    enum Field: Hashable {
        case name
        case fullName
    }
    @FocusState private var focusedField: Field?

    var body: some View {
        TextField("Name", ...)
            .focused($focusedField, equals: .name)
        TextField("Full Name", ...)
            .focused($focusedField, equals: .name) // incorrect re-use of .name
    }
}
```

If the user moves focus to either field, the `focusedField` binding updates to `name`. However, if the app programmatically sets the value to `name`, SwiftUI chooses the first candidate, which in this case is the “Name” field. SwiftUI also emits a runtime warning in this case, since the repeated binding is likely a programmer error.

##### Nest Focusable Views

It is important to consider the difference between [`focused(_:equals:)`](view/focused(_:equals:).md) and [`focused(_:)`](view/focused(_:).md) with nested focusable views.

For example, consider the following code:

```swift
struct ContentView: View {
    @FocusState private var fieldIsFocused: Bool
    @FocusState private var containerIsFocused: Bool

    var body: some View {
        VStack {
            TextField("Name", ...)
                .focused($fieldIsFocused)
        }
        .focusable()
        .focused($containerIsFocused)
    }
}
```

The code above uses [`focused(_:)`](view/focused(_:).md), which binds focus state to the given Boolean state value. [`focused(_:)`](view/focused(_:).md) sets `containerIsFocused` to `true` both when the `VStack` itself receives focus and  the `TextField` that it contains receives focus. This behavior occurs because two independent instances of `@FocusState` are used to observe the focus state of the focusable `VStack` and the `TextField`. When the `VStack` does not have focus, SwiftUI checks the view hierarchy to find the closest view with focus to set the value for `containerIsFocused`. If the `TextField` contained within this `VStack` happens to be focused, [`focused(_:)`](view/focused(_:).md) will set `containerIsFocused` to `true`.

If there is need to observe whether only the `VStack` has focus, but not the inner TextField, consider using [`focused(_:equals:)`](view/focused(_:equals:).md) instead, for more granular control.

With [`focused(_:equals:)`](view/focused(_:equals:).md), the above code can be rewritten as follows:

```swift
struct ContentView: View {
    enum Focus {
        case container
        case field
    }

    @FocusState private var focused: Focus?

    var body: some View {
        VStack {
            TextField("Name", ...)
                .focused($focused, equals: .field)
        }
        .focusable()
        .focused($focused, equals: .container)
    }
}
```

With [`focused(_:equals:)`](view/focused(_:equals:).md), it is possible to define a custom data structure to represent focus state. In this case, a `Focus` enumeration is used. It has two cases, one for the focusable `VStack` and another for the `TextField` it contains. [`focused(_:equals:)`](view/focused(_:equals:).md) binds focused to `.container` only when the `VStack` itself has focus, and to `.field` when the `TextField` has focus. Because now there is only one `@FocusState` property, SwiftUI is able to disambiguate between cases when `VStack`  focus and  focus itself.

Note that both of the above approaches are acceptable. [`focused(_:equals:)`](view/focused(_:equals:).md) can be used to observe whether the given view currently receives focus. While [`focused(_:)`](view/focused(_:).md) can be used for the same purpose, additionally it can observe whether the given view contains focus.

## Topics

### Creating a focus state
- [init()](focusstate/init.md)
  Creates a focus state that binds to a Boolean.
### Inspecting the focus state
- [var projectedValue: FocusState<Value>.Binding](focusstate/projectedvalue.md)
  A projection of the focus state value that returns a binding.
- [FocusState.Binding](focusstate/binding.md)
  A property wrapper type that can read and write a value that indicates the current focus location.
- [var wrappedValue: Value](focusstate/wrappedvalue.md)
  The current state value, taking into account whatever bindings might be in effect due to the current location of focus.

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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/focusstate)*