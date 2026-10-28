# PHSharedAlbumCreationViewController

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class PHSharedAlbumCreationViewController
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@interface PHSharedAlbumCreationViewController : UIViewController
```

*macOS*

```objc
@interface PHSharedAlbumCreationViewController : NSViewController
```

## Overview

This class is used to present the shared album creation view from AppKit-based view controllers.

## Topics

### Protocols
- [PHSharedAlbumCreationViewController.Delegate](./phsharedalbumcreationviewcontroller/delegate-swift.protocol.md)
### Initializers
- [convenience init(configuration: PHSharedAlbumCreationConfiguration)](./phsharedalbumcreationviewcontroller/init%28configuration%29.md)
  Returns a view controller that allows the user to create a new shared album.
### Instance Properties
- [var creationResult: __PHSharedAlbumCreationResult?](./phsharedalbumcreationviewcontroller/creationresult.md)
  Upon successful album creation, `creationResult` will be non-nil and provide information about the just-created shared album.
- [var delegate: (any PHSharedAlbumCreationViewController.Delegate)?](./phsharedalbumcreationviewcontroller/delegate-swift.property.md)
  The delegate to respond to `PHSharedAlbumCreationViewController` events.
### Instance Methods
- [- initWithConfiguration:](./phsharedalbumcreationviewcontroller/initwithconfiguration_.md)

## Relationships

### Inherits From
- [NSViewController](../AppKit/nsviewcontroller.md)
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](../AppKit/nseditor.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumcreationviewcontroller)*