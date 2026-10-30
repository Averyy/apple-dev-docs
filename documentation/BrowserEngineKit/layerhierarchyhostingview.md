# LayerHierarchyHostingView

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

A view that hosts a layer hierarchy you manage in another process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
class LayerHierarchyHostingView
```

```objc
@interface BELayerHierarchyHostingView : UIView
```

## Mentions

- [Hosting browser view layers in the rendering extension](./hosting-browser-view-layers-in-the-rendering-extension.md)
- [Propagating view visibility information to extension processes](./propagating-view-visibility-information-to-browser-extensions.md)

## Overview

To connect a view hierarchy in another process, create an instance of this class and set its [`handle`](./layerhierarchyhostingview/handle.md) to a [`LayerHierarchyHandle`](./layerhierarchyhandle.md) from the other process.

> ❗ **Important**: If you invalidate the associated layer hierarchy, stop displaying the view.

## Topics

### Identifying remote layer hierarchy
- [var handle: LayerHierarchyHandle?](./layerhierarchyhostingview/handle.md)
  A reference to a layer hierarchy in another process.

## Relationships

### Inherits From
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Layer hosting
- [Hosting browser view layers in the rendering extension](./hosting-browser-view-layers-in-the-rendering-extension.md)
  Coordinate view-hierarchy and layer-hierarchy changes between processes.
- [class LayerHierarchy](./layerhierarchy.md)
  An object that holds a reference to layers rendered in another process’s view.
- [class LayerHierarchyHostingTransactionCoordinator](./layerhierarchyhostingtransactioncoordinator.md)
  A class that synchronizes updates to views and layers in different processes.
- [class LayerHierarchyHandle](./layerhierarchyhandle.md)
  A reference to a layer hierarchy that your app shares between processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingview)*