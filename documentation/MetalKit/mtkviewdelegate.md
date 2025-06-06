# MTKViewDelegate

**Framework**: MetalKit  
**Kind**: protocol

Methods for responding to a MetalKit view’s drawing and resizing events.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
protocol MTKViewDelegate : NSObjectProtocol
```

#### Overview

You can set an object that implements the [`MTKViewDelegate`](mtkviewdelegate.md) protocol as a [`MTKView`](mtkview.md) object’s delegate. Use a delegate to provide a drawing method to a [`MTKView`](mtkview.md) object and respond to rendering events without subclassing the [`MTKView`](mtkview.md) class.

## Topics

### Changing the View’s Layout
- [func mtkView(MTKView, drawableSizeWillChange: CGSize)](mtkviewdelegate/mtkview(_:drawablesizewillchange:).md)
  Updates the view’s contents upon receiving a change in layout, resolution, or size.
### Drawing the View’s Contents
- [func draw(in: MTKView)](mtkviewdelegate/draw(in:).md)
  Draws the view’s contents.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MTKView](mtkview.md)
  A specialized view that creates, configures, and displays Metal objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkviewdelegate)*