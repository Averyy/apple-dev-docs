# ICDeviceBrowser

**Framework**: ImageCaptureCore  
**Kind**: class

An object for finding digital cameras and scanners.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
class ICDeviceBrowser
```

## Topics

### Creating a Device Browser
- [init()](icdevicebrowser/init.md)
  Creates an ImageCaptureCore device browser.
### Managing Device Browsing
- [var delegate: (any ICDeviceBrowserDelegate)?](icdevicebrowser/delegate.md)
  The object that acts as the delegate of the device browser.
- [protocol ICDeviceBrowserDelegate](icdevicebrowserdelegate.md)
  Methods for managing the addition and removal of devices and responding to device changes.
### Browsing Devices
- [var isBrowsing: Bool](icdevicebrowser/isbrowsing.md)
  A Boolean value indicating whether the device browser is browsing for devices.
- [var devices: [ICDevice]?](icdevicebrowser/devices.md)
  All devices found by the browser.
- [class ICDevice](icdevice.md)
  An abstract object that represents a device.
- [var browsedDeviceTypeMask: ICDeviceTypeMask](icdevicebrowser/browseddevicetypemask.md)
  A mask whose set bits indicate the type of devices being browsed after the delegate receives the start message.
- [func start()](icdevicebrowser/start.md)
  Tells the delegate to start looking for devices.
- [func stop()](icdevicebrowser/stop.md)
  Tells the delegate to stop looking for devices.
### Setting a Preferred Device
- [var preferredDevice: ICDevice?](icdevicebrowser/preferreddevice.md)
  Returns a device object that the client application should select when it launches.
### Instance Properties
- [var contentsAuthorizationStatus: ICAuthorizationStatus](icdevicebrowser/contentsauthorizationstatus.md)
- [var controlAuthorizationStatus: ICAuthorizationStatus](icdevicebrowser/controlauthorizationstatus.md)
- [var isSuspended: Bool](icdevicebrowser/issuspended.md)
### Instance Methods
- [func requestContentsAuthorization(completion: (ICAuthorizationStatus) -> Void)](icdevicebrowser/requestcontentsauthorization(completion:).md)
- [func requestControlAuthorization(completion: (ICAuthorizationStatus) -> Void)](icdevicebrowser/requestcontrolauthorization(completion:).md)
- [func resetContentsAuthorization(completion: (ICAuthorizationStatus) -> Void)](icdevicebrowser/resetcontentsauthorization(completion:).md)
- [func resetControlAuthorization(completion: (ICAuthorizationStatus) -> Void)](icdevicebrowser/resetcontrolauthorization(completion:).md)

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

- [Photos Library Entitlement](../BundleResources/Entitlements/com.apple.security.personal-information.photos-library.md)
  A Boolean value that indicates whether the app has read-write access to the user’s Photos library.
- [NSCameraUsageDescription](../BundleResources/Information-Property-List/NSCameraUsageDescription.md)
  A message that tells people why the app is requesting access to the device’s camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icdevicebrowser)*