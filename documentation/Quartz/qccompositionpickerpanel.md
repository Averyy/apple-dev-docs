# QCCompositionPickerPanel

**Framework**: Quartz  
**Kind**: class

The `QCCompositionPickerPanel` class represents a utility window that allows users to browse compositions that are in the Quartz Composer composition repository and, if supported, preview the composition. The `QCCompositionPickerPanel` class cannot be subclassed.

**Availability**:
- macOS 10.4+

## Declaration

```swift
@MainActor
class QCCompositionPickerPanel
```

## Topics

### Creating the Utility Window for Browsing Compositions
- [class func shared() -> QCCompositionPickerPanel!](qccompositionpickerpanel/shared.md)
  Returns the shared instance of the composition picker panel.
### Getting the Picker Panel View
- [func compositionPickerView() -> QCCompositionPickerView!](qccompositionpickerpanel/compositionpickerview.md)
  Returns the composition picker view used by the panel so that it can be configured.

## Relationships

### Inherits From
- [NSPanel](../AppKit/NSPanel.md)
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
- [NSMenuItemValidation](../AppKit/NSMenuItemValidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [NSUserInterfaceValidations](../AppKit/NSUserInterfaceValidations.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class QCComposition](qccomposition.md)
  The `QCComposition` class represents a Quartz Composer composition that either:
- [class QCCompositionLayer](qccompositionlayer.md)
  A layer that loads, plays, and controls Quartz Composer compositions in a Core Animation layer hierarchy.
- [class QCCompositionParameterView](qccompositionparameterview.md)
  A class that allows users to edit the input parameters of a composition in real time. The composition can be rendering in any of the following objects: [`QCRenderer`](qcrenderer.md), [`QCView`](qcview.md), or [`QCCompositionLayer`](qccompositionlayer.md).
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerpanel)*