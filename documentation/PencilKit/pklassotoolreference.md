# PKLassoToolReference

**Framework**: PencilKit  
**Kind**: class

A tool for selecting stroked lines and shapes in a canvas view.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class PKLassoToolReference
```

#### Overview

A [`PKLassoToolReference`](pklassotoolreference.md) object supports the selection of content on a [`PKCanvasView`](pkcanvasview.md). When active, the canvas uses incoming touch events to determine what content to add to the selection.

Create a lasso tool programmatically or display a [`PKToolPicker`](pktoolpicker.md) object from which the user selects the tool. Assign the resulting object to the [`tool`](pkcanvasview/tool-6str6.md) property of your [`PKCanvasView`](pkcanvasview.md) object. The canvas uses any subsequent touch sequences to select content on the canvas.

## Topics

### Creating a lasso tool
- [init()](pklassotoolreference/init.md)
  Creates a lasso tool object for selecting content on a canvas view.

## Relationships

### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pklassotoolreference)*