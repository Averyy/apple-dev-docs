# UIBackgroundExtensionView

**Framework**: UIKit  
**Kind**: class

A view that extends content to fill its own bounds.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
class UIBackgroundExtensionView
```

#### Overview

A background extension view can be laid out to extend outside the safe area, such as under a sidebar or an inspector. By default, the view lays out its content to stay within the safe area, and uses modifications of the content along the edges to fill the container view.

## Topics

### Instance Properties
- [var automaticallyPlacesContentView: Bool](uibackgroundextensionview/automaticallyplacescontentview.md)
  Controls the automatic safe area placement of the `contentView` within the container.
- [var contentView: UIView?](uibackgroundextensionview/contentview.md)
  The content view to extend to fill the `UIBackgroundExtensionView`.

## Relationships

### Inherits From
- [UIView](uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](uiactivityitemsconfigurationproviding.md)
- [UIAppearance](uiappearance.md)
- [UIAppearanceContainer](uiappearancecontainer.md)
- [UICoordinateSpace](uicoordinatespace.md)
- [UIDynamicItem](uidynamicitem.md)
- [UIFocusEnvironment](uifocusenvironment.md)
- [UIFocusItem](uifocusitem.md)
- [UIFocusItemContainer](uifocusitemcontainer.md)
- [UILargeContentViewerItem](uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](uiresponderstandardeditactions.md)
- [UITraitChangeObservable](uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](uitraitenvironment.md)
- [UIUserActivityRestoring](uiuseractivityrestoring.md)

## See Also

- [class UIScrollEdgeElementContainerInteraction](uiscrolledgeelementcontainerinteraction.md)
  Add this interaction to a container view of views that overlay the edge of a scroll view. Any descendants of this view that should affect the shape of the edge effect, such as labels, images, glass views, and controls, will automatically do so.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibackgroundextensionview)*