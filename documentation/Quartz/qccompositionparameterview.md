# QCCompositionParameterView

**Framework**: Quartz  
**Kind**: class

A class that allows users to edit the input parameters of a composition in real time. The composition can be rendering in any of the following objects: [`QCRenderer`](qcrenderer.md), [`QCView`](qcview.md), or [`QCCompositionLayer`](qccompositionlayer.md).

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
class QCCompositionParameterView
```

## Topics

### Getting and Setting the Renderer
- [func setCompositionRenderer((any QCCompositionRenderer)!)](qccompositionparameterview/setcompositionrenderer(_:).md)
  Sets the composition parameter view for editing the input parameters of the provided renderer object.
- [func compositionRenderer() -> (any QCCompositionRenderer)!](qccompositionparameterview/compositionrenderer.md)
  Returns the renderer object associated with the composition parameter view.
### Checking for Input Parameters
- [func hasParameters() -> Bool](qccompositionparameterview/hasparameters.md)
  Checks whether the composition that is currently edited by the composition parameter view has any input parameters.
### Setting and Retrieving the Delegate
- [func setDelegate(Any!)](qccompositionparameterview/setdelegate(_:).md)
  Sets the composition parameter view delegate.
- [func delegate() -> Any!](qccompositionparameterview/delegate.md)
  Returns the composition parameter view delegate.
### Managing Background Drawing
- [func setDrawsBackground(Bool)](qccompositionparameterview/setdrawsbackground(_:).md)
  Sets whether the composition parameter view draws its background.
- [func drawsBackground() -> Bool](qccompositionparameterview/drawsbackground.md)
  Returns whether the composition parameter view draws its background.
### Setting and Getting the Background Color
- [func setBackgroundColor(NSColor!)](qccompositionparameterview/setbackgroundcolor(_:).md)
  Sets the background color of the composition parameter view.
- [func backgroundColor() -> NSColor!](qccompositionparameterview/backgroundcolor.md)
  Retrieves the background color of the composition parameter view.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class QCComposition](qccomposition.md)
  The `QCComposition` class represents a Quartz Composer composition that either:
- [class QCCompositionLayer](qccompositionlayer.md)
  A layer that loads, plays, and controls Quartz Composer compositions in a Core Animation layer hierarchy.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionparameterview)*