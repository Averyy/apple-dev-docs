# PHPickerViewController

**Framework**: PhotosUI  
**Kind**: class  
**Role**: Class

A view controller that provides the user interface for choosing assets from the photo library.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class PHPickerViewController
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@interface PHPickerViewController : UIViewController
```

*macOS*

```objc
@interface PHPickerViewController : NSViewController
```

## Mentions

- [Delivering an Enhanced Privacy Experience in Your Photos App](../PhotoKit/delivering-an-enhanced-privacy-experience-in-your-photos-app.md)

## Overview

The `PHPickerViewController` class is an alternative to [`UIImagePickerController`](../UIKit/uiimagepickercontroller.md). `PHPickerViewController` improves stability and reliability, and includes several benefits to developers and users, such as the following:

- Deferred image loading and recovery UI
- Reliable handling of large and complex assets, like RAW and panoramic images
- User-selectable assets that aren’t available for [`UIImagePickerController`](../UIKit/uiimagepickercontroller.md)
- Configuration of the picker to display only Live Photos
- Availability of [`PHLivePhoto`](../Photos/phlivephoto.md) objects without library access
- Stricter validations against invalid inputs

### Observe required viewing standards

As a view controller that the system renders on top of your app, the picker controller requires certain prerequisites for operation that your app needs to observe:

- The picker controller disables user interaction if an app alters its visibility, such as by adjusting the [`opacity`](../QuartzCore/calayer/opacity.md) of its view’s layer. In iOS 17 and later, the picker controller ignores touch events while its opacity is anything other than fully opaque.
- As a system-rendered UI, you can’t subclass [`PHPickerViewController`](./phpickerviewcontroller.md). Its view hierarchy belongs to the system and therefore, the framework provides no access.

## Topics

### Creating a picker
- [convenience init(configuration: PHPickerConfiguration)](./phpickerviewcontroller/init%28configuration%29.md)
  Creates a new picker view controller with the configuration you specify.
- [struct PHPickerConfiguration](./phpickerconfiguration-swift.struct.md)
  An object that contains information about how to configure a picker view controller.
- [- initWithConfiguration:](./phpickerviewcontroller/initwithconfiguration_.md)
  Creates a new picker view controller with the configuration you specify.
- [PHPickerConfiguration](./phpickerconfiguration-c.class.md)
  An object that contains information about how to configure a picker view controller.
### Managing the configuration
- [var configuration: PHPickerConfiguration](./phpickerviewcontroller/configuration-17a8p.md)
  The configuration you specify when creating the picker.
- [func updatePicker(using: PHPickerConfiguration.Update)](./phpickerviewcontroller/updatepicker%28using%29.md)
  Customizes your app’s photo picker according to the given configuration.
- [configuration](./phpickerviewcontroller/configuration-3vf53.md)
  The configuration you specify when creating the picker.
- [- updatePickerUsingConfiguration:](./phpickerviewcontroller/updatepickerusingconfiguration_.md)
  Customizes your app’s photo picker according to the given configuration.
### Setting content position and scale
- [func scrollToInitialPosition()](./phpickerviewcontroller/scrolltoinitialposition%28%29.md)
  Resets the visible photo thumbnails by scrolling the view to the picker’s initial position.
- [func zoomIn()](./phpickerviewcontroller/zoomin%28%29.md)
  Changes the picker’s content scale by making the photo thumbnails larger in the view.
- [func zoomOut()](./phpickerviewcontroller/zoomout%28%29.md)
  Changes the picker’s content scale by making the photo thumbnails smaller in the view.
### Responding to user selection
- [var delegate: (any PHPickerViewControllerDelegate)?](./phpickerviewcontroller/delegate-3zqmt.md)
  The picker’s delegate object.
- [protocol PHPickerViewControllerDelegate](./phpickerviewcontrollerdelegate-5yntc.md)
  A set of methods that the delegate must implement to respond to `PHPickerViewController` user events.
- [struct PHPickerResult](./phpickerresult-swift.struct.md)
  Types that represent a selected asset from a person’s photo library.
- [delegate](./phpickerviewcontroller/delegate-8dlnb.md)
  The picker’s delegate object.
- [PHPickerViewControllerDelegate](./phpickerviewcontrollerdelegate-9y5xc.md)
  A protocol the picker uses to communicate user selections.
- [PHPickerResult](./phpickerresult-c.class.md)
  Types that represent a selected asset from a person’s photo library.
### Deselecting assets
- [func deselectAssets(withIdentifiers: [String])](./phpickerviewcontroller/deselectassets%28withidentifiers%29.md)
  Deselects assets that are in a selected state.
### Reordering assets
- [func moveAsset(withIdentifier: String, afterAssetWithIdentifier: String?)](./phpickerviewcontroller/moveasset%28withidentifier,afterassetwithidentifier%29.md)
  Reorders assets that are in a selected state.

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

## See Also

### Photos picker for UIKit, AppKit
- [Selecting Photos and Videos in iOS](../PhotoKit/selecting-photos-and-videos-in-ios.md)
  Improve the user experience of finding and selecting assets by using the Photos picker.
- [protocol PHPickerViewControllerDelegate](./phpickerviewcontrollerdelegate-5yntc.md)
  A set of methods that the delegate must implement to respond to `PHPickerViewController` user events.
- [struct PHPickerConfiguration](./phpickerconfiguration-swift.struct.md)
  An object that contains information about how to configure a picker view controller.
- [struct PHPickerFilter](./phpickerfilter-swift.struct.md)
  A type that defines the filter to apply to the photo library.
- [struct PHPickerResult](./phpickerresult-swift.struct.md)
  Types that represent a selected asset from a person’s photo library.
- [PHPickerConfiguration](./phpickerconfiguration-c.class.md)
  An object that contains information about how to configure a picker view controller.
- [PHPickerFilter](./phpickerfilter-c.class.md)
  A type that defines the filter to apply to the photo library.
- [PHPickerResult](./phpickerresult-c.class.md)
  Types that represent a selected asset from a person’s photo library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/photosui/phpickerviewcontroller)*