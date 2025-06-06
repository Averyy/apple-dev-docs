# NSDraggingImageComponent

**Framework**: AppKit  
**Kind**: class

A single object in a dragging item.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class NSDraggingImageComponent
```

#### Overview

An array of [`NSDraggingImageComponent`](nsdraggingimagecomponent.md) instances are composited together to create the dragging image for an [`NSDraggingItem`](nsdraggingitem.md). [`NSDraggingImageComponent`](nsdraggingimagecomponent.md) instances can simply be considered as named images with a location used by an [`NSDraggingItem`](nsdraggingitem.md) instance.

## Topics

### Creating a Dragging Image Component
- [init(key: NSDraggingItem.ImageComponentKey)](nsdraggingimagecomponent/init(key:).md)
  Initializes and returns a dragging image component with the specified key.
### Dragging Image Component
- [var key: NSDraggingItem.ImageComponentKey](nsdraggingimagecomponent/key.md)
  The unique name of this image component instance.
### Dragging Image Contents
- [var contents: Any?](nsdraggingimagecomponent/contents.md)
  An object providing the image contents of the component.
- [var frame: NSRect](nsdraggingimagecomponent/frame.md)
  The coordinate space is the bounds of the parent dragging item.
### Constants
- [NSDragImage Component Keys](nsdragimage-component-keys.md)
  These constants are used by the [`init(key:)`](nsdraggingimagecomponent/init(key:).md), [`draggingImageComponentWithKey:`](nsdraggingimagecomponent/draggingimagecomponentwithkey:.md) methods and the [`key`](nsdraggingimagecomponent/key.md) property.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSDraggingSource](nsdraggingsource.md)
  A set of methods that are implemented by the source object in a dragging session.
- [class NSDraggingItem](nsdraggingitem.md)
  A single dragged item within a dragging session.
- [class NSDraggingSession](nsdraggingsession.md)
  The encapsulation of a drag-and-drop action that supports modification of the drag while in progress.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponent)*