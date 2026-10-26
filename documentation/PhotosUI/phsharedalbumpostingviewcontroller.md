# PHSharedAlbumPostingViewController

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
class PHSharedAlbumPostingViewController
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@interface PHSharedAlbumPostingViewController : UIViewController
```

*macOS*

```objc
@interface PHSharedAlbumPostingViewController : NSViewController
```

#### Overview

This class is used to present a view for posting assets to a shared album from AppKit-based view controllers.

## Topics

### Protocols
- [PHSharedAlbumPostingViewController.Delegate](./phsharedalbumpostingviewcontroller/delegate-swift.protocol.md)
### Initializers
- [convenience init(items: [PHPickerResult], defaultAlbumIdentifier: String?, photoLibrary: PHPhotoLibrary)](./phsharedalbumpostingviewcontroller/init%28items,defaultalbumidentifier,photolibrary%29.md)
  Returns a view controller that allows the user to create a new shared album.
### Instance Properties
- [var albumIdentifier: String?](./phsharedalbumpostingviewcontroller/albumidentifier.md)
  The identifier of the shared album that was posted to.
- [var delegate: (any PHSharedAlbumPostingViewController.Delegate)?](./phsharedalbumpostingviewcontroller/delegate-swift.property.md)
  The delegate to respond to `PHSharedAlbumPostingViewController` events.
### Instance Methods
- [- initWithItems:defaultAlbumIdentifier:photoLibrary:](./phsharedalbumpostingviewcontroller/initwithitems_defaultalbumidentifier_photolibrary_.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumpostingviewcontroller)*