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
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [var contentSelectionViewController: AVContentSelectionViewController?](avmultiviewmanager/contentselectionviewcontroller.md)
  A view controller that presents a user interface to select additional video content to display.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontentselectionviewcontroller)*