# init(textLineRects:)

**Framework**: UIKit  
**Kind**: init

Creates a preview parameters object with information about the text you want to preview.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
convenience init(textLineRects: [NSValue])
```

#### Return Value

A new preview parameters object for a view containing text.

## Parameters

- `textLineRects`: An array of text line rectangles in the coordinate system of the view being animated. UIKit clips the previewed content using the specified rectangles. Wrap each   in an   object. If you specify an empty array, UIKit shows the entire view.

## See Also

- [init()](uipreviewparameters/init.md)
  Creates a default set of preview parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipreviewparameters/init(textlinerects:))*