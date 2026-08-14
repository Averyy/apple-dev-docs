# MarkupEditViewController

**Framework**: PaperKit  
**Kind**: class

A view controller that manages the interface for inserting content into a canvas.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency class MarkupEditViewController
```

## Mentions

- [Integrating PaperKit into your app](getting-started-with-paperkit.md)

#### Overview

Use `MarkupToolbarViewController` for macOS.

## Topics

### Creating a view controller
- [init(supportedFeatureSet: FeatureSet, additionalActions: [UIMenuElement])](markupeditviewcontroller/init(supportedfeatureset:additionalactions:).md)
  Creates a markup edit view controller.
### Configuring the view controller
- [let supportedFeatureSet: FeatureSet](markupeditviewcontroller/supportedfeatureset.md)
  The supported features of this edit UI.
- [var delegate: (any MarkupEditViewController.Delegate)?](markupeditviewcontroller/delegate-swift.property.md)
  The delegate for responding to user actions.
### Responding to changes
- [MarkupEditViewController.Delegate](markupeditviewcontroller/delegate-swift.protocol.md)
### Managing view lifecycle
- [func viewDidLoad()](markupeditviewcontroller/viewdidload.md)

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
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
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

- [class PaperMarkupViewController](papermarkupviewcontroller.md)
  A view controller for interactively creating and showing markup.
- [class MarkupToolbarViewController](markuptoolbarviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupeditviewcontroller)*