# UIRequiredDeviceCapabilities

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

The device-related features that your app requires to run.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Details

- **Name**: `UIRequiredDeviceCapabilities` (Required device capabilities)
- **Type**: array of string 

## Possible Values

- `accelerometer`: The presence of accelerometers. Use the [Core Motion](../../CoreMotion/CoreMotion.md) framework to receive accelerometer events. You don’t need to include this value if your app detects only device orientation changes. Available in iOS 3.0 and later. Unavailable in visionOS.
- `arkit`: Support for [ARKit](../../ARKit/ARKit.md). Available in iOS 11.0 and later, and Full Space apps in visionOS. Unavailable for iPadOS and iOS apps running in visionOS.
- `armv7`: Compilation for the `armv7` instruction set, or as a 32- or 64-bit universal app. Available in iOS 3.1 and later, and visionOS.
- `arm64`: Compilation for the `arm64` instruction set. Include this key for all 64-bit apps and embedded bundles, like extensions and frameworks. Available in iOS 8.0 and later, and visionOS.
- `auto-focus-camera`: Autofocus capabilities in the device’s still camera. You might need to include this value if your app supports macro photography or requires sharper images to perform certain image-processing tasks. Available in iOS 3.0 and later. Unavailable in visionOS.
- `bluetooth-le`: Bluetooth low-energy hardware. Available in iOS 5.0 and later, and visionOS.
- `camera-flash`: A camera flash. Use the [`cameraFlashMode`](../../UIKit/uiimagepickercontroller/cameraflashmode-swift.property.md) property of a [`UIImagePickerController`](../../UIKit/uiimagepickercontroller.md) instance to control the camera’s flash. Available in iOS 3.0 and later. Unavailable in visionOS.
- `driverkit`: Support for [DriverKit](../../DriverKit/DriverKit.md) on devices with M1 or later chips. Available on iPadOS 16.0 or later. Unavailable in visionOS.
- `front-facing-camera`: A forward-facing camera. Use the [`cameraDevice`](../../UIKit/uiimagepickercontroller/cameradevice-swift.property.md) property of a [`UIImagePickerController`](../../UIKit/uiimagepickercontroller.md) instance to select the device’s camera. Available in iOS 3.0 and later, and iPadOS and iOS apps running in visionOS. Unavailable in apps built for visionOS.
- `gamekit`: Access to the Game Center service. Enable the Game Center capability in Xcode to add this value to your app. Available in iOS 4.1 and later, and visionOS.
- `gps`: GPS (or AGPS) hardware for tracking locations. If you include this value, you should also include the location-services value. Require GPS only if your app needs location data more accurate than the cellular or Wi-Fi radios provide. Available in iOS 3.0 and later. Unavailable in visionOS.
- `gyroscope`: A gyroscope. Use the [Core Motion](../../CoreMotion/CoreMotion.md) framework to retrieve information from gyroscope hardware. Available in iOS 3.0 and later. Unavailable in visionOS.
- `healthkit`: Support for [HealthKit](../../HealthKit/HealthKit.md). The system uses this value to limit apps to iPhone. In order to ship Universal apps, remove this key. Available in iOS 8.0 and later. Unavailable in visionOS.
- `iphone-performance-gaming-tier`: Requires the graphics performance and gaming features equivalent to the iPhone 15 Pro and iPhone 15 Pro Max. Available in iOS 17.0 and later. Unavailable in visionOS.
- `iphone-ipad-minimum-performance-a12`: Performance and capabilities of the A12 Bionic and later chips. Available in iOS 12.0 and later, and iPadOS and iOS apps running in visionOS. Unavailable in apps built for visionOS.
- `location-services`: Access to the device’s current location using the [Core Location](../../CoreLocation/CoreLocation.md) framework. This value refers to the general location services feature. If you specifically need GPS-level accuracy, also include the `gps` feature. Available in iOS 3.0 and later, and visionOS.
- `magnetometer`: Magnetometer hardware. Apps use this hardware to receive heading-related events through the [Core Location](../../CoreLocation/CoreLocation.md) framework. Available in iOS 3.0 and later. Unavailable in visionOS.
- `metal`: Support for graphics processing with [Metal](../../Metal/Metal.md). Available in iOS 8.0 and later, and visionOS.
- `microphone`: The built-in microphone or accessories that provide a microphone. Available in iOS 3.0 and later, and visionOS.
- `nfc`: Near Field Communication (NFC) tag detection and access to messages that contain NFC Data Exchange Format data. Use the [Core NFC](../../CoreNFC/CoreNFC.md) framework to detect and read NFC tags. Available in iOS 11.0 and later. Unavailable in visionOS.
- `opengles-1`: The OpenGL ES 1.1 interface. Available in iOS 3.0 and later, and iPadOS and iOS apps running in visionOS. Unavailable in apps built for visionOS.
- `opengles-2`: The OpenGL ES 2.0 interface. Available in iOS 3.0 and later, and iPadOS and iOS apps running in visionOS. Unavailable in apps built for visionOS.
- `opengles-3`: The OpenGL ES 3.0 interface. Available in iOS 7.0 and later, and iPadOS and iOS apps running in visionOS. Unavailable in apps built for visionOS.
- `peer-peer`: Peer-to-peer connectivity over a Bluetooth network. Available in iOS 3.1 and later, and visionOS. The App Store doesn’t prevent distributing an app to a device that doesn’t support this capability, but iOS prevents running the app.
- `sms`: The Messages app. You might require this feature if your app opens URLs with the `sms` scheme. Available in iOS 3.0 and later. Unavailable in visionOS.
- `still-camera`: A camera on the device. Use the [`UIImagePickerController`](../../UIKit/uiimagepickercontroller.md) interface to capture images from the device’s still camera. Available in iOS 3.0 and later. Unavailable in visionOS.
- `telephony`: The Phone app. You might require this feature if your app opens URLs with the `tel` scheme. Available in iOS 3.0 and later. Unavailable in visionOS.
- `video-camera`: A camera with video capabilities on the device. Use the [`UIImagePickerController`](../../UIKit/uiimagepickercontroller.md) interface to capture video from the device’s camera. Available in iOS 3.0 and later, and visionOS.
- `wifi`: Networking features related to Wi-Fi access. Available in iOS 3.0 and later, and visionOS.

