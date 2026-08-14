# TVLockupHeaderFooterView

**Framework**: TVUIKit  
**Kind**: class

A view that contains header and footer information.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
class TVLockupHeaderFooterView
```

#### Overview

You can add header and footer views containing titles and subtitles to the lockup view. Headers and footers are always displayed when the lockup view is in focus.

## Topics

### Adding Titles
- [var titleLabel: UILabel?](tvlockupheaderfooterview/titlelabel.md)
  The title for a header or footer.
- [var subtitleLabel: UILabel?](tvlockupheaderfooterview/subtitlelabel.md)
  The subtitle for a header or footer.
### Configuring Focus Behavior
- [var showsOnlyWhenAncestorFocused: Bool](tvlockupheaderfooterview/showsonlywhenancestorfocused.md)
  A Boolean value indicating whether titles and subtitles are displayed when a lockup view isn’t in focus.

## Relationships

### Inherits From
- [UIView](../uikit/uiview.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [TVLockupViewComponent](tvlockupviewcomponent.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class TVLockupView](tvlockupview.md)
  A focusable view that presents main content, like a movie poster, and an optional header and footer.
- [protocol TVLockupViewComponent](tvlockupviewcomponent.md)
  The protocol for responding to lockup view state changes.
- [class TVCardView](tvcardview.md)
  A view that responds to focus interaction with a motion effect it applies to all of its subviews.
- [class TVPosterView](tvposterview.md)
  An optimized view for displaying an image, a header, and a footer.
- [class TVCaptionButtonView](tvcaptionbuttonview.md)
  A button-like view that responds to user interactions.
- [class TVMonogramView](tvmonogramview.md)
  A specialized lockup view that contains a circular image of a person or the person’s initials, along with a footer view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvlockupheaderfooterview)*