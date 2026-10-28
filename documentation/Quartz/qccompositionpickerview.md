# QCCompositionPickerView

**Framework**: Quartz  
**Kind**: class  
**Role**: Class

The `QCCompositionPickerView` class allows users to browse compositions that are in the Quartz Composer composition repository, and to preview them. You can set the default input parameters for a composition preview  by using the method setDefaultValue:forInputKey:.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class QCCompositionPickerView
```

```objc
@interface QCCompositionPickerView : NSView
```

## Overview

Note that the composition picker view does not automatically refresh its content when the composition repository is updated. It’s your responsibility to perform any necessary updating.

## Topics

### Setting and Getting the Background Color
- [func setBackgroundColor(NSColor!)](./qccompositionpickerview/setbackgroundcolor%28_%29.md)
  Sets the background color for the composition picker view.
- [func backgroundColor() -> NSColor!](./qccompositionpickerview/backgroundcolor%28%29.md)
  Returns the background color of the composition picker view.
### Managing Background Drawing
- [func setDrawsBackground(Bool)](./qccompositionpickerview/setdrawsbackground%28_%29.md)
  Sets whether the composition picker view draws its background.
- [func drawsBackground() -> Bool](./qccompositionpickerview/drawsbackground%28%29.md)
  Returns whether the composition picker view draws its background.
### Setting Composition Input Parameters
- [func setDefaultValue(Any!, forInputKey: String!)](./qccompositionpickerview/setdefaultvalue%28_,forinputkey%29.md)
  Sets the default value to use for a composition input parameter.
- [func resetDefaultInputValues()](./qccompositionpickerview/resetdefaultinputvalues%28%29.md)
  Clears all previously set default values for composition input parameters.
### Managing Animation
- [func startAnimation(Any!)](./qccompositionpickerview/startanimation%28_%29.md)
  Starts animating the composition in the composition picker view.
- [func stopAnimation(Any!)](./qccompositionpickerview/stopanimation%28_%29.md)
  Stops animating the composition that is currently animating in the composition picker view.
- [func isAnimating() -> Bool](./qccompositionpickerview/isanimating%28%29.md)
  Returns whether or not the composition picker view is currently animating its composition.
- [func setMaxAnimationFrameRate(Float)](./qccompositionpickerview/setmaxanimationframerate%28_%29.md)
  Sets the maximum frame rate for animating compositions.
- [func maxAnimationFrameRate() -> Float](./qccompositionpickerview/maxanimationframerate%28%29.md)
  Retrieves the maximum frame rate for animating compositions.
### Controlling Display of Composition Names
- [func setShowsCompositionNames(Bool)](./qccompositionpickerview/setshowscompositionnames%28_%29.md)
  Enables  the display of composition names in the composition picker view.
- [func showsCompositionNames() -> Bool](./qccompositionpickerview/showscompositionnames%28%29.md)
  Retrieves whether composition names can be shown in the composition picker view.
### Setting and Retrieving the View Delegate
- [func setDelegate(Any!)](./qccompositionpickerview/setdelegate%28_%29.md)
  Sets the composition picker view delegate.
- [func delegate() -> Any!](./qccompositionpickerview/delegate%28%29.md)
  Retrieves the composition picker view delegate.
### Managing the Composition Picker View
- [func setCompositionsFromRepositoryWithProtocol(String!, andAttributes: [AnyHashable : Any]!)](./qccompositionpickerview/setcompositionsfromrepositorywithprotocol%28_,andattributes%29.md)
  Sets the  compositions in the composition picker view  to those that match the specified criteria.
- [func compositions() -> [Any]!](./qccompositionpickerview/compositions%28%29.md)
  Returns the list of compositions that are currently in the composition picker view.
- [func setAllowsEmptySelection(Bool)](./qccompositionpickerview/setallowsemptyselection%28_%29.md)
  Sets whether to allow an empty selection in the composition picker view.
- [func allowsEmptySelection() -> Bool](./qccompositionpickerview/allowsemptyselection%28%29.md)
  Retrieves the empty-selection state of the composition picker view.
- [func setCompositionAspectRatio(NSSize)](./qccompositionpickerview/setcompositionaspectratio%28_%29.md)
  Sets  the aspect ratio used to display compositions in the composition picker view.
- [func compositionAspectRatio() -> NSSize](./qccompositionpickerview/compositionaspectratio%28%29.md)
  Retrieves the aspect ratio used to display compositions in the composition picker  view.
- [func setSelectedComposition(QCComposition!)](./qccompositionpickerview/setselectedcomposition%28_%29.md)
  Sets a composition as selected in the composition picker view.
- [func selectedComposition() -> QCComposition!](./qccompositionpickerview/selectedcomposition%28%29.md)
  Returns the composition that is currently selected in the composition picker view.
### Working with Columns and Rows
- [func setNumberOfColumns(Int)](./qccompositionpickerview/setnumberofcolumns%28_%29.md)
  Sets the number of columns in the composition picker view.
- [func numberOfColumns() -> Int](./qccompositionpickerview/numberofcolumns%28%29.md)
  Retrieves the number of columns in the composition picker view.
- [func setNumberOfRows(Int)](./qccompositionpickerview/setnumberofrows%28_%29.md)
  Sets the number of rows in the composition picker view.
- [func numberOfRows() -> Int](./qccompositionpickerview/numberofrows%28%29.md)
  Retrieves the number of rows in the composition picker view.
### Notifications
- [QCCompositionPickerViewDidSelectCompositionNotification](./qccompositionpickerviewdidselectcompositionnotification.md)
  Posted when the user selects a composition in the picker view.

## Relationships

### Inherits From
- [NSView](../AppKit/nsview.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Classes
- [class QCComposition](./qccomposition.md)
  The `QCComposition` class represents a Quartz Composer composition that either:
- [class QCCompositionLayer](./qccompositionlayer.md)
  A layer that loads, plays, and controls Quartz Composer compositions in a Core Animation layer hierarchy.
- [class QCCompositionParameterView](./qccompositionparameterview.md)
  A class that allows users to edit the input parameters of a composition in real time. The composition can be rendering in any of the following objects: [`QCRenderer`](./qcrenderer.md), [`QCView`](./qcview.md), or [`QCCompositionLayer`](./qccompositionlayer.md).
- [class QCCompositionPickerPanel](./qccompositionpickerpanel.md)
  The `QCCompositionPickerPanel` class represents a utility window that allows users to browse compositions that are in the Quartz Composer composition repository and, if supported, preview the composition. The `QCCompositionPickerPanel` class cannot be subclassed.
- [class QCCompositionRepository](./qccompositionrepository.md)
  The `QCCompositionRepository` class represents a system-wide centralized repository of built-in and installed Quartz Composer compositions (`/Library/Compositions` and `~/Library/Compositions`). The `QCCompositionRepository` class cannot be subclassed.
- [class QCPatchController](./qcpatchcontroller.md)
- [class QCPlugIn](./qcplugin.md)
  A base class to subclass for writing custom patches.
- [class QCPlugInViewController](./qcpluginviewcontroller.md)
  The `QCPlugInViewController` class communicates (through Cocoa bindings) between a custom patch and the view used for the internal settings of the custom patch. Only custom patches that use internal settings exposed to the user need to use the `QCPlugInViewController` class.
- [class QCRenderer](./qcrenderer.md)
  A base class for low-level rendering.
- [class QCView](./qcview.md)
  The `QCView` class is a custom `NSView` class that loads, plays, and controls Quartz Composer compositions. It is an autonomous view that is driven by an internal timer running on the main thread.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionpickerview)*