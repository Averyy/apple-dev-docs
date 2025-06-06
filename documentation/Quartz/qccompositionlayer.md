# QCCompositionLayer

**Framework**: Quartz  
**Kind**: class

A layer that loads, plays, and controls Quartz Composer compositions in a Core Animation layer hierarchy.

**Availability**:
- macOS 10.5+

## Declaration

```swift
class QCCompositionLayer
```

#### Overview

The composition tracks the Core Animation layer time and is rendered directly at the current dimensions of the [`QCCompositionLayer`](qccompositionlayer.md) object.

An archived `QCCompositionLayer` object saves the composition that’s loaded at the time the layer is archived. It detects layer usage and pauses or resumes the composition appropriately. A `QCCompositionLayer` object starts rendering the composition automatically when the layer is placed in a visible layer hierarchy. The layer stops rendering when it is hidden or removed from the visible layer hierarchy.

You can pass data to the input ports, or retrieve data from the output ports, of the root patch of a composition by accessing the `patch` attribute of the `QCCompositionLayer` instance using methods provided by the [`QCCompositionRenderer`](qccompositionrenderer.md) protocol.

> **Note**:  You must not modify the `asynchronous` property of the superclass [`CAOpenGLLayer`](https://developer.apple.com/documentation/QuartzCore/CAOpenGLLayer).

 You must not modify the `asynchronous` property of the superclass [`CAOpenGLLayer`](https://developer.apple.com/documentation/QuartzCore/CAOpenGLLayer).

## Topics

### Creating a Composition Layer
- [init!(file: String!)](qccompositionlayer/init(file:).md)
  Initializes and returns a composition layer using the Quartz Composer composition in the specified file.
- [init!(composition: QCComposition!)](qccompositionlayer/init(composition:).md)
  Initializes and returns a  composition layer using the provided Quartz Composer composition.
### Getting the Composition
- [func composition() -> QCComposition!](qccompositionlayer/composition.md)
  Returns the composition associated with the layer.

## Relationships

### Inherits From
- [CAOpenGLLayer](../QuartzCore/CAOpenGLLayer.md)
### Conforms To
- [CAMediaTiming](../QuartzCore/CAMediaTiming.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [QCCompositionRenderer](qccompositionrenderer.md)

## See Also

- [class QCComposition](qccomposition.md)
  The `QCComposition` class represents a Quartz Composer composition that either:
- [class QCCompositionParameterView](qccompositionparameterview.md)
  A class that allows users to edit the input parameters of a composition in real time. The composition can be rendering in any of the following objects: [`QCRenderer`](qcrenderer.md), [`QCView`](qcview.md), or [`QCCompositionLayer`](qccompositionlayer.md).
- [class QCCompositionPickerPanel](qccompositionpickerpanel.md)
  The `QCCompositionPickerPanel` class represents a utility window that allows users to browse compositions that are in the Quartz Composer composition repository and, if supported, preview the composition. The `QCCompositionPickerPanel` class cannot be subclassed.
- [class QCCompositionPickerView](qccompositionpickerview.md)
  The `QCCompositionPickerView` class allows users to browse compositions that are in the Quartz Composer composition repository, and to preview them. You can set the default input parameters for a composition preview  by using the method setDefaultValue:forInputKey:.
- [class QCCompositionRepository](qccompositionrepository.md)
  The `QCCompositionRepository` class represents a system-wide centralized repository of built-in and installed Quartz Composer compositions (`/Library/Compositions` and `~/Library/Compositions`). The `QCCompositionRepository` class cannot be subclassed.
- [class QCPatchController](qcpatchcontroller.md)
- [class QCPlugIn](qcplugin.md)
  A base class to subclass for writing custom patches.
- [class QCPlugInViewController](qcpluginviewcontroller.md)
  The `QCPlugInViewController` class communicates (through Cocoa bindings) between a custom patch and the view used for the internal settings of the custom patch. Only custom patches that use internal settings exposed to the user need to use the `QCPlugInViewController` class.
- [class QCRenderer](qcrenderer.md)
  A base class for low-level rendering.
- [class QCView](qcview.md)
  The `QCView` class is a custom `NSView` class that loads, plays, and controls Quartz Composer compositions. It is an autonomous view that is driven by an internal timer running on the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionlayer)*