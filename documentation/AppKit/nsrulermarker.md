# NSRulerMarker

**Framework**: AppKit  
**Kind**: class

A symbol on a ruler view, indicating a location for the graphics element it represents in the client of the ruler view.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSRulerMarker
```

#### Overview

An example of a marker is the representation of a margin or tab setting, or the edges of a graphic on the page.

## Topics

### Creating instances
- [init(rulerView: NSRulerView, markerLocation: CGFloat, image: NSImage, imageOrigin: NSPoint)](nsrulermarker/init(rulerview:markerlocation:image:imageorigin:).md)
  Initializes a newly allocated ruler marker, associating it with (but not adding it to) a specified ruler view and assigning the attributes provided.
### Getting the ruler view
- [var ruler: NSRulerView?](nsrulermarker/ruler.md)
  The receiver’s ruler view.
### Setting the image
- [var image: NSImage](nsrulermarker/image.md)
  The receiver’s image.
- [var imageOrigin: NSPoint](nsrulermarker/imageorigin.md)
  The point in the receiver’s image that is positioned at the receiver’s location on the ruler view.
- [var imageRectInRuler: NSRect](nsrulermarker/imagerectinruler.md)
  The rectangle occupied by the receiver’s image.
- [var thicknessRequiredInRuler: CGFloat](nsrulermarker/thicknessrequiredinruler.md)
  The amount of the receiver’s image that’s displayed above or to the left of the ruler view’s baseline.
### Setting movability
- [var isMovable: Bool](nsrulermarker/ismovable.md)
  A Boolean that indicates whether the user can move the receiver in its ruler view.
- [var isRemovable: Bool](nsrulermarker/isremovable.md)
  A Boolean that indicates whether the user can remove the receiver from its ruler view.
### Setting the location
- [var markerLocation: CGFloat](nsrulermarker/markerlocation.md)
  The location of the receiver in the coordinate system of the ruler view’s client view.
### Setting the represented object
- [var representedObject: (any NSCopying)?](nsrulermarker/representedobject.md)
  The object the receiver represents.
### Drawing and event handling
- [func draw(NSRect)](nsrulermarker/draw(_:).md)
  Draws the receiver’s image that appears in the supplied rectangle.
- [var isDragging: Bool](nsrulermarker/isdragging.md)
  A Boolean that indicates whether the receiver is being dragged.
- [func trackMouse(with: NSEvent, adding: Bool) -> Bool](nsrulermarker/trackmouse(with:adding:).md)
  Handles user manipulation of the receiver in its ruler view.
### Initializers
- [init(coder: NSCoder)](nsrulermarker/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSRulerView](nsrulerview.md)
  A ruler and the markers above or to the side of a scroll view’s document view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrulermarker)*