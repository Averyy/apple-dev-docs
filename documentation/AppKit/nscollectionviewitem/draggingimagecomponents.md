# draggingImageComponents

**Framework**: AppKit  
**Kind**: property

Dragging images for multi-image drag and drop support.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
var draggingImageComponents: [NSDraggingImageComponent] { get }
```

#### Discussion

The component frames are relative to a coordinate system that has its origin at the bottom left, so you need to take into account the flipped state of your view when computing the component frames.

This methods can be subclassed and overridden to provide a custom set of [`NSDraggingImageComponent`](nsdraggingimagecomponent.md) objects to create the drag image.

The default implementation will return an array of up to two [`NSDraggingImageComponent`](nsdraggingimagecomponent.md) instances – one for the [`imageView`](nscollectionviewitem/imageview.md) and another for the [`textField`](nscollectionviewitem/textfield.md) (if not `nil`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewitem/draggingimagecomponents)*