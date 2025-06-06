# draggingImageComponents(withFrame:in:)

**Framework**: Appkit  
**Kind**: method

Generates dragging image components with the specified frame in the view.

**Availability**:
- macOS 10.7+

## Declaration

```swift
@MainActor
func draggingImageComponents(withFrame frame: NSRect, in view: NSView) -> [NSDraggingImageComponent]
```

#### Return Value

An array of [`NSDraggingImageComponent`](nsdraggingimagecomponent.md) objects representing the cell.

#### Discussion

The default implementation generates an image from the cell and return two components: one for [`label`](nsdraggingitem/imagecomponentkey/label.md) and another for [`icon`](nsdraggingitem/imagecomponentkey/icon.md). This is done by capturing the portion from the [`titleRect(forBounds:)`](nscell/titlerect(forbounds:).md) and [`imageRect(forBounds:)`](nscell/imagerect(forbounds:).md) methods respectively.

This method can be subclassed and overridden to provide a custom set of [`NSDraggingImageComponent`](nsdraggingimagecomponent.md) to create the drag image for the cell. This method is generally used by NSTableView/NSOutlineView.

> **Note**:  NSCell currently has an issue where it will return an empty array from `draggingImageComponentsWithFrame:inView:` if the cell does not have an image portion. To work around this, subclass NSCell and override `draggingImageComponentsWithFrame:inView:` and generate your own [`NSDraggingImageComponent`](nsdraggingimagecomponent.md) in the returned array.

## Parameters

- `frame`: The bounding rectangle of the receiver.
- `view`: The view that manages the cell.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscell/draggingimagecomponents(withframe:in:))*