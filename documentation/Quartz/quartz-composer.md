# Quartz Composer

**Framework**: Quartz

**Availability**:
- macOS 10.4+

## Topics

### Classes
- [class QCComposition](qccomposition.md)
  The `QCComposition` class represents a Quartz Composer composition that either:
- [class QCCompositionLayer](qccompositionlayer.md)
  A layer that loads, plays, and controls Quartz Composer compositions in a Core Animation layer hierarchy.
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
### Protocols
- [QCCompositionParameterViewDelegate](qccompositionparameterviewdelegate.md)
  A protocol for composition parameter view’s delegate.
- [QCCompositionPickerViewDelegate](qccompositionpickerviewdelegate.md)
  The `QCCompositionPickerViewDelegate` informal protocol defines methods that allow  your application to respond to changes in a composition picker view (a [`QCCompositionPickerView`](qccompositionpickerview.md) object).
- [protocol QCCompositionRenderer](qccompositionrenderer.md)
  The `QCRenderer` protocol defines the methods used to pass data to the input ports or retrieve data from the output ports of the root patch of a Quartz Composer composition. This protocol is adopted by the [`QCRenderer`](qcrenderer.md), [`QCView`](qcview.md), and [`QCCompositionLayer`](qccompositionlayer.md) classes.
- [protocol QCPlugInContext](qcplugincontext.md)
  The `QCPlugInContext` protocol defines methods that you use only from within the execution method ([`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md)) of a `QCPlugIn` object.
- [protocol QCPlugInInputImageSource](qcplugininputimagesource.md)
  The `QCPlugInInputImageSource` protocol eliminates the need to use explicit image types for the image input ports on your custom patch. Not only does using the protocol avoid restrictions of a specific image type, but it avoids impedance mismatches, and provides better performance by deferring pixel computation until it is needed. When you need to access the pixels in an image, you simply convert the image to a representation (texture or buffer) using one of the methods defined by the `QCPlugInInputImageSource` protocol. Use a texture representation when you want to use input images on the GPU. Use a buffer representation when you want to use input images on the CPU.
- [protocol QCPlugInOutputImageProvider](qcpluginoutputimageprovider.md)
  The `QCPlugInOuputImageProvider` protocol eliminates the need to use explicit image types for the image output ports on a custom patch. The methods in this protocol are called by the Quartz Composer engine when the output image is needed. If your custom patch has an image output port, you need to implement the appropriate methods for rendering image data and to supply information about the rendering destination and the image bounds.
### Structures
- [struct QCPlugInExecutionMode](qcpluginexecutionmode.md)
  Execution modes for custom patches.
- [struct QCPlugInTimeMode](qcplugintimemode.md)
  Time modes for custom patches.
### Reference
- [Quartz Data Types](quartz-data-types.md)
- [Quartz Constants](quartz-constants.md)
- [Quartz Enumerations](quartz-enumerations.md)
- [Quartz Composer Constants](quartz-composer-constants.md)
- [Quartz Composer Enumerations](quartz-composer-enumerations.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/quartz-composer)*