#### Discussion

The App Store prevents customers from installing an app on a device that doesn’t support the required capabilities for that app. Use this key to declare the capabilities your app requires. For a list of the features that different devices support, see [Required Device Capabilities](https://developer.apple.com/support/required-device-capabilities/).

You typically use an array for the key’s associated value. The presence in that array of any of the above possible values indicates that the app requires the corresponding feature. Omit a value to indicate that the app doesn’t require the feature, but it can be present.

Alternatively, you can use a dictionary as the associated value for the [`UIRequiredDeviceCapabilities`](./uirequireddevicecapabilities.md) key. In that case, use the values above as the dictionary’s keys, each with an associated Boolean value. Set the value to `true` to require the corresponding feature. Set the value to `false` to indicate that the feature must not be present on the device. Omit the feature from the dictionary to indicate that your app neither requires nor disallows it.

Specify only the features that your app absolutely requires. If your app can accommodate missing features by avoiding the code paths that use those features, don’t include the corresponding key.

> ❗ **Important**:  Your app must include the [`UIRequiredDeviceCapabilities`](./uirequireddevicecapabilities.md) key in the [`Information Property List`](../information-property-list.md) file that you submit with your binary. For app updates, you can only maintain or relax capability requirements. Submitting an update with added requirements would prevent some customers who previously downloaded your app from running the update.

## See Also

### Launch conditions
- [LSMultipleInstancesProhibited](./lsmultipleinstancesprohibited.md)
  A Boolean value indicating whether more than one user can launch the app simultaneously.
- [LSArchitecturePriority](./lsarchitecturepriority.md)
  An array of the architectures that the app supports, arranged according to their preferred usage.
- [LSRequiresNativeExecution](./lsrequiresnativeexecution.md)
  A Boolean value that indicates whether to require the execution of the app’s native architecture when multiple architectures are available.
- [WKPrefersNetworkUponForeground](./wkprefersnetworkuponforeground.md)
  A Boolean value that indicates whether an app requires network access on launch.
- [WKRunsIndependentlyOfCompanionApp](./wkrunsindependentlyofcompanionapp.md)
  A Boolean value indicating whether the user can install and run the watchOS app independently of its iOS companion app.
- [WKWatchOnly](./wkwatchonly.md)
  A Boolean value indicating whether the app is a watch-only app.
- [PUICAutoLaunchAudioOptOut](./puicautolaunchaudiooptout.md)
  A Boolean value that indicates whether a watchOS app should opt out of automatically launching when its companion iOS app starts playing audio content.
- [CLKComplicationSupportedFamilies](./clkcomplicationsupportedfamilies.md)
  The complication families for which the app can provide data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/uirequireddevicecapabilities)*