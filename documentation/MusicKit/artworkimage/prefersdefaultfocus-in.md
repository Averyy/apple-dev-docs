# prefersDefaultFocus(_:in:)

**Framework**: MusicKit  
**Kind**: method

Indicates that the view should receive focus by default for a given namespace.

**Availability**:
- macOS 12.0+
- tvOS 14.0+
- watchOS 7.0+

## Declaration

```swift
nonisolated
func prefersDefaultFocus(_ prefersDefaultFocus: Bool = true, in namespace: Namespace.ID) -> some View
```

#### Return Value

A modified view that sets whether it prefers to be focused by default.

#### Discussion

This modifier sets the initial focus preference when no other view has focus. Use the environment value `EnvironmentValues/resetFocus` to force a reevaluation of default focus at any time.

The following tvOS example shows three buttons, labeled “1”, “2”, and “3”, in a `VStack`. By default, the “1” button would receive focus, because it is the first child in the stack. However, the `prefersDefaultFocus(_:in:)` modifier allows button “3” to receive default focus instead. Once the buttons are visible, the user can move down to and focus the “Reset to default focus” button. When the user activates this button, it uses the `ResetFocusAction` to reevaluate default focus in the `mainNamespace`, which returns the focus to button “3”.

```swift
struct ContentView: View {
    @Namespace var mainNamespace
    @Environment(\.resetFocus) var resetFocus

    var body: some View {
        VStack {
            Button ("1") {}
            Button ("2") {}
            Button ("3") {}
                .prefersDefaultFocus(in: mainNamespace)
            Button ("Reset to default focus") {
                resetFocus(in: mainNamespace)
            }
        }
        .focusScope(mainNamespace)
    }
}
```

The default focus preference is limited to the focusable ancestor that matches the provided namespace. If multiple views express this preference, then SwiftUI applies the current platform rules to determine which view receives focus.

## Parameters

- `prefersDefaultFocus`: A Boolean value that indicates whether this   view prefers to receive focus by default. The default value,  ,   causes the view to receive focus by default.
- `namespace`: The namespace associated with the focus scope within   which this view prefers default focus.


---

*[View on Apple Developer](https://developer.apple.com/documentation/musickit/artworkimage/prefersdefaultfocus(_:in:))*