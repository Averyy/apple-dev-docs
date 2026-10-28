# AMWorkflowView

**Framework**: Automator  
**Kind**: class  
**Role**: Class

An object that lets you view and edit Automator workflows in your app.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
class AMWorkflowView
```

```objc
@interface AMWorkflowView : NSView
```

## Overview

A workflow view displays an instance of [`AMWorkflow`](./amworkflow.md).

You can use Interface Builder to add an instance of [`AMWorkflowView`](./amworkflowview.md) to a window in your app. You can then add an [`AMWorkflowView`](./amworkflowview.md) object to the nib window and use the controller’s [`workflowView`](./amworkflowcontroller/workflowview-swift.property.md) outlet to connect it to the workflow view. The controller object also has [`run(_:)`](./amworkflowcontroller/run%28_%29.md) and [`stop(_:)`](./amworkflowcontroller/stop%28_%29.md) actions that can be connected to buttons or other user interface elements.

## Topics

### Configuring the Workflow View
- [var isEditable: Bool](./amworkflowview/iseditable.md)
  A Boolean value that indicates whether the workflow view is editable.
- [var workflowController: AMWorkflowController?](./amworkflowview/workflowcontroller.md)
  The view’s workflow controller.

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

## See Also

### Workflows
- [class AMWorkflow](./amworkflow.md)
  An object that lets you use an Automator workflow in your app.
- [class AMWorkflowController](./amworkflowcontroller.md)
  An object that lets you manage an Automator workflow in your app.
- [class AMWorkspace](./amworkspace.md)
  A workspace for running an Automator workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowview)*