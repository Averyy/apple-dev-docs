# multilineTextAlignment(_:)

**Framework**: Journaling Suggestions  
**Kind**: method

Sets the alignment of a text view that contains multiple lines of text.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func multilineTextAlignment(_ alignment: TextAlignment) -> some View
```

#### Return Value

A view that aligns the lines of multiline `Text` instances it contains.

#### Discussion

Use this modifier to set an alignment for a multiline block of text. For example, the modifier centers the contents of the following `Text` view:

```None
Text("This is a block of text that shows up in a text element as multiple lines.\("\n") Here we have chosen to center this text.")
    .frame(width: 200)
    .multilineTextAlignment(.center)
```

The text in the above example spans more than one line because:

- The newline character introduces a line break.
- The frame modifier limits the space available to the text view, and by default a text view wraps lines that don’t fit in the available width. As a result, the text before the explicit line break wraps to three lines, and the text after uses two lines.

The modifier applies the alignment to the all the lines of text in the view, regardless of why wrapping occurs:

The modifier has no effect on a `Text` view that contains only one line of text, because a text view has a width that exactly matches the width of its widest line. If you want to align an entire text view rather than its contents, set the aligment of its container, like a `VStack` or a frame that you create with the `View/frame(minWidth:idealWidth:maxWidth:minHeight:idealHeight:maxHeight:alignment:)` modifier.

> **Note**: You can use this modifier to control the alignment of a `Text` view that you create with the `Text/init(_:style:)` initializer to display localized dates and times, including when the view uses only a single line, but only when that view appears in a widget.

You can use this modifier to control the alignment of a `Text` view that you create with the `Text/init(_:style:)` initializer to display localized dates and times, including when the view uses only a single line, but only when that view appears in a widget.

The modifier also affects the content alignment of other text container types, like `TextEditor` and `TextField`. In those cases, the modifier sets the alignment even when the view contains only a single line because view’s width isn’t dictated by the width of the text it contains.

The modifier operates by setting the `EnvironmentValues/multilineTextAlignment` value in the environment, so it affects all the text containers in the modified view hierarchy. For example, you can apply the modifier to a `VStack` to configure all the text views inside the stack.

## Parameters

- `alignment`: A value that you use to align multiple lines of   text within a view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/journalingsuggestions/journalingsuggestionspicker/multilinetextalignment(_:))*