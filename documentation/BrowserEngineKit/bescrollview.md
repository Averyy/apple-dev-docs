# BEScrollView

**Framework**: BrowserEngineKit  
**Kind**: class

A scroll view that works with its delegate to handle nesting, and customize scroll interactions.

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

#### Overview

Use `BEScrollView` instead of [`UIScrollView`](https://developer.apple.com/documentation/UIKit/UIScrollView) in situations where you need to:

- Handle scroll updates programmatically, potentially overriding the default scroll view behavior.
- Have scroll views that are siblings in the view hierarchy but nested in the browser Document Object Model (DOM).

If either of these is true, replace your use of `UIScrollView` with `BEScrollView` and set the scroll view’s [`delegate`](bescrollview/delegate.md) to an object that implements the [`BEScrollViewDelegate`](bescrollviewdelegate.md) methods.

## Topics

### Responding to scroll updates
- [var delegate: (any BEScrollViewDelegate)?](bescrollview/delegate.md)
  The delegate of the scroll view.

## Relationships

### Inherits From
- [UIScrollView](../UIKit/UIScrollView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UIFocusItemScrollableContainer](../UIKit/UIFocusItemScrollableContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class BEScrollViewScrollUpdate](bescrollviewscrollupdate.md)
  An object that represents a change in a scroll view’s scroll state.
- [protocol BEScrollViewDelegate](bescrollviewdelegate.md)
  The protocol that browser scroll view delegates conform to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollview)*