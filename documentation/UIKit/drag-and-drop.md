# Drag and drop

**Framework**: Uikit

Bring drag and drop to your app by using interaction APIs with your views.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

#### Overview

With drag and drop in iOS, users can drag items from one onscreen location to another using continuous gestures. A drag-and-drop activity can take place in a single app, or it can start in one app and end in another.

![Dragging multiple pictures from an app into Mail](https://docs-assets.developer.apple.com/published/7bae4e3a10591fbf6cfae19ea45fd25b/media-2910342%402x.png)

> **Note**:  Prior to iOS 15, drag-and-drop activities on iPhone can take place in a single app but not between two apps.

The app from which an item is dragged is the . The app on which an item is dropped is the . For drag and drop in a single app, that app plays both roles simultaneously. The complete user action from start to finish — using system-mediated gestures — is a . A , by contrast, is an object that’s managed by the system and that manages the items the user is dragging.

When dragging is in progress, the source and destination apps continue to run normally and support user interaction. A user can invoke the Dock, return to the Home screen, open a second app in Split View, and even start another drag activity.

Unlike in macOS, iOS drag and drop supports multiple simultaneous drag activities—as many as the user’s fingers can handle. You can design your app so that the user can sequentially add drag items to an in-progress drag session, and a destination app can accept multiple, simultaneous drops.

Text views and text fields automatically support drag and drop. Collection views and table views offer dedicated, view-specific methods and properties, and text views offer APIs for customizing the views’ drag-and-drop behavior. You can configure any custom view to support drag and drop, as well.

> **Note**:  The system handles all security aspects of inter-app drag and drop in iOS. You don’t need to perform additional configuration like setting special entitlements or `Info.plist` keys.

## Topics

### Essentials
- [Understanding a drag item as a promise](understanding-a-drag-item-as-a-promise.md)
  Use drag items to convey data representation promises between a source app and a destination app.
- [Making a view into a drag source](making-a-view-into-a-drag-source.md)
  Adopt drag interaction APIs to provide items for dragging.
- [Making a view into a drop destination](making-a-view-into-a-drop-destination.md)
  Adopt drop interaction APIs to selectively consume dragged content.
- [Adopting drag and drop in a custom view](adopting-drag-and-drop-in-a-custom-view.md)
  Demonstrates how to enable drag and drop for a `UIImageView` instance.
- [Adopting drag and drop in a table view](adopting-drag-and-drop-in-a-table-view.md)
  Demonstrates how to enable and implement drag and drop for a table view.
### Drag and drop interactions
- [protocol UIDragInteractionDelegate](uidraginteractiondelegate.md)
  The interface for configuring and controlling a drag interaction.
- [protocol UIDropInteractionDelegate](uidropinteractiondelegate.md)
  The interface for configuring and controlling a drop interaction.
- [class UIDragInteraction](uidraginteraction.md)
  An interaction to enable dragging of items from a view, employing a delegate to provide drag items and to respond to calls from the drag session.
- [class UIDropInteraction](uidropinteraction.md)
  An interaction to enable dropping of items onto a view, employing a delegate to instantiate objects and respond to calls from the drop session.
### Spring-loaded interactions
- [protocol UISpringLoadedInteractionBehavior](uispringloadedinteractionbehavior.md)
  The interface for specifying the behavior of a spring-loaded interaction.
- [protocol UISpringLoadedInteractionSupporting](uispringloadedinteractionsupporting.md)
  The interface that determines if an object supports a spring-loaded interaction for drag and drop activities.
- [class UISpringLoadedInteraction](uispringloadedinteraction.md)
  An interaction object for configuring and controlling spring-loaded, user-driven navigation during a drag activity.
- [protocol UISpringLoadedInteractionContext](uispringloadedinteractioncontext.md)
  The interface an object implements to provide information about a spring-loaded interaction.
- [protocol UISpringLoadedInteractionEffect](uispringloadedinteractioneffect.md)
  The interface for providing visual styling to a spring-loaded interaction based on the interaction state.
### Drag sources
- [class UIDragItem](uidragitem.md)
  A representation of an underlying data item as a person drags it from one location to another.
- [protocol UIDragDropSession](uidragdropsession.md)
  The common interface for querying the state of both drag sessions and drop sessions.
- [protocol UIDragSession](uidragsession.md)
  The interface for configuring a drag session.
- [protocol UIDragAnimating](uidraganimating.md)
  The interface for providing custom animation alongside the system’s lift, drop, and cancellation animations.
### Drop destinations
- [protocol UIDropSession](uidropsession.md)
  The interface for querying a drop session about its state and associated drag items.
- [class UIDropProposal](uidropproposal.md)
  A configuration for the behavior of a drop interaction, required if a view accepts drop activities.
- [enum UIDropOperation](uidropoperation.md)
  Operation types that determine how a drag and drop activity resolves when the user drops a drag item.
- [enum UIDropSessionProgressIndicatorStyle](uidropsessionprogressindicatorstyle.md)
  The drop-progress indicator styles for the drop session, used while data is moving from the source to the destination.
### Item providers
- [Data delivery with drag and drop](data-delivery-with-drag-and-drop.md)
  Share data between iPad apps during a drag and drop operation using an item provider.
- [class NSItemProvider](../Foundation/NSItemProvider.md)
  An item provider for conveying data or a file between processes during drag-and-drop or copy-and-paste activities, or from a host app to an app extension.
- [protocol NSItemProviderReading : NSObjectProtocol](../Foundation/NSItemProviderReading.md)
  The protocol for implementing a class to allow an item provider to create an instance of the class.
- [protocol NSItemProviderWriting : NSObjectProtocol](../Foundation/NSItemProviderWriting.md)
  The protocol for implementing a class to allow an item provider to retrieve data from an instance of the class.
- [protocol UIItemProviderPresentationSizeProviding](uiitemproviderpresentationsizeproviding.md)
- [protocol UIItemProviderReadingAugmentationDesignating](uiitemproviderreadingaugmentationdesignating.md)
- [protocol UIItemProviderReadingAugmentationProviding](uiitemproviderreadingaugmentationproviding.md)
### Pasteboard support
- [class UIPasteConfiguration](uipasteconfiguration.md)
  The interface that an object implements to declare its ability to accept specific data types for pasting and for drag-and-drop activities.
- [protocol UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
  The interface that determines whether a responder object supports paste configuration.
### Custom drag item previews
- [class UIDragPreviewParameters](uidragpreviewparameters.md)
  A set of parameters for adjusting the appearance of a drag item preview or a targeted drag item preview.
- [class UIDragPreview](uidragpreview.md)
  A graphical preview for a single drag item, used by the system after a drag has started and when no related animation is running.
- [class UIDragPreviewTarget](uidragpreviewtarget.md)
  A geometric specification for the source or destination of a drag item preview, used by the system when a user drops items or cancels a drag activity.
- [class UITargetedDragPreview](uitargeteddragpreview.md)
  A drag item preview used by the system during lift, drop, or cancellation animation.

## See Also

- [Touches, presses, and gestures](touches-presses-and-gestures.md)
  Encapsulate your app’s event-handling logic in gesture recognizers so that you can reuse that code throughout your app.
- [Menus and shortcuts](menus-and-shortcuts.md)
  Simplify interactions with your app using menu systems, contextual menus, Home Screen quick actions, and keyboard shortcuts.
- [Pointer interactions](pointer-interactions.md)
  Support pointer interactions in your custom controls and views.
- [Apple Pencil interactions](apple-pencil-interactions.md)
  Handle user interactions like double tap and squeeze on Apple Pencil.
- [Focus-based navigation](focus-based-navigation.md)
  Navigate the interface of your UIKit app using a remote, game controller, or keyboard.
- [Accessibility for UIKit](accessibility-for-uikit.md)
  Make your UIKit apps accessible to everyone who uses iOS and tvOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/UIKit/drag-and-drop)*