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

To connect a view hierarchy in another process, create an instance of this class and set its [`handle`](layerhierarchyhostingview/handle.md) to a [`LayerHierarchyHandle`](layerhierarchyhandle.md) from the other process.

> ❗ **Important**: If you invalidate the associated layer hierarchy, stop displaying the view.

## Topics

### Identifying remote layer hierarchy
- [var handle: LayerHierarchyHandle?](layerhierarchyhostingview/handle.md)
  A reference to a layer hierarchy in another process.

## Relationships

### Inherits From
- [UIView](../uikit/uiview.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [Hosting browser view layers in the rendering extension](hosting-browser-view-layers-in-the-rendering-extension.md)
  Coordinate view-hierarchy and layer-hierarchy changes between processes.
- [class LayerHierarchy](layerhierarchy.md)
  An object that holds a reference to layers rendered in another process’s view.
- [class LayerHierarchyHostingTransactionCoordinator](layerhierarchyhostingtransactioncoordinator.md)
  A class that synchronizes updates to views and layers in different processes.
- [class LayerHierarchyHandle](layerhierarchyhandle.md)
  A reference to a layer hierarchy that your app shares between processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/layerhierarchyhostingview)*