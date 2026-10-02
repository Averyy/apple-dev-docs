# BEScrollView

**Framework**: BrowserEngineKit  
**Kind**: class

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

#### Overview

Use `BEScrollView` instead of [`UIScrollView`](https://developer.apple.com/documentation/uikit/uiscrollview) if you need to:

- Handle scroll updates programmatically
- Override default scroll view behavior
- Support scroll views that are siblings in the view hierarchy, but nested in the browser Document Object Model (DOM)

In any of these scenarios, set the scroll view’s [`delegate`](bescrollview/delegate.md) to an object that implements [`BEScrollViewDelegate`](bescrollviewdelegate.md).

## Topics

### Responding to scroll updates
- [var delegate: (any BEScrollViewDelegate)?](bescrollview/delegate.md)
  A delegate that responds to the scroll view’s scroll updates.

## Relationships

### Inherits From
- [UIScrollView](../uikit/uiscrollview.md)
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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UIFocusItemScrollableContainer](../uikit/uifocusitemscrollablecontainer.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class BEScrollViewScrollUpdate](bescrollviewscrollupdate.md)
  An object that describes a change in a scroll view’s scroll state.
- [protocol BEScrollViewDelegate](bescrollviewdelegate.md)
  A protocol for scroll view delegates to handle scroll updates and DOM nesting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bescrollview)*