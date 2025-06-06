# replaceDisabled(_:)

**Framework**: App Intents  
**Kind**: method

Prevents replace operations in a text editor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func replaceDisabled(_ isDisabled: Bool = true) -> some View
```

#### Return Value

A view that disables the replace feature of a find and replace interface.

#### Discussion

Add this modifier to ensure that people can’t activate the replace feature of a find and replace interface for a `TextEditor`:

```swift
TextEditor(text: $text)
    .replaceDisabled()
```

If you want to disable both find and replace, use the `View/findDisabled(_:)` modifier instead.

Using this modifer also disables the replace feature of a find and replace interface that you present programmatically using the `View/findNavigator(isPresented:)` method. Be sure to place the disabling modifier closer to the text editor for this to work:

```swift
TextEditor(text: $text)
    .replaceDisabled(isDisabled)
    .findNavigator(isPresented: $isPresented)
```

If you apply this modifer at multiple levels of a view hierarchy, the call closest to the text editor takes precedence. For example, people can activate find and replace for the first text editor in the following example, but only find for the second:

```swift
VStack {
    TextEditor(text: $text1)
        .replaceDisabled(false)
    TextEditor(text: $text2)
}
.replaceDisabled(true)
```

## Parameters

- `isDisabled`: A Boolean value that indicates whether text   replacement in the find and replace interface is disabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/siritipview/replacedisabled(_:))*