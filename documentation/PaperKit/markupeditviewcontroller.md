# MarkupEditViewController

**Framework**: PaperKit  
**Kind**: class  
**Role**: Class

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

- [Integrating PaperKit into your app](./getting-started-with-paperkit.md)

## Overview

Use `MarkupToolbarViewController` for macOS.

## Topics

### Creating a view controller
- [init(supportedFeatureSet: FeatureSet, additionalActions: [UIMenuElement])](./markupeditviewcontroller/init%28supportedfeatureset,additionalactions%29.md)
  Creates a markup edit view controller.
### Configuring the view controller
- [let supportedFeatureSet: FeatureSet](./markupeditviewcontroller/supportedfeatureset.md)
  The supported features of this edit UI.
- [var delegate: (any MarkupEditViewController.Delegate)?](./markupeditviewcontroller/delegate-swift.property.md)
  The delegate for responding to user actions.
### Responding to changes
- [MarkupEditViewController.Delegate](./markupeditviewcontroller/delegate-swift.protocol.md)
### Managing view lifecycle
- [func viewDidLoad()](./markupeditviewcontroller/viewdidload%28%29.md)

## Relationships

### Inherits From
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### View controllers
- [class PaperMarkupViewController](./papermarkupviewcontroller.md)
  A view controller for interactively creating and showing markup.
- [class MarkupToolbarViewController](./markuptoolbarviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupeditviewcontroller)*