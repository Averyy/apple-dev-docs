# TVLockupHeaderFooterView

**Framework**: TVUIKit  
**Kind**: class  
**Role**: Class

A view that contains header and footer information.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
class TVLockupHeaderFooterView
```

```objc
@interface TVLockupHeaderFooterView : UIView
```

#### Overview

You can add header and footer views containing titles and subtitles to the lockup view. Headers and footers are always displayed when the lockup view is in focus.

## Topics

### Adding Titles
- [var titleLabel: UILabel?](./tvlockupheaderfooterview/titlelabel.md)
  The title for a header or footer.
- [var subtitleLabel: UILabel?](./tvlockupheaderfooterview/subtitlelabel.md)
  The subtitle for a header or footer.
### Configuring Focus Behavior
- [var showsOnlyWhenAncestorFocused: Bool](./tvlockupheaderfooterview/showsonlywhenancestorfocused.md)
  A Boolean value indicating whether titles and subtitles are displayed when a lockup view isn’t in focus.

## Relationships

### Inherits From
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [TVLockupViewComponent](./tvlockupviewcomponent.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Lockup views
- [class TVLockupView](./tvlockupview.md)
  A focusable view that presents main content, like a movie poster, and an optional header and footer.
- [protocol TVLockupViewComponent](./tvlockupviewcomponent.md)
  The protocol for responding to lockup view state changes.
- [class TVCardView](./tvcardview.md)
  A view that responds to focus interaction with a motion effect it applies to all of its subviews.
- [class TVPosterView](./tvposterview.md)
  An optimized view for displaying an image, a header, and a footer.
- [class TVCaptionButtonView](./tvcaptionbuttonview.md)
  A button-like view that responds to user interactions.
- [class TVMonogramView](./tvmonogramview.md)
  A specialized lockup view that contains a circular image of a person or the person’s initials, along with a footer view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvlockupheaderfooterview)*