# kIOServicePowerCapabilityPause

**Framework**: SCSIControllerDriverKit  
**Kind**: macro

A PCIe-specific power state for halting transactions while reallocating resources.

**Availability**:
- DriverKit ?+

## Declaration

```swift
#define kIOServicePowerCapabilityPause
```

#### Discussion

[`IOUserSCSIParallelInterfaceController`](iouserscsiparallelinterfacecontroller.md) supports this power state, in addition to the [`kIOServicePowerCapabilityOn`](https://developer.apple.com/documentation/DriverKit/kIOServicePowerCapabilityOn) and [`kIOServicePowerCapabilityOff`](https://developer.apple.com/documentation/DriverKit/kIOServicePowerCapabilityOff) power states defined in the base [`DriverKit`](https://developer.apple.com/documentation/DriverKit) framework. Implement the [`SetPowerState`](https://developer.apple.com/documentation/DriverKit/IOService/SetPowerState) method in your service object and use it to put your driver in a safe state for any of these power states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/kioservicepowercapabilitypause)*