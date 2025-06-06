# AVExternalStorageDevice

**Framework**: AVFoundation  
**Kind**: class

Represents a physical external storage device that stores media assets.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+

## Declaration

```swift
class AVExternalStorageDevice
```

#### Overview

Each storage device instance corresponds to a physical external storage device where the system can media assets. You can access all of the currently available external storage devices with the [`AVExternalStorageDeviceDiscoverySession`](avexternalstoragedevicediscoverysession.md) object’s [`externalStorageDevices`](avexternalstoragedevicediscoverysession/externalstoragedevices.md) property.

## Topics

### Checking permission to generate URLs
- [class var authorizationStatus: AVAuthorizationStatus](avexternalstoragedevice/authorizationstatus.md)
  Your app’s authorization status for the external storage device.
### Requesting permission to generate URLs
- [class func requestAccess(completionHandler: (Bool) -> Void)](avexternalstoragedevice/requestaccess(completionhandler:).md)
  Requests access to an external storage device on behalf of your app, which can present a dialog to a person on their device’s display.
### Generating URLs for image assets
- [func nextAvailableURLs(withPathExtensions: [String]) throws -> [URL]](avexternalstoragedevice/nextavailableurls(withpathextensions:).md)
  Generates an array of security scoped URLs that are compliant for digital camera formats, where each element has a different path extension.
### Inspecting a storage device
- [var isConnected: Bool](avexternalstoragedevice/isconnected.md)
  A Boolean value that indicates whether the system has a connection to the external storage device.
- [var displayName: String?](avexternalstoragedevice/displayname.md)
  The name of an external storage device that’s appropriate for a user interface.
- [var uuid: UUID?](avexternalstoragedevice/uuid.md)
  The external storage device’s unique identifier.
- [var freeSize: Int](avexternalstoragedevice/freesize.md)
  The amount of free storage space, in bytes, that’s available on the external storage device.
- [var totalSize: Int](avexternalstoragedevice/totalsize.md)
  The total amount of storage space, in bytes, that’s available on the external storage device.
- [var isNotRecommendedForCaptureUse: Bool](avexternalstoragedevice/isnotrecommendedforcaptureuse.md)
  A Boolean value that indicates whether the external storage device is suitable for camera capture.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Choosing a Capture Device](choosing-a-capture-device.md)
  Select the front or back camera, or use advanced features like the TrueDepth camera or dual camera.
- [class AVCaptureDevice](avcapturedevice.md)
  An object that represents a hardware or virtual capture device like a camera or microphone.
- [class AVCaptureDeviceInput](avcapturedeviceinput.md)
  An object that provides media input from a capture device to a capture session.
- [class AVContinuityDevice](avcontinuitydevice.md)
  A class that represents a physical iOS device that’s nearby and can provide access to its cameras and microphones.
- [class AVExternalStorageDeviceDiscoverySession](avexternalstoragedevicediscoverysession.md)
  Informs your app when the external storage devices connect to and disconnect from the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avexternalstoragedevice)*