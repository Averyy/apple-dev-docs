# QCCompositionRenderer

**Framework**: Quartz  
**Kind**: protocol

The `QCRenderer` protocol defines the methods used to pass data to the input ports or retrieve data from the output ports of the root patch of a Quartz Composer composition. This protocol is adopted by the [`QCRenderer`](qcrenderer.md), [`QCView`](qcview.md), and [`QCCompositionLayer`](qccompositionlayer.md) classes.

**Availability**:
- macOS 10.4+

## Declaration

```swift
protocol QCCompositionRenderer
```

## Topics

### Passing and Retrieving Values From a Composition
- [func setValue(Any!, forInputKey: String!) -> Bool](qccompositionrenderer/setvalue(_:forinputkey:).md)
  Sets the value for an input port of a composition.
- [func value(forInputKey: String!) -> Any!](qccompositionrenderer/value(forinputkey:).md)
  Returns the value for an input port of a composition.
- [func value(forOutputKey: String!) -> Any!](qccompositionrenderer/value(foroutputkey:).md)
  Returns the value for an output port of a composition.
- [func value(forOutputKey: String!, ofType: String!) -> Any!](qccompositionrenderer/value(foroutputkey:oftype:).md)
  Returns the current value on an output port (identified by its key) of the root patch of the composition.
### Getting Input and Output Keys
- [func inputKeys() -> [Any]!](qccompositionrenderer/inputkeys.md)
  Returns an array that contains the keys that identify the input ports of the root patch of the composition.
- [func outputKeys() -> [Any]!](qccompositionrenderer/outputkeys.md)
  Returns an array that contains the keys that identify the output ports of the root patch of the composition.
### Getting Attributes
- [func attributes() -> [AnyHashable : Any]!](qccompositionrenderer/attributes.md)
  Returns the attributes of the composition associated with the renderer.
### Storing Arbitrary Information
- [func userInfo() -> NSMutableDictionary!](qccompositionrenderer/userinfo.md)
  Returns a mutable dictionary for storing arbitrary information.
### Saving and Restoring Input Values
- [func propertyListFromInputValues() -> Any!](qccompositionrenderer/propertylistfrominputvalues.md)
  Returns a property list object that represents the current values for all the input keys of the composition.
- [func setInputValuesWithPropertyList(Any!)](qccompositionrenderer/setinputvalueswithpropertylist(_:).md)
  Sets the values for the input keys of the composition from a previously saved property list.

## Relationships

### Conforming Types
- [QCCompositionLayer](qccompositionlayer.md)
- [QCRenderer](qcrenderer.md)
- [QCView](qcview.md)

## See Also

- [QCCompositionParameterViewDelegate](qccompositionparameterviewdelegate.md)
  A protocol for composition parameter view’s delegate.
- [QCCompositionPickerViewDelegate](qccompositionpickerviewdelegate.md)
  The `QCCompositionPickerViewDelegate` informal protocol defines methods that allow  your application to respond to changes in a composition picker view (a [`QCCompositionPickerView`](qccompositionpickerview.md) object).
- [protocol QCPlugInContext](qcplugincontext.md)
  The `QCPlugInContext` protocol defines methods that you use only from within the execution method ([`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md)) of a `QCPlugIn` object.
- [protocol QCPlugInInputImageSource](qcplugininputimagesource.md)
  The `QCPlugInInputImageSource` protocol eliminates the need to use explicit image types for the image input ports on your custom patch. Not only does using the protocol avoid restrictions of a specific image type, but it avoids impedance mismatches, and provides better performance by deferring pixel computation until it is needed. When you need to access the pixels in an image, you simply convert the image to a representation (texture or buffer) using one of the methods defined by the `QCPlugInInputImageSource` protocol. Use a texture representation when you want to use input images on the GPU. Use a buffer representation when you want to use input images on the CPU.
- [protocol QCPlugInOutputImageProvider](qcpluginoutputimageprovider.md)
  The `QCPlugInOuputImageProvider` protocol eliminates the need to use explicit image types for the image output ports on a custom patch. The methods in this protocol are called by the Quartz Composer engine when the output image is needed. If your custom patch has an image output port, you need to implement the appropriate methods for rendering image data and to supply information about the rendering destination and the image bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrenderer)*