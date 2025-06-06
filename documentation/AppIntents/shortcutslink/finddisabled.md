# findDisabled(_:)

**Framework**: App Intents  
**Kind**: method

Prevents find and replace operations in a text editor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func findDisabled(_ isDisabled: Bool = true) -> some View
```

#### Return Value

A view that disables the find and replace interface.

#### Discussion

Add this modifier to ensure that people can’t activate the find and replace interface for a `TextEditor`:

```swift
TextEditor(text: $text)
    .findDisabled()
```

When you disable the find operation, you also implicitly disable the replace operation. If you want to only disable replace, use `View/replaceDisabled(_:)` instead.

Using this modifer also prevents programmatic find and replace interface presentation using the `View/findNavigator(isPresented:)` method. Be sure to place the disabling modifier closer to the text editor for this to work:

```swift
TextEditor(text: $text)
    .findDisabled(isDisabled)
    .findNavigator(isPresented: $isPresented)
```

If you apply this modifer at multiple levels of a view hierarchy, the call closest to the text editor takes precedence. For example, people can activate find and replace for the first text editor in the following example, but not the second:

```swift
VStack {
    TextEditor(text: $text1)
        .findDisabled(false)
    TextEditor(text: $text2)
}
.findDisabled(true)
```

## Parameters

- `isDisabled`: A Boolean value that indicates whether to   disable the find and replace interface for a text editor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/finddisabled(_:))*