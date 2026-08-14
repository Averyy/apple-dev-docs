# AMWorkflowView

**Framework**: Automator  
**Kind**: class

An object that lets you view and edit Automator workflows in your app.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
class AMWorkflowView
```

#### Overview

A workflow view displays an instance of [`AMWorkflow`](amworkflow.md).

You can use Interface Builder to add an instance of [`AMWorkflowView`](amworkflowview.md) to a window in your app. You can then add an [`AMWorkflowView`](amworkflowview.md) object to the nib window and use the controller’s [`workflowView`](amworkflowcontroller/workflowview-swift.property.md) outlet to connect it to the workflow view. The controller object also has [`run(_:)`](amworkflowcontroller/run(_:).md) and [`stop(_:)`](amworkflowcontroller/stop(_:).md) actions that can be connected to buttons or other user interface elements.

## Topics

### Configuring the Workflow View
- [var isEditable: Bool](amworkflowview/iseditable.md)
  A Boolean value that indicates whether the workflow view is editable.
- [var workflowController: AMWorkflowController?](amworkflowview/workflowcontroller.md)
  The view’s workflow controller.

## Relationships

### Inherits From
- [NSView](../appkit/nsview.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)

## See Also

- [class AMWorkflow](amworkflow.md)
  An object that lets you use an Automator workflow in your app.
- [class AMWorkflowController](amworkflowcontroller.md)
  An object that lets you manage an Automator workflow in your app.
- [class AMWorkspace](amworkspace.md)
  A workspace for running an Automator workflow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amworkflowview)*