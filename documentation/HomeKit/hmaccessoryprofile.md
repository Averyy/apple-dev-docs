# HMAccessoryProfile

**Framework**: HomeKit  
**Kind**: class

A profile that certain accessories implement.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 10.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class HMAccessoryProfile
```

#### Overview

This is an abstract superclass for classes such as [`HMCameraProfile`](hmcameraprofile.md) and [`HMNetworkConfigurationProfile`](hmnetworkconfigurationprofile.md). Each profile subclass controls specific features for a specific set of accessories.

## Topics

### Getting information about a profile
- [var accessory: HMAccessory?](hmaccessoryprofile/accessory.md)
  The accessory that implements this profile.
- [var services: [HMService]](hmaccessoryprofile/services.md)
  An array of services that represents this profile.
- [var uniqueIdentifier: UUID](hmaccessoryprofile/uniqueidentifier.md)
  A unique identifier for the profile.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [HMCameraProfile](hmcameraprofile.md)
- [HMMediaSourceDisplayOrderProfile](hmmediasourcedisplayorderprofile.md)
- [HMNetworkConfigurationProfile](hmnetworkconfigurationprofile.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var profiles: [HMAccessoryProfile]](hmaccessory/profiles.md)
  An array of profiles implemented by the accessory.
- [class HMNetworkConfigurationProfile](hmnetworkconfigurationprofile.md)
  A profile that provides information about network protection for an accessory.
- [class HMCameraProfile](hmcameraprofile.md)
  A camera profile that interacts with an accessory’s camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessoryprofile)*