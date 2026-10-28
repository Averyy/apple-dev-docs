# QCCompositionRepository

**Framework**: Quartz  
**Kind**: class  
**Role**: Class

The `QCCompositionRepository` class represents a system-wide centralized repository of built-in and installed Quartz Composer compositions (`/Library/Compositions` and `~/Library/Compositions`). The `QCCompositionRepository` class cannot be subclassed.

**Availability**:
- macOS 10.4+ - Deprecated in 10.15

> **Deprecated**: QuartzComposer API deprecated. (Define QC_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
class QCCompositionRepository
```

```objc
@interface QCCompositionRepository : NSObject
```

## Overview

Compositions in the repository are represented by the [`QCComposition`](./qccomposition.md) class. You can use the methods of the `QCCompositionRepository` class to fetch all compositions or only those that meet specific criteria.

## Topics

### Getting the Composition Repository
- [class func shared() -> QCCompositionRepository!](./qccompositionrepository/shared%28%29.md)
  Returns the shared instance of the composition repository.
### Fetching Compositions
- [func composition(withIdentifier: String!) -> QCComposition!](./qccompositionrepository/composition%28withidentifier%29.md)
  Returns the composition that corresponds to the identifier.
- [func compositions(withProtocols: [Any]!, andAttributes: [AnyHashable : Any]!) -> [Any]!](./qccompositionrepository/compositions%28withprotocols,andattributes%29.md)
  Returns an array of compositions that match a set of criteria.
- [func allCompositions() -> [Any]!](./qccompositionrepository/allcompositions%28%29.md)
  Returns an array that contains all compositions currently in the composition repository.
### Notifications
- [QCCompositionRepositoryDidUpdateNotification](./qccompositionrepositorydidupdatenotification.md)
  Posted whenever the list of compositions in the composition repository is updated.
### Instance Variables
- [cq](./qccompositionrepository/cq.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

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
- [class QCCompositionPickerView](./qccompositionpickerview.md)
  The `QCCompositionPickerView` class allows users to browse compositions that are in the Quartz Composer composition repository, and to preview them. You can set the default input parameters for a composition preview  by using the method setDefaultValue:forInputKey:.
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartz/qccompositionrepository)*