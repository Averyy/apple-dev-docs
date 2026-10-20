# profiles

**Framework**: HomeKit  
**Kind**: property  
**Role**: Instance Property

An array of profiles implemented by the accessory.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var profiles: [HMAccessoryProfile] { get }
```

```objc
@property (copy, readonly) NSArray<HMAccessoryProfile *> * profiles;
```

## See Also

### Managing accessory profiles
- [class HMAccessoryProfile](../hmaccessoryprofile.md)
  A profile that certain accessories implement.
- [class HMNetworkConfigurationProfile](../hmnetworkconfigurationprofile.md)
  A profile that provides information about network protection for an accessory.
- [class HMCameraProfile](../hmcameraprofile.md)
  A camera profile that interacts with an accessory’s camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmaccessory/profiles)*