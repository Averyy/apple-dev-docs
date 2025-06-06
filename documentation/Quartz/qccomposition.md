# QCComposition

**Framework**: Quartz  
**Kind**: class

The `QCComposition` class represents a Quartz Composer composition that either:

**Availability**:
- macOS 10.4+

## Declaration

```swift
class QCComposition
```

#### Overview

- comes from the system-wide composition repository  (`/Library/Compositions` and `~/Library/Compositions`) where it can be accessed by any application through the methods of the [`QCCompositionRepository`](qccompositionrepository.md) class
- is created from an arbitrary source (typically a file on disk) using one of its methods

This class cannot be subclassed.

A `QCComposition` object has the following information associated with it and that you can obtain by using the appropriate method of the `QCComposition` class:

- Attributes include the name and description of the composition, copyright information, and whether or not its provided by macOS (built-in).
- The protocols that the composition conforms to. A   defines a set of required and optional input parameters and output results.

Many methods of the [`QCRenderer`](qcrenderer.md), [`QCCompositionLayer`](qccompositionlayer.md), and [`QCView`](qcview.md) classes take a `QCComposition` object as a parameter.

## Topics

### Creating a Composition
- [init!(file: String!)](qccomposition/init(file:).md)
  Returns a composition object initialized with a Quartz Composer composition file.
- [init!(data: Data!)](qccomposition/init(data:).md)
  Returns a composition object  initialized with the contents of a Quartz Composer composition file.
### Getting Information About a Composition
- [func attributes() -> [AnyHashable : Any]!](qccomposition/attributes.md)
  Returns the attributes of the composition.
- [func protocols() -> [Any]!](qccomposition/protocols.md)
  Returns the list of protocols to which the composition conforms.
- [func identifier() -> String!](qccomposition/identifier.md)
  Returns the unique and persistent identifier for the composition from the composition repository.
### Getting Port Keys
- [func inputKeys() -> [Any]!](qccomposition/inputkeys.md)
  Returns an array listing the keys that identify the input ports of the root patch of the composition.
- [func outputKeys() -> [Any]!](qccomposition/outputkeys.md)
  Returns an array listing the keys that identify the output ports of the root patch of the composition.
### Constants
- [Attribute Keys](attribute-keys.md)
  Attributes of a composition.
- [Composition Categories](composition-categories.md)
  Categories for compositions.
- [Standard Protocol Input Keys](standard-protocol-input-keys.md)
  Input ports of a composition.
- [Standard Protocol Output Keys](standard-protocol-output-keys.md)
  Output ports of a composition.
- [Standard Protocols](standard-protocols.md)
  Protocols for a composition.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccomposition)*