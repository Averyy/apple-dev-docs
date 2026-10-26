# AUViewController

**Framework**: CoreAudioKit  
**Kind**: class  
**Role**: Class

The base class to extend when creating a custom user interface for an audio unit.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class AUViewController
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@interface AUViewController : UIViewController
```

*macOS*

```objc
@interface AUViewController : NSViewController
```

#### Overview

This class doesn’t add any new methods or properties to its superclass, but it does conform to the [`NSExtensionRequestHandling`](../Foundation/nsextensionrequesthandling.md) protocol.

A host app can access the view controller by calling the [`requestViewController(completionHandler:)`](../AudioToolbox/auaudiounit/requestviewcontroller%28completionhandler%29.md) method on the corresponding [`AUAudioUnit`](../AudioToolbox/auaudiounit.md) object.

##### Subclassing Notes

If an audio unit provides a custom view controller, the UI Audio Unit extension must implement a subclass of `AUViewController` and implement the [`AUAudioUnitFactory`](../AudioToolbox/auaudiounitfactory.md) protocol inside the subclass.

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

### Audio Units
- [class AUAudioUnitViewConfiguration](./auaudiounitviewconfiguration.md)
  A configuration object that describes how to present the audio unit’s user interface.
- [class AUGenericView](./augenericview.md)
  A view that provides a generic user interface for a Cocoa audio unit.
- [class AUPannerView](./aupannerview.md)
  A view that provides a specialized user interface for a Cocoa-based panner audio unit.
- [protocol AUCustomViewPersistentData](./aucustomviewpersistentdata.md)
  A protocol that defines the methods an Audio Unit host calls to manage view data.
- [AUViewControllerBase](./auviewcontrollerbase.md)
  A type definition that indicates the the platform’s Audio Unit view controller base class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiokit/auviewcontroller)*