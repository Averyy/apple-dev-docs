# fixedSize(horizontal:vertical:)

**Framework**: App Intents  
**Kind**: method

Fixes this view at its ideal size in the specified dimensions.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
nonisolated
func fixedSize(horizontal: Bool, vertical: Bool) -> some View
```

#### Return Value

A view that fixes this view at its ideal size in the dimensions specified by `horizontal` and `vertical`.

#### Discussion

This function behaves like `View/fixedSize()`, except with `fixedSize(horizontal:vertical:)` the fixing of the axes can be optionally specified in one or both dimensions. For example, if you horizontally fix a text view before wrapping it in the frame view, you’re telling the text view to maintain its ideal . The view calculates this to be the space needed to represent the entire string.

```swift
Text("A single line of text, too long to fit in a box.")
    .fixedSize(horizontal: true, vertical: false)
    .frame(width: 200, height: 200)
    .border(Color.gray)
```

This can result in the view exceeding the parent’s bounds, which may or may not be the effect you want.

## Parameters

- `horizontal`: A Boolean value that indicates whether to fix the width   of the view.
- `vertical`: A Boolean value that indicates whether to fix the height   of the view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/shortcutslink/fixedsize(horizontal:vertical:))*