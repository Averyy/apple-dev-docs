# findNavigator(isPresented:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Programmatically presents the find and replace interface for text editor views.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+

## Declaration

```swift
nonisolated
func findNavigator(isPresented: Binding<Bool>) -> some View
```

#### Return Value

A view that presents the find and replace interface when `isPresented` is `true`.

#### Discussion

Add this modifier to a `TextEditor`, or to a view hierarchy that contains at least one text editor, to control the presentation of the find and replace interface. When you set the `isPresented` binding to `true`, the system shows the interface, and when you set it to `false`, the system hides the interface. The following example shows and hides the interface based on the state of a toolbar button:

```None
TextEditor(text: $text)
    .findNavigator(isPresented: $isPresented)
    .toolbar {
        Toggle(isOn: $isPresented) {
            Label("Find", systemImage: "magnifyingglass")
        }
    }
```

The find and replace interface allows people to search for instances of a specified string in the text editor, and optionally to replace instances of the search string with another string. They can also show and hide the interface using built-in controls, like menus and keyboard shortcuts. SwiftUI updates `isPresented` to reflect the users’s actions.

If the text editor view isn’t currently in focus, the system still presents the find and replace interface when you set `isPresented` to `true`. If the view hierarchy contains multiple editors, the one that shows the find and replace interface is nondeterministic.

You can disable the find and replace interface for a text editor by applying the `View/findDisabled(_:)` modifier to the editor. If you do that, setting this modifier’s `isPresented` binding to `true` has no effect, but only if the disabling modifier appears closer to the text editor, like this:

```None
TextEditor(text: $text)
    .findDisabled(isDisabled)
    .findNavigator(isPresented: $isPresented)
```

## Parameters

- `isPresented`: A binding to a Boolean value that controls the   presentation of the find and replace interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/findnavigator(ispresented:))*