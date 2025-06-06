# UIPreviewInteraction

**Framework**: Uikit  
**Kind**: class

A class that registers a view to provide a custom user experience in response to 3D Touch interactions.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UIPreviewInteraction
```

#### Overview

A 3D Touch interaction results in a  that comprises two phases, the first also called , followed by . The interaction progresses through these phases as a person applies more force with a touch. The following image shows the relationship between the force of a person’s touch and the phases of the preview interaction.

![An illustration showing the preview interaction as it progresses through the preview phase and into the commit phases in response to increasing touch force.](https://docs-assets.developer.apple.com/published/be9bfae0ee50a5a22bc56521a0d7dea9/media-2793214%402x.png)

When using view controller previewing,  represents the preview phase, and  the commit phase.

> **Note**:  If you want to provide the system default view controller previewing behavior ( and ), use the [`registerForPreviewing(with:sourceView:)`](uiviewcontroller/registerforpreviewing(with:sourceview:).md) and [`unregisterForPreviewing(withContext:)`](uiviewcontroller/unregisterforpreviewing(withcontext:).md) methods on [`UIViewController`](uiviewcontroller.md) instead of [`UIPreviewInteraction`](uipreviewinteraction.md). See `Working With 3D Touch Previews and Preview Quick Actions` for further details.

A preview interaction is responsible for managing 3D Touch interactions for a specified view. It uses a delegate object to communicate the progress and status of the interaction to your code.

To use a preview interaction in your app:

1. Create a [`UIPreviewInteraction`](uipreviewinteraction.md) object, passing the view into the default initializer.
2. Create a delegate object that conforms to the [`UIPreviewInteractionDelegate`](uipreviewinteractiondelegate.md) protocol, and implement the appropriate methods.
3. Assign the delegate object to the [`delegate`](uipreviewinteraction/delegate.md) property on the preview interaction object.

For more information about the state transitions through which a preview interaction progresses, see [`UIPreviewInteractionDelegate`](uipreviewinteractiondelegate.md).

## Topics

### Creating a preview interaction
- [init(view: UIView)](uipreviewinteraction/init(view:).md)
  Returns a newly initialized preview interaction for the specified view.
### Preparing preview interactions
- [var delegate: (any UIPreviewInteractionDelegate)?](uipreviewinteraction/delegate.md)
  An object that acts as the delegate of the preview interaction.
- [protocol UIPreviewInteractionDelegate](uipreviewinteractiondelegate.md)
  A set of methods for communicating the progress of a preview interaction.
### Handling preview interactions
- [var view: UIView?](uipreviewinteraction/view.md)
  The view from which the preview interaction receives touch events.
- [func cancel()](uipreviewinteraction/cancel.md)
  Cancels the current preview interaction.
- [func location(in: (any UICoordinateSpace)?) -> CGPoint](uipreviewinteraction/location(in:).md)
  Returns the location of the touch that started the interaction.

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
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol UIPreviewInteractionDelegate](uipreviewinteractiondelegate.md)
  A set of methods for communicating the progress of a preview interaction.
- [protocol UIPreviewActionItem](uipreviewactionitem.md)
  A set of methods that defines the styles you can apply to peek quick actions and peek quick action groups, and defines a read-only accessor for the user-visible title of a peek quick action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UIKit/uipreviewinteraction)*