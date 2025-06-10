# focused(_:)

**Framework**: App Intents  
**Kind**: method

Modifies this view by binding its focus state to the given Boolean state value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
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

In the following example, a single `TextField` accepts a user’s desired `username`. The text field binds its focus state to the Boolean value `usernameFieldIsFocused`. A “Submit” button’s action verifies whether the name is available. If the name is unavailable, the button sets `usernameFieldIsFocused` to `true`, which causes focus to return to the text field, so the user can enter a different name.

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

To control focus by matching a value, use the `View/focused(_:equals:)` method instead.

## Parameters

- `condition`: The focus state to bind. When focus moves   to the view, the binding sets the bound value to  . If a caller   sets the value to    programmatically, then focus moves to the   modified view. When focus leaves the modified view, the binding   sets the value to  . If a caller sets the value to  ,   SwiftUI automatically dismisses focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/focused(_:))*