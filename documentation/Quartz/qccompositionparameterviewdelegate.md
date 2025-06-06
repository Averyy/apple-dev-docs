# QCCompositionParameterViewDelegate

**Framework**: Quartz

A protocol for composition parameter view’s delegate.

#### Overview

This informal protocol allows your application to define which parameters should be visible in a [`QCCompositionParameterView`](qccompositionparameterview.md) object.

## Topics

### Responding to Composition Selections
- [func compositionParameterView(_ parameterView: QCCompositionParameterView!, shouldDisplayParameterWithKey portKey: String!, attributes portAttributes: [AnyHashable : Any]! = [:]) -> Bool](../ObjectiveC/NSObject-swift.class/compositionParameterView(_:shouldDisplayParameterWithKey:attributes:).md)
  Allows you to define which composition parameters are visible in the user interface when the composition parameter view refreshes.
### Responding when an Input Parameter Changes
- [func compositionParameterView(_ parameterView: QCCompositionParameterView!, didChangeParameterWithKey portKey: String!)](../ObjectiveC/NSObject-swift.class/compositionParameterView(_:didChangeParameterWithKey:).md)
  Called after an input parameter in the composition parameter view has been edited.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionparameterviewdelegate)*