# suggestedFrameForInserting(contentInFrame:)

**Framework**: PaperKit  
**Kind**: method

The frame that should be used for inserting shapes and other content.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency func suggestedFrameForInserting(contentInFrame frame: CGRect) -> CGRect
```

#### Return Value

The suggested frame for where the content should go. This can be used to transform a `PaperMarkup` before inserting it.

#### Discussion

```swift
var shapeFrame = CGRect(x: 100, y: 100, width: 300, height: 300)
// Get the default frame for inserting, and insert the shape there.
let suggestedFrame = paperViewController.suggestedFrameForInserting(contentInFrame: shapeFrame)
paperViewController.markup.insertNewShape(configuration: shapeConfiguration, frame: suggestedFrame)
```

## Parameters

- `frame`: The frame of the content to be inserted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/papermarkupviewcontroller/suggestedframeforinserting(contentinframe:))*