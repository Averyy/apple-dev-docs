# TVMediaItemContentView

**Framework**: TVUIKit  
**Kind**: class

A view that represents media content, such as movies and TV shows.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
class TVMediaItemContentView
```

#### Overview

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
- [convenience init(configuration: TVMediaItemContentConfiguration)](tvmediaitemcontentview/init(configuration:).md)
  Creates a media item content view with the configuration you specify.
- [struct TVMediaItemContentConfiguration](tvmediaitemcontentconfiguration-swift.struct.md)
  A content configuration for a media item view.
### Managing the Content Layout
- [var focusedFrameGuide: UILayoutGuide](tvmediaitemcontentview/focusedframeguide.md)
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

- [class TVMonogramContentView](tvmonogramcontentview.md)
  A view that contains a circular image of a person or the person’s initials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmediaitemcontentview)*