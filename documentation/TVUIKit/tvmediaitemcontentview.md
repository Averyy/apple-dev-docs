# TVMediaItemContentView

**Framework**: TVUIKit  
**Kind**: class

A view that represents media content, such as movies and TV shows.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
@MainActor
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
- [UIView](../UIKit/UIView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentView](../UIKit/UIContentView-5fh3z.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class TVMonogramContentView](tvmonogramcontentview.md)
  A view that contains a circular image of a person or the person’s initials.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmediaitemcontentview)*