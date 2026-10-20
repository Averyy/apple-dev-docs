# NSCustomImageRep

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An object that uses a delegate object to render an image from a custom format.

**Availability**:
- macOS

## Declaration

```swift
class NSCustomImageRep
```

```objc
@interface NSCustomImageRep : NSImageRep
```

#### Overview

When called upon to produce an image, an [`NSCustomImageRep`](./nscustomimagerep.md) sends a message to its delegate to do the actual drawing. You can use this class to support custom image formats without going to the trouble of subclassing [`NSImageRep`](./nsimagerep.md) directly.

## Topics

### Creating Representations of Images in Custom Formats
- [init(draw: Selector, delegate: Any)](./nscustomimagerep/init%28draw,delegate%29.md)
  Returns a representation of an image initialized with the specified delegate information.
- [init(size: NSSize, flipped: Bool, drawingHandler: (NSRect) -> Bool)](./nscustomimagerep/init%28size,flipped,drawinghandler%29.md)
  Initializes a representation of an image of the specified size and flipped status, using a block to draw its content.
### Getting Drawing Handlers
- [var drawingHandler: ((NSRect) -> Bool)?](./nscustomimagerep/drawinghandler.md)
  The destination rectangle of the drawing handler block.
### Getting Information About Images
- [var delegate: AnyObject?](./nscustomimagerep/delegate.md)
  The delegate object that renders the image for the image representation.
- [var drawSelector: Selector?](./nscustomimagerep/drawselector.md)
  The selector for the delegate’s drawing method.
### Initializers
- [init(drawSelector: Selector, delegate: Any)](./nscustomimagerep/init%28drawselector,delegate%29.md)

## Relationships

### Inherits From
- [NSImageRep](./nsimagerep.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscustomimagerep)*