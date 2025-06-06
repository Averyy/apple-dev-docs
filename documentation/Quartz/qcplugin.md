# QCPlugIn

**Framework**: Quartz  
**Kind**: class

A base class to subclass for writing custom patches.

**Availability**:
- macOS 10.4+

## Declaration

```swift
class QCPlugIn
```

#### Overview

The `QCPlugIn` class provides the base class to subclass for writing custom  Quartz Composer patches. You implement a custom patch by subclassing `QCPlugIn`, overriding the appropriate methods, packaging the code as an `NSBundle` object, and installing the bundle in the appropriate location. A bundle can contain more than one subclass  of `QCPlugIn`, allowing you to provide a suite of custom patches in one bundle. [`Quartz Composer Custom Patch Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzComposer_Patch_PlugIn_ProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004787) provides detailed instructions on how to create and package a custom patch.  supplements the information in the programming guide.

The methods related to the executing the custom patch (called when the Quartz Composer engine is rendering) are passed an opaque object that conforms to the [`QCPlugInContext`](qcplugincontext.md) protocol. This object represents the execution context of the `QCPlugIn` object. You should not retain the execution context or use it outside of the scope of the execution method that it is passed to.

## Topics

### Defining the Characteristics of a Custom Patch
- [class func executionMode() -> QCPlugInExecutionMode](qcplugin/executionmode.md)
  Returns the execution mode of the custom patch.
- [class func timeMode() -> QCPlugInTimeMode](qcplugin/timemode.md)
  Returns the time mode for the custom patch.
### Executing a Custom Patch
- [func execute((any QCPlugInContext)!, atTime: TimeInterval, withArguments: [AnyHashable : Any]!) -> Bool](qcplugin/execute(_:attime:witharguments:).md)
  Performs the processing or rendering tasks appropriate for the custom patch.
### Performing Custom Tasks During Execution
- [func startExecution((any QCPlugInContext)!) -> Bool](qcplugin/startexecution(_:).md)
  Allows you to perform custom setup tasks before the Quartz Composer engine starts rendering.
- [func enableExecution((any QCPlugInContext)!)](qcplugin/enableexecution(_:).md)
  Allows you to perform custom tasks when the execution of the `QCPlugIn` object is resumed.
- [func disableExecution((any QCPlugInContext)!)](qcplugin/disableexecution(_:).md)
  Allows you to perform custom tasks when the execution of the `QCPlugIn` object is paused.
- [func stopExecution((any QCPlugInContext)!)](qcplugin/stopexecution(_:).md)
  Allows you to perform custom tasks when the `QCPlugIn` object stops executing.
### Defining Patch and Property Port Attributes
- [class func attributes() -> [AnyHashable : Any]!](qcplugin/attributes.md)
  Returns a dictionary that contains strings for the user interface that describe the custom patch.
- [class func attributesForPropertyPort(withKey: String!) -> [AnyHashable : Any]!](qcplugin/attributesforpropertyport(withkey:).md)
  Returns a dictionary that contains strings for the user interface that describe the optional attributes for ports created from properties.
### Defining Internal Settings
- [func createViewController() -> QCPlugInViewController!](qcplugin/createviewcontroller.md)
  Creates and returns a view controller for the Settings pane of a custom patch.
- [class func plugInKeys() -> [Any]!](qcplugin/pluginkeys.md)
  Returns the keys for the internal settings of a custom patch.
### Supporting Saving and Retrieving Internal Settings
- [func serializedValue(forKey: String!) -> Any!](qcplugin/serializedvalue(forkey:).md)
  A method implemented to override serialization.
- [func setSerializedValue(Any!, forKey: String!)](qcplugin/setserializedvalue(_:forkey:).md)
  Provides custom deserialization for patch internal settings that were previously serialized using the method [`serializedValue(forKey:)`](qcplugin/serializedvalue(forkey:).md).
### Adding Ports Dynamically
- [func addInputPort(withType: String!, forKey: String!, withAttributes: [AnyHashable : Any]!)](qcplugin/addinputport(withtype:forkey:withattributes:).md)
  Adds an input port of the specified type and associates a key and attributes with the port.
- [func removeInputPort(forKey: String!)](qcplugin/removeinputport(forkey:).md)
  Removes the input port for a given key.
- [func addOutputPort(withType: String!, forKey: String!, withAttributes: [AnyHashable : Any]!)](qcplugin/addoutputport(withtype:forkey:withattributes:).md)
  Adds an output port of the specified type and associates a key and attributes with the port.
- [func removeOutputPort(forKey: String!)](qcplugin/removeoutputport(forkey:).md)
  Removes the output port for a given key.
### Getting and Setting Port Values
- [func didValue(forInputKeyChange: String!) -> Bool](qcplugin/didvalue(forinputkeychange:).md)
  Returns whether the input port value changed since the last execution of the custom patch.
- [func value(forInputKey: String!) -> Any!](qcplugin/value(forinputkey:).md)
  Returns the current value for an input port.
- [func setValue(Any!, forOutputKey: String!) -> Bool](qcplugin/setvalue(_:foroutputkey:).md)
  Sets the value of an output port.
### Loading Bundle and Custom Patches Manually
- [class func load(atPath: String!) -> Bool](qcplugin/load(atpath:).md)
  Loads a Quartz Composer plug-in bundle from the specified path.
- [class func registerClass(AnyClass!)](qcplugin/registerclass(_:).md)
  Registers a `QCPlugIn` subclass.
### Ordering Property Ports
- [class func sortedPropertyPortKeys() -> [Any]!](qcplugin/sortedpropertyportkeys.md)
  Returns and array of property port keys in the order you want them to appear in the user interface.
### Constants
- [Patch Attributes](patch-attributes.md)
  Attributes for custom patches.
- [Input and Output Port Attributes](input-and-output-port-attributes.md)
  Attributes for input and output ports.
- [Port Input and Output Types](port-input-and-output-types.md)
  Data types for input and output ports.
- [Pixel Formats](pixel-formats.md)
  Supported image pixel formats.
- [Execution Arguments](execution-arguments.md)
  Arguments to the method [`execute(_:atTime:withArguments:)`](qcplugin/execute(_:attime:witharguments:).md).
- [struct QCPlugInExecutionMode](qcpluginexecutionmode.md)
  Execution modes for custom patches.
- [struct QCPlugInTimeMode](qcplugintimemode.md)
  Time modes for custom patches.
### Instance Methods
- [func executionTime(for: (any QCPlugInContext)!, atTime: TimeInterval, withArguments: [AnyHashable : Any]!) -> TimeInterval](qcplugin/executiontime(for:attime:witharguments:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Quartz Composer Custom Patch Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/QuartzComposer_Patch_PlugIn_ProgGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004787)
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
- [class QCPlugInViewController](qcpluginviewcontroller.md)
  The `QCPlugInViewController` class communicates (through Cocoa bindings) between a custom patch and the view used for the internal settings of the custom patch. Only custom patches that use internal settings exposed to the user need to use the `QCPlugInViewController` class.
- [class QCRenderer](qcrenderer.md)
  A base class for low-level rendering.
- [class QCView](qcview.md)
  The `QCView` class is a custom `NSView` class that loads, plays, and controls Quartz Composer compositions. It is an autonomous view that is driven by an internal timer running on the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qcplugin)*