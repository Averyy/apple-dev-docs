# MKOverlayView

**Framework**: MapKit  
**Kind**: class

Defines the basic behavior associated with all overlay views.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
class MKOverlayView
```

#### Overview

An overlay view provides the visual representation of an overlay object—that is, an object that conforms to the [`MKOverlay`](mkoverlay.md) protocol. This class defines the drawing infrastructure used by the map view but does not do any actual drawing. Subclasses are expected to override the [`drawMapRect:zoomScale:inContext:`](mkoverlayview/drawmaprect:zoomscale:incontext:.md) method in order to draw the contents of the overlay view.

The Map Kit framework provides several concrete instances of overlay views. Specifically, it provides overlay views for each of the concrete overlay objects. You can use one of these existing overlay views or define your own subclass if you want to draw the overlay contents differently.

In iOS 7 and later, use the [`MKOverlayRenderer`](mkoverlayrenderer.md) class to display overlays instead.

##### Subclassing Notes

You can subclass `MKOverlayView` to create overlays based on custom shapes and content. The only method subclasses are expected to override is the [`drawMapRect:zoomScale:inContext:`](mkoverlayview/drawmaprect:zoomscale:incontext:.md) method. However, if your class contains content that may not be ready for drawing right away, you should also override the [`canDrawMapRect:zoomScale:`](mkoverlayview/candrawmaprect:zoomscale:.md) method and use it to report when your class is ready and able to draw.

The implementation of your [`drawMapRect:zoomScale:inContext:`](mkoverlayview/drawmaprect:zoomscale:incontext:.md) method must be safe to run from multiple threads simultaneously. To improve performance, the map view may tile overlays that are large enough and distribute the rendering of each tile to separate threads.

## Relationships

### Inherits From
- [UIView](../UIKit/UIView.md)
### Inherited By
- [MKOverlayPathView](mkoverlaypathview.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlayview)*