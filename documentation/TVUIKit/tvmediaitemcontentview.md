# TVMediaItemContentView

**Framework**: TVUIKit  
**Kind**: class  
**Role**: Class

A view that represents media content, such as movies and TV shows.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
class TVMediaItemContentView
```

```objc
@interface TVMediaItemContentView : UIView
```

## Overview

The following code illustrates how to update the configuration for a wide media item:

```swift
override func updateConfiguration(using state: UICellConfigurationState) {
    var configuration = TVMediaItemContentConfiguration.wideCell().updatedConfiguration(for: state)

    configuration.image = coverArtImage
    configuration.text = // The title of the media content.
    configuration.secondaryText = "S1, E1"
    configuration.playbackProgress = 0.4
    configuration.badgeText = "Live"
    configuration.badgeProperties = TVMediaItemContentConfiguration.BadgeProperties.liveContent()

    self.contentConfiguration = configuration
}
```

## Topics

### Creating a Media Item Content View
- [convenience init(configuration: TVMediaItemContentConfiguration)](./tvmediaitemcontentview/init%28configuration%29.md)
  Creates a media item content view with the configuration you specify.
- [struct TVMediaItemContentConfiguration](./tvmediaitemcontentconfiguration-swift.struct.md)
  A content configuration for a media item view.
- [- initWithConfiguration:](./tvmediaitemcontentview/initwithconfiguration_.md)
  Creates a media item content view with the configuration you specify.
- [TVMediaItemContentConfiguration](./tvmediaitemcontentconfiguration-c.class.md)
  A content configuration for a media item view.
### Managing the Content Layout
- [var focusedFrameGuide: UILayoutGuide](./tvmediaitemcontentview/focusedframeguide.md)
  A guide for positioning other elements with the content view image’s focused frame.
### Managing the Content Configuration
- [configuration](./tvmediaitemcontentview/configuration.md)
  The current configuration of the view.

## Relationships

### Inherits From
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentView](../UIKit/uicontentview-5fh3z.md)
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
- [UIContentView](../UIKit/uicontentview-3zu2k.md)

## See Also

### Content views
- [class TVMonogramContentView](./tvmonogramcontentview.md)
  A view that contains a circular image of a person or the person’s initials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmediaitemcontentview)*