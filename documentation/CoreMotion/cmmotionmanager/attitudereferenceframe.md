# attitudeReferenceFrame

**Framework**: Core Motion  
**Kind**: property

Returns either the reference frame currently being used or the default attitude reference frame.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var attitudeReferenceFrame: CMAttitudeReferenceFrame { get }
```

## Mentions

- [Getting processed device-motion data](getting-processed-device-motion-data.md)

#### Discussion

If the device-motion service is active, this property returns the reference frame currently in use. If the service is inactive, but your app started it at some point since launch, this property contains the last reference frame you used. If you haven’t started the device-motion service since app launch, this property returns the default frame of reference, which is [`xArbitraryZVertical`](cmattitudereferenceframe/xarbitraryzvertical.md).

If device motion is not available on the current device, the value of this property is undefined.

## See Also

- [var isDeviceMotionAvailable: Bool](cmmotionmanager/isdevicemotionavailable.md)
  A Boolean value that indicates whether the device-motion service is available on the device.
- [class func availableAttitudeReferenceFrames() -> CMAttitudeReferenceFrame](cmmotionmanager/availableattitudereferenceframes.md)
  Returns a bitmask of the available reference frames for reporting the attitude of the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmmotionmanager/attitudereferenceframe)*