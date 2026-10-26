# PHSharedAlbumCustomizationViewController

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
class PHSharedAlbumCustomizationViewController
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@interface PHSharedAlbumCustomizationViewController : UIViewController
```

*macOS*

```objc
@interface PHSharedAlbumCustomizationViewController : NSViewController
```

#### Overview

This class is used to present the shared album customization view from AppKit-based view controllers.

Only the system photo library is supported, so `albumIdentifier` must be for an album in the system photo library. If `albumIdentifier` is from a different library, showing a customization sheet will fail.

## Topics

### Protocols
- [PHSharedAlbumCustomizationViewController.Delegate](./phsharedalbumcustomizationviewcontroller/delegate-swift.protocol.md)
### Initializers
- [init(albumIdentifier: String, photoLibrary: PHPhotoLibrary)](./phsharedalbumcustomizationviewcontroller/init%28albumidentifier,photolibrary%29.md)
### Instance Properties
- [var albumIdentifier: String](./phsharedalbumcustomizationviewcontroller/albumidentifier.md)
  The identifier of the shared album to be customized.
- [var delegate: (any PHSharedAlbumCustomizationViewController.Delegate)?](./phsharedalbumcustomizationviewcontroller/delegate-swift.property.md)
  The delegate to respond to `PHSharedAlbumCustomizationViewController` events.

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

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phsharedalbumcustomizationviewcontroller)*