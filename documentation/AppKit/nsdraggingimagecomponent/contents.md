# contents

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An object providing the image contents of the component.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var contents: Any? { get set }
```

```objc
@property (strong, nullable) id contents;
```

#### Discussion

Typically you set an [`NSImage`](../nsimage.md) instance or a [`CGImage`](../../CoreGraphics/cgimage.md) as content.

## See Also

### Dragging Image Contents
- [var frame: NSRect](./frame.md)
  The coordinate space is the bounds of the parent dragging item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdraggingimagecomponent/contents)*