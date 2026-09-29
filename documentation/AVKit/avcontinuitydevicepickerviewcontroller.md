# AVContinuityDevicePickerViewController

**Framework**: AVKit  
**Kind**: class

A view controller that provides an interface to a person so they can select and connect a continuity device to the system.

**Availability**:
- tvOS 17.0+

## Declaration

```swift
class AVContinuityDevicePickerViewController
```

#### Overview

The view controller presents an interface on an Apple TV that lets a person choose a nearby continuity device ([`AVContinuityDevice`](https://developer.apple.com/documentation/avfoundation/avcontinuitydevice)). Your app can then connect to that device’s cameras and microphones (see [`AVCaptureDevice`](https://developer.apple.com/documentation/avfoundation/avcapturedevice) and [`AVAudioSessionPortDescription`](https://developer.apple.com/documentation/avfaudio/avaudiosessionportdescription), respectively).

> ❗ **Important**:  The continuity device picker presents any devices near the Apple TV that use the same Apple ID.

To respond to the various outcome events from the picker, your app needs to implement the [`AVContinuityDevicePickerViewControllerDelegate`](avcontinuitydevicepickerviewcontrollerdelegate.md) and assign it to the picker’s [`delegate`](avcontinuitydevicepickerviewcontroller/delegate.md) property.

> **Note**:  SwiftUI apps can present the same interface with the [`continuityDevicePicker(isPresented:onDidConnect:)`](https://developer.apple.com/documentation/swiftui/view/continuitydevicepicker(ispresented:ondidconnect:)) view modifier.

## Topics

### Checking for feature support
- [class var isSupported: Bool](avcontinuitydevicepickerviewcontroller/issupported.md)
  A Boolean value that indicates whether the system supports connecting to a continuity device.
### Designating a delegate
- [var delegate: (any AVContinuityDevicePickerViewControllerDelegate)?](avcontinuitydevicepickerviewcontroller/delegate.md)
  The delegate that responds to events from the continuity device picker view controller.

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
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [Supporting Continuity Camera in your tvOS app](supporting-continuity-camera-in-your-tvos-app.md)
  Capture high-quality photos, video, and audio in your Apple TV app by connecting an iPhone or iPad as a continuity device.
- [protocol AVContinuityDevicePickerViewControllerDelegate](avcontinuitydevicepickerviewcontrollerdelegate.md)
  An interface that responds to events from a continuity device picker view controller.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcontinuitydevicepickerviewcontroller)*