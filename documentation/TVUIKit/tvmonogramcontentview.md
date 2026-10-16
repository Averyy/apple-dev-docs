# TVMonogramContentView

**Framework**: TVUIKit  
**Kind**: class

A view that contains a circular image of a person or the person’s initials.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
class TVMonogramContentView
```

#### Overview

The system provides a generic placeholder image if [`image`](tvmonogramcontentconfiguration-c.class/image.md) is `nil`. If [`personNameComponents`](tvmonogramcontentconfiguration-c.class/personnamecomponents.md) isn’t `nil`, the system creates a localized monogram image using the first initials from the name components.

![A darkened image with a highlighted box along the left side. The box contains a round image with an actor’s initials inside of it.](/images/com.apple.tvuikit/media-3801438@2x.png)

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
- [convenience init(configuration: TVMonogramContentConfiguration)](tvmonogramcontentview/init(configuration:).md)
  Creates a monogram content view with the configuration you specify.
- [struct TVMonogramContentConfiguration](tvmonogramcontentconfiguration-swift.struct.md)
  A content configuration for a monogram view.
### Managing the Content Layout
- [var focusedFrameGuide: UILayoutGuide](tvmonogramcontentview/focusedframeguide.md)
  A guide for positioning other elements with the content view image’s focused frame.

## Relationships

### Inherits From
- [UIView](../uikit/uiview.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentView](../uikit/uicontentview-5fh3z.md)
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

- [class TVMediaItemContentView](tvmediaitemcontentview.md)
  A view that represents media content, such as movies and TV shows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentview)*