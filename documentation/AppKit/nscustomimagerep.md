# NSCustomImageRep

**Framework**: AppKit  
**Kind**: class

An object that uses a delegate object to render an image from a custom format.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSCustomImageRep
```

#### Overview

When called upon to produce an image, an [`NSCustomImageRep`](nscustomimagerep.md) sends a message to its delegate to do the actual drawing. You can use this class to support custom image formats without going to the trouble of subclassing [`NSImageRep`](nsimagerep.md) directly.

## Topics

### Creating Representations of Images in Custom Formats
- [init(draw: Selector, delegate: Any)](nscustomimagerep/init(draw:delegate:).md)
  Returns a representation of an image initialized with the specified delegate information.
- [init(size: NSSize, flipped: Bool, drawingHandler: (NSRect) -> Bool)](nscustomimagerep/init(size:flipped:drawinghandler:).md)
  Initializes a representation of an image of the specified size and flipped status, using a block to draw its content.
### Getting Drawing Handlers
- [var drawingHandler: ((NSRect) -> Bool)?](nscustomimagerep/drawinghandler.md)
  The destination rectangle of the drawing handler block.
### Getting Information About Images
- [var delegate: AnyObject?](nscustomimagerep/delegate.md)
  The delegate object that renders the image for the image representation.
- [var drawSelector: Selector?](nscustomimagerep/drawselector.md)
  The selector for the delegate’s drawing method.

## Relationships

### Inherits From
- [NSImageRep](nsimagerep.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscustomimagerep)*