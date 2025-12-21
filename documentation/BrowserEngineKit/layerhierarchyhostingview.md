# LayerHierarchyHostingView

**Framework**: BrowserEngineKit  
**Kind**: class

A view that hosts a layer hierarchy you manage in another process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
class LayerHierarchyHostingView
```

## Mentions

- [Hosting browser view layers in the rendering extension](hosting-browser-view-layers-in-the-rendering-extension.md)
- [Propagating view visibility information to extension processes](propagating-view-visibility-information-to-browser-extensions.md)

#### Overview

Set the view’s [`handle`](layerhierarchyhostingview/handle.md) to a [`LayerHierarchyHandle`](layerhierarchyhandle.md) you get from the other process. When you invalidate the associated layer hierarchy, you need to stop displaying the view.

## Topics

### Identifying remote layer hierarchy
- [var handle: LayerHierarchyHandle?](layerhierarchyhostingview/handle.md)
  A handle that refers to a layer hierarchy in another process.

## Relationships

### Inherits From
- [UIView](../UIKit/UIView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Hosting browser view layers in the rendering extension](hosting-browser-view-layers-in-the-rendering-extension.md)
  Coordinate view-hierarchy and layer-hierarchy changes between processes.
- [class LayerHierarchy](layerhierarchy.md)
  An object that holds a reference to layers rendered in another process’s view.
- [class LayerHierarchyHostingTransactionCoordinator](layerhierarchyhostingtransactioncoordinator.md)
  Synchronizes updates to views and layers in different processes.
- [class LayerHierarchyHandle](layerhierarchyhandle.md)
  A reference to a layer hierarchy that you share between processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingview)*