# suggestedFrameForInserting(contentInFrame:)

**Framework**: PaperKit  
**Kind**: method

Returns the suggested frame for inserting shapes and other content.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@preconcurrency func suggestedFrameForInserting(contentInFrame frame: CGRect) -> CGRect
```

#### Return Value

The suggested frame for the content. Use this value to transform a `PaperMarkup` before inserting it.

#### Discussion

```swift
var shapeFrame = CGRect(x: 100, y: 100, width: 300, height: 300)
// Get the default frame for inserting, and insert the shape there.
let suggestedFrame = paperViewController.suggestedFrameForInserting(contentInFrame: shapeFrame)
paperViewController.markup.insertNewShape(configuration: shapeConfiguration, frame: suggestedFrame)
```

## Parameters

- `frame`: The frame of the content you want to insert.

## See Also

- [var selection: Set<MarkupOrderedSet.ElementID>](papermarkupviewcontroller/selection.md)
  The current selected elements on the canvas.
- [var selectedMarkup: PaperMarkup](papermarkupviewcontroller/selectedmarkup.md)
  The selected contents in the UI.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/suggestedframeforinserting(contentinframe:))*