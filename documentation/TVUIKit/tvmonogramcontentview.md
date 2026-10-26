# TVMonogramContentView

**Framework**: TVUIKit  
**Kind**: class  
**Role**: Class

A view that contains a circular image of a person or the person’s initials.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
class TVMonogramContentView
```

```objc
@interface TVMonogramContentView : UIView
```

#### Overview

The system provides a generic placeholder image if [`image`](./tvmonogramcontentconfiguration-c.class/image.md) is `nil`. If [`personNameComponents`](./tvmonogramcontentconfiguration-c.class/personnamecomponents.md) isn’t `nil`, the system creates a localized monogram image using the first initials from the name components.

![A darkened image with a highlighted box along the left side. The box contains a round image with an actor’s initials inside of it.](https://developer.apple.com/tutorials/images/com.apple.tvuikit/media-3801438@2x.png)

The following code illustrates how to update the configuration for a monogram:

```swift
override func updateConfiguration(using state: UICellConfigurationState) {
    var configuration = TVMonogramContentConfiguration().updatedConfiguration(for: state)

    configuration.image = avatarImage
    configuration.text = "Anne Johnson"
    configuration.secondaryText = "Actor"
    configuration.personNameComponents = nameComponents

    self.contentConfiguration = configuration
}
```

## Topics

### Creating a Monogram Content View
- [convenience init(configuration: TVMonogramContentConfiguration)](./tvmonogramcontentview/init%28configuration%29.md)
  Creates a monogram content view with the configuration you specify.
- [struct TVMonogramContentConfiguration](./tvmonogramcontentconfiguration-swift.struct.md)
  A content configuration for a monogram view.
- [- initWithConfiguration:](./tvmonogramcontentview/initwithconfiguration_.md)
  Creates a monogram content view with the configuration you specify.
- [TVMonogramContentConfiguration](./tvmonogramcontentconfiguration-c.class.md)
  A content configuration for a monogram view.
### Managing the Content Layout
- [var focusedFrameGuide: UILayoutGuide](./tvmonogramcontentview/focusedframeguide.md)
  A guide for positioning other elements with the content view image’s focused frame.
### Managing the Content Configuration
- [configuration](./tvmonogramcontentview/configuration.md)
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
- [class TVMediaItemContentView](./tvmediaitemcontentview.md)
  A view that represents media content, such as movies and TV shows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentview)*