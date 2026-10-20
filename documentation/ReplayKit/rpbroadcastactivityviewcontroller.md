# RPBroadcastActivityViewController

**Framework**: ReplayKit  
**Kind**: class  
**Role**: Class

A view controller that displays a user interface where users choose a broadcast service.

**Availability**:
- iOS 10.0+ - Deprecated in 27.0
- iPadOS 10.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: No longer supported

## Declaration

```swift
class RPBroadcastActivityViewController
```

```objc
@interface RPBroadcastActivityViewController : UIViewController
```

#### Overview

The view controller displays the broadcast services currently installed on the device. On iPad, you must present the broadcast activity view controller as a popover.

## Topics

### Presenting the Broadcast Activity UI
- [class func load(handler: (RPBroadcastActivityViewController?, (any Error)?) -> Void)](./rpbroadcastactivityviewcontroller/load%28handler%29.md)
  Loads a broadcast activity view controller.
- [class func load(withPreferredExtension: String?, handler: (RPBroadcastActivityViewController?, (any Error)?) -> Void)](./rpbroadcastactivityviewcontroller/load%28withpreferredextension,handler%29.md)
  Loads a broadcast activity view controller with a preferred extension.
### Getting the Delegate
- [var delegate: (any RPBroadcastActivityViewControllerDelegate)?](./rpbroadcastactivityviewcontroller/delegate.md)
  The delegate for the broadcast activity view controller.
- [protocol RPBroadcastActivityViewControllerDelegate](./rpbroadcastactivityviewcontrollerdelegate.md)
  The protocol you implement to respond to changes to a broadcast activity user interface.

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

### Live Broadcast Implementation
- [class RPSystemBroadcastPickerView](./rpsystembroadcastpickerview.md)
  A view displaying a broadcast button that, when tapped, shows a broadcast picker.
- [class RPBroadcastActivityController](./rpbroadcastactivitycontroller.md)
  A controller object that presents the macOS broadcast picker.
- [protocol RPBroadcastActivityControllerDelegate](./rpbroadcastactivitycontrollerdelegate.md)
  A protocol that defines the methods to implement to respond to selection events from a broadcast activity controller.
- [class RPBroadcastConfiguration](./rpbroadcastconfiguration.md)
  An object used to configure the movie clips produced during a live broadcast.


---

*[View on Apple Developer](https://developer.apple.com/documentation/replaykit/rpbroadcastactivityviewcontroller)*