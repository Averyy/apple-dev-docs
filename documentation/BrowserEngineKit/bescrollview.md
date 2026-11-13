# BEScrollView

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

A scroll view that works with its delegate to handle nesting and customize scroll interactions.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- tvOS 17.4+
- visionOS 1.1+

## Declaration

```swift
@MainActor
class BEScrollView
```

```objc
@interface BEScrollView : UIScrollView
```

## Overview

Use `BEScrollView` instead of [`UIScrollView`](../UIKit/uiscrollview.md) if you need to:

- Handle scroll updates programmatically
- Override default scroll view behavior
- Support scroll views that are siblings in the view hierarchy, but nested in the browser Document Object Model (DOM)

In any of these scenarios, set the scroll view’s [`delegate`](./bescrollview/delegate.md) to an object that implements [`BEScrollViewDelegate`](./bescrollviewdelegate.md).

## Topics

### Responding to scroll updates
- [var delegate: (any BEScrollViewDelegate)?](./bescrollview/delegate.md)
  A delegate that responds to the scroll view’s scroll updates.

## Relationships

### Inherits From
- [UIScrollView](../UIKit/uiscrollview.md)
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
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UIFocusItemScrollableContainer](../UIKit/uifocusitemscrollablecontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Scroll view interaction
- [class BEScrollViewScrollUpdate](./bescrollviewscrollupdate.md)
  An object that describes a change in a scroll view’s scroll state.
- [protocol BEScrollViewDelegate](./bescrollviewdelegate.md)
  A protocol for scroll view delegates to handle scroll updates and DOM nesting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollview)*