# AVContinuityDevicePickerViewController

**Framework**: AVKit  
**Kind**: class  
**Role**: Class

A view controller that provides an interface to a person so they can select and connect a continuity device to the system.

**Availability**:
- tvOS 17.0+

## Declaration

```swift
class AVContinuityDevicePickerViewController
```

```objc
@interface AVContinuityDevicePickerViewController : UIViewController
```

## Overview

The view controller presents an interface on an Apple TV that lets a person choose a nearby continuity device ([`AVContinuityDevice`](../AVFoundation/avcontinuitydevice.md)). Your app can then connect to that device’s cameras and microphones (see [`AVCaptureDevice`](../AVFoundation/avcapturedevice.md) and [`AVAudioSessionPortDescription`](../AVFAudio/avaudiosessionportdescription.md), respectively).

> ❗ **Important**:  The continuity device picker presents any devices near the Apple TV that use the same Apple ID.

To respond to the various outcome events from the picker, your app needs to implement the [`AVContinuityDevicePickerViewControllerDelegate`](./avcontinuitydevicepickerviewcontrollerdelegate.md) and assign it to the picker’s [`delegate`](./avcontinuitydevicepickerviewcontroller/delegate.md) property.

> **Note**:  SwiftUI apps can present the same interface with the [`continuityDevicePicker(isPresented:onDidConnect:)`](../SwiftUI/view/continuitydevicepicker%28ispresented,ondidconnect%29.md) view modifier.

## Topics

### Checking for feature support
- [class var isSupported: Bool](./avcontinuitydevicepickerviewcontroller/issupported.md)
  A Boolean value that indicates whether the system supports connecting to a continuity device.
### Designating a delegate
- [var delegate: (any AVContinuityDevicePickerViewControllerDelegate)?](./avcontinuitydevicepickerviewcontroller/delegate.md)
  The delegate that responds to events from the continuity device picker view controller.

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Continuity Camera
- [Supporting Continuity Camera in your tvOS app](./supporting-continuity-camera-in-your-tvos-app.md)
  Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- [protocol AVContinuityDevicePickerViewControllerDelegate](./avcontinuitydevicepickerviewcontrollerdelegate.md)
  An interface that responds to events from a continuity device picker view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontinuitydevicepickerviewcontroller)*