# ImageCaptureCore

**Framework**: ImageCaptureCore  
**Kind**: module

Browse for media devices and control them programmatically from your app.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.6+
- visionOS 1.0+

#### Overview

Using ImageCaptureCore, your app can:

- Discover connected cameras and scanners
- View and modify the folders, files, and metadata on a connected camera
- Take photos directly on a connected camera using tethered capture
- Perform overview scans and scans on a connected scanner

![Diagram showing a macOS device connected by cables to a camera and a scanner, and an iPadOS device connected by cable to a camera.](https://docs-assets.developer.apple.com/published/0060df4265c83f5384bad802fb263ffd/media-3501083%402x.png)

##### Configuring Tethered Capture and Photo Import

To import pictures and tether from a macOS app, you first need to enable the Hardened Runtime capability in Xcode, and then add the [`Photos Library Entitlement`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.personal-information.photos-library).

Before you can tether from an iOS app, you need to tell the user why the app is requesting access to an external camera. Add the [`NSCameraUsageDescription`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSCameraUsageDescription) key to your `Info.plist` file with a description of your intended use.

> ❗ **Important**:  In macOS 14 and later, use the [`com.apple.security.device.usb`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.security.device.usb) entitlement key to allow your sandboxed app to interact with USB devices.

## Topics

### Essentials
- [class ICDeviceBrowser](icdevicebrowser.md)
  An object for finding digital cameras and scanners.
- [Photos Library Entitlement](../BundleResources/Entitlements/com.apple.security.personal-information.photos-library.md)
  A Boolean value that indicates whether the app has read-write access to the user’s Photos library.
- [NSCameraUsageDescription](../BundleResources/Information-Property-List/NSCameraUsageDescription.md)
  A message that tells the user why the app is requesting access to the device’s camera.
### Cameras
- [class ICCameraDevice](iccameradevice.md)
  An object that represents a camera.
- [protocol ICCameraDeviceDelegate](iccameradevicedelegate.md)
  Methods for detecting cameras, getting metadata and thumbnails, handling access and capability changes, and performing other actions on connected cameras.
- [class ICCameraItem](iccameraitem.md)
  An abstract class that represents a camera item.
- [class ICCameraFile](iccamerafile.md)
  An object that represents a file on a camera.
- [class ICCameraFolder](iccamerafolder.md)
  An object that represents a folder on a camera.
### Scanners
- [class ICScannerDevice](icscannerdevice.md)
  An object that represents a scanner.
- [protocol ICScannerDeviceDelegate](icscannerdevicedelegate.md)
  Methods for determining availability, selecting a functional unit, and performing scans on connected scanners.
- [Scanner Configuration](scanner-configuration.md)
  Examine a scanner’s functional units and features.
### Errors
- [ICReturn](icreturn.md)
  An error returned from ImageCaptureCore.
- [ICLegacyReturn](iclegacyreturn.md)
  A legacy error returned from ImageCaptureCore.
- [struct ICReturnConnectionError](icreturnconnectionerror.md)
  A connection error returned from ImageCaptureCore.
- [struct ICReturnDownloadError](icreturndownloaderror.md)
  A download error returned from ImageCaptureCore.
- [struct ICReturnMetadataError](icreturnmetadataerror.md)
  A metadata error returned from ImageCaptureCore.
- [struct ICReturnObjectError](icreturnobjecterror.md)
  An object error returned from ImageCaptureCore.
- [struct ICReturnPTPDeviceError](icreturnptpdeviceerror.md)
  A PTP device error returned from ImageCaptureCore.
- [struct ICReturnThumbnailError](icreturnthumbnailerror.md)
  A thumbnail error returned from ImageCaptureCore.
### Legacy Symbols
- [let ICRunLoopMode: String](icrunloopmode.md)
### Articles
- [ImageCaptureCore Constants](imagecapturecore-constants.md)
- [ImageCaptureCore Data Types](imagecapturecore-data-types.md)
- [ImageCaptureCore Enumerations](imagecapturecore-enumerations.md)
- [ImageCaptureCore Macros](imagecapturecore-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/ImageCaptureCore)*