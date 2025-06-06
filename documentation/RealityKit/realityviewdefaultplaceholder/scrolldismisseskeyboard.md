# scrollDismissesKeyboard(_:)

**Framework**: RealityKit  
**Kind**: method

Configures the behavior in which scrollable content interacts with the software keyboard.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
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

You use this modifier to customize how scrollable content interacts with the software keyboard. For example, you can specify a value of `ScrollDismissesKeyboardMode/immediately` to indicate that you would like scrollable content to immediately dismiss the keyboard if present when a scroll drag gesture begins.

```None
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

You can also use this modifier to customize the keyboard dismissal behavior for other kinds of scrollable views, like a `List` or a `TextEditor`.

By default, a `TextEditor` is interactive while other kinds of scrollable content always dismiss the keyboard on a scroll when linked against iOS 16 or later. Pass a value of `ScrollDismissesKeyboardMode/never` to indicate that scrollable content should never automatically dismiss the keyboard.

## Parameters

- `mode`: The keyboard dismissal mode that scrollable content   uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewdefaultplaceholder/scrolldismisseskeyboard(_:))*