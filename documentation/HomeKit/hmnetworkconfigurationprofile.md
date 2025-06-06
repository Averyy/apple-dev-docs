# HMNetworkConfigurationProfile

**Framework**: HomeKit  
**Kind**: class

A profile that provides information about network protection for an accessory.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class HMNetworkConfigurationProfile
```

#### Overview

To increase security, HomeKit can restrict network access for specific accessories, including access to other accessories in the home, and to the internet. However, an accessory your app controls might need network access to carry out certain functions, like downloading new firmware.

Check the [`isNetworkAccessRestricted`](hmnetworkconfigurationprofile/isnetworkaccessrestricted.md) property of an accessory’s network configuration profile to find out if an accessory has restricted access. You can use this information to ask the user to relax network restrictions in the Home app.

## Topics

### Restricting network access
- [var isNetworkAccessRestricted: Bool](hmnetworkconfigurationprofile/isnetworkaccessrestricted.md)
  An indication of whether the accessory’s access to the network is restricted.
### Listening for access changes
- [var delegate: (any HMNetworkConfigurationProfileDelegate)?](hmnetworkconfigurationprofile/delegate.md)
  A delegate that HomeKit tells about changes in the state of network access.
- [protocol HMNetworkConfigurationProfileDelegate](hmnetworkconfigurationprofiledelegate.md)
  An interface that your app adopts to receive notifications about changes in the state of network access.

## Relationships

### Inherits From
- [HMAccessoryProfile](hmaccessoryprofile.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var profiles: [HMAccessoryProfile]](hmaccessory/profiles.md)
  An array of profiles implemented by the accessory.
- [class HMAccessoryProfile](hmaccessoryprofile.md)
  A profile that certain accessories implement.
- [class HMCameraProfile](hmcameraprofile.md)
  A camera profile that interacts with an accessory’s camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmnetworkconfigurationprofile)*