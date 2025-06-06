# scrollDismissesKeyboard(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures the behavior in which scrollable content interacts with the software keyboard.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+

## Declaration

```swift
nonisolated
func scrollDismissesKeyboard(_ mode: ScrollDismissesKeyboardMode) -> some View
```

#### Return Value

A view that uses the specified keyboard dismissal mode.

#### Discussion

You use this modifier to customize how scrollable content interacts with the software keyboard. For example, you can specify a value of [`immediately`](scrolldismisseskeyboardmode/immediately.md) to indicate that you would like scrollable content to immediately dismiss the keyboard if present when a scroll drag gesture begins.

```swift
@State private var text = ""

ScrollView {
    TextField("Prompt", text: $text)
    ForEach(0 ..< 50) { index in
        Text("\(index)")
            .padding()
    }
}
.scrollDismissesKeyboard(.immediately)
```

You can also use this modifier to customize the keyboard dismissal behavior for other kinds of scrollable views, like a [`List`](list.md) or a [`TextEditor`](texteditor.md).

By default, a [`TextEditor`](texteditor.md) is interactive while other kinds of scrollable content always dismiss the keyboard on a scroll when linked against iOS 16 or later. Pass a value of [`never`](scrolldismisseskeyboardmode/never.md) to indicate that scrollable content should never automatically dismiss the keyboard.

## Parameters

- `mode`: The keyboard dismissal mode that scrollable content   uses.

## See Also

- [var scrollDismissesKeyboardMode: ScrollDismissesKeyboardMode](environmentvalues/scrolldismisseskeyboardmode.md)
  The way that scrollable content interacts with the software keyboard.
- [struct ScrollDismissesKeyboardMode](scrolldismisseskeyboardmode.md)
  The ways that scrollable content can interact with the software keyboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/scrolldismisseskeyboard(_:))*