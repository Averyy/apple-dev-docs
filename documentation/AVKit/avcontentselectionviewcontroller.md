# AVContentSelectionViewController

**Framework**: AVKit  
**Kind**: class

A view controller for providing additional UI to the multiview experience.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
@MainActor
@objc(AVContentSelectionViewController) @preconcurrency class AVContentSelectionViewController
```

#### Overview

Subclass or use view controller containment to add additional UI elements to the multiview experience.

## Topics

### Creating a view controller.
- [init?(coder: NSCoder)](avcontentselectionviewcontroller/init(coder:).md)
  Creates a view controller with data in an unarchiver.
- [init(nibName: String?, bundle: Bundle?)](avcontentselectionviewcontroller/init(nibname:bundle:).md)
  Creates a view controller with the nib file in the specified bundle.

## Relationships

### Inherits From
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [var contentSelectionViewController: AVContentSelectionViewController?](avmultiviewmanager/contentselectionviewcontroller.md)
  A view controller that presents a user interface to select additional video content to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentselectionviewcontroller)*