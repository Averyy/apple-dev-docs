# TVMonogramContentView

**Framework**: TVUIKit  
**Kind**: class

A view that contains a circular image of a person or the person’s initials.

**Availability**:
- tvOS 15.0+

## Declaration

```swift
@MainActor
class TVMonogramContentView
```

#### Overview

The system provides a generic placeholder image if [`image`](tvmonogramcontentconfiguration-c.class/image.md) is `nil`. If [`personNameComponents`](tvmonogramcontentconfiguration-c.class/personnamecomponents.md) isn’t `nil`, the system creates a localized monogram image using the first initials from the name components.

![A darkened image with a highlighted box along the left side. The box contains a round image with an actor’s initials inside of it.](https://docs-assets.developer.apple.com/published/64d07085129af0f3a469bc3bfb9d2ae7/media-3801438%402x.png)

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
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentView](../UIKit/UIContentView-5fh3z.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class TVMediaItemContentView](tvmediaitemcontentview.md)
  A view that represents media content, such as movies and TV shows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmonogramcontentview)*