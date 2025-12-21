# MarkupEditViewController

**Framework**: PaperKit  
**Kind**: class

A view controller that manages the interface for inserting content into a canvas.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency class MarkupEditViewController
```

## Topics

### Protocols
- [MarkupEditViewController.Delegate](markupeditviewcontroller/delegate-swift.protocol.md)
### Initializers
- [init(supportedFeatureSet: FeatureSet, additionalActions: [UIMenuElement])](markupeditviewcontroller/init(supportedfeatureset:additionalactions:).md)
  Creates a markup edit view controller.
### Instance Properties
- [var delegate: (any MarkupEditViewController.Delegate)?](markupeditviewcontroller/delegate-swift.property.md)
  The delegate for responding to user actions.
- [let supportedFeatureSet: FeatureSet](markupeditviewcontroller/supportedfeatureset.md)
  The supported features of this edit UI.
### Instance Methods
- [func viewDidLoad()](markupeditviewcontroller/viewdidload.md)

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
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
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

- [class PaperMarkupViewController](papermarkupviewcontroller.md)
  A view controller for interactively creating, and showing markup.
- [class MarkupToolbarViewController](markuptoolbarviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupeditviewcontroller)*