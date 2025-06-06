# truncationMode(_:)

**Framework**: ManagedAppDistribution  
**Kind**: method

Sets the truncation mode for lines of text that are too long to fit in the available space.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func truncationMode(_ mode: Text.TruncationMode) -> some View
```

#### Return Value

A view that truncates text at different points in a line depending on the mode you select.

#### Discussion

Use the `truncationMode(_:)` modifier to determine whether text in a long line is truncated at the beginning, middle, or end. Truncation is indicated by adding an ellipsis (…) to the line when removing text to indicate to readers that text is missing.

In the example below, the bounds of text view constrains the amount of text that the view displays and the `truncationMode(_:)` specifies from which direction and where to display the truncation indicator:

```None
Text("This is a block of text that will show up in a text element as multiple lines. The text will fill the available space, and then, eventually, be truncated.")
    .frame(width: 150, height: 150)
    .truncationMode(.tail)
```

## Parameters

- `mode`: The truncation mode that specifies where to truncate   the text within the text view, if needed. You can truncate at the   beginning, middle, or end of the text view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/managedappdistribution/managedappview/truncationmode(_:))*