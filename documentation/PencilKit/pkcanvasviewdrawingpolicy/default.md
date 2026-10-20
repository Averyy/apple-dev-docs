# PKCanvasViewDrawingPolicy.default

**Framework**: PencilKit  
**Kind**: case  
**Role**: Case

The default input type to use for drawing on a canvas.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- visionOS 1.0+

## Declaration

```swift
case `default`
```

```c
PKCanvasViewDrawingPolicyDefault
```

#### Discussion

By default, if the tool picker is visible, respect the pencil interaction setting of the [`prefersPencilOnlyDrawing`](../../UIKit/uipencilinteraction/preferspencilonlydrawing.md) property; otherwise only accept input from Apple Pencil.

## See Also

### Drawing policies
- [PKCanvasViewDrawingPolicy.anyInput](./anyinput.md)
  Allows drawing on the canvas from any input source.
- [PKCanvasViewDrawingPolicy.pencilOnly](./pencilonly.md)
  Pencil touches are the only input that draw on the canvas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkcanvasviewdrawingpolicy/default)*