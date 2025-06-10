# defaultFocus(_:_:priority:)

**Framework**: PermissionKit  
**Kind**: method

Defines a region of the window in which default focus is evaluated by assigning a value to a given focus state binding.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 26.0+ (Beta)
- watchOS 9.0+

## Declaration

```swift
nonisolated
func defaultFocus<V>(_ binding: FocusState<V>.Binding, _ value: V, priority: DefaultFocusEvaluationPriority = .automatic) -> some View where V : Hashable
```

#### Return Value

The modified view.

#### Discussion

By default, SwiftUI evaluates default focus when the window first appears, and when a focus state binding update moves focus automatically, but not when responding to user-driven navigation commands.

Clients can override the default behavior by specifying an evaluation priority of `DefaultFocusEvaluationPriority/userInitiated`, which causes SwiftUI to use the client’s preferred default focus in response to user-driven focus navigation as well as automatic changes.

In the following example, focus automatically goes to the second of the two text fields when the view is first presented in the window.

```None
WindowGroup {
    VStack {
        TextField(...)
            .focused($focusedField, equals: .firstField)
        TextField(...)
            .focused($focusedField, equals: .secondField)
    }
    .defaultFocus($focusedField, .secondField)
}
```

## Parameters

- `binding`: A focus state binding to update when evaluating default   focus in the modified view hierarchy.
- `value`: The value to set the binding to during evaluation.
- `priority`: An indication of how to prioritize the preferred default   focus target when focus moves into the modified view hierarchy.   The default value is  , which means the preference will   be given priority when focus is being initialized or relocated   programmatically, but not when responding to user-directed   navigation commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/permissionkit/communicationlimitsbutton/defaultfocus(_:_:priority:))*