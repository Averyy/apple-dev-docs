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
### Initializers
- [init(drawSelector: Selector, delegate: Any)](nscustomimagerep/init(drawselector:delegate:).md)

## Relationships

### Inherits From
- [NSImageRep](nsimagerep.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscustomimagerep)*