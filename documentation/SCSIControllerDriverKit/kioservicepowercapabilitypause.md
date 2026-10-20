# kIOServicePowerCapabilityPause

**Framework**: SCSIControllerDriverKit  
**Kind**: macro  
**Role**: Macro

A PCIe-specific power state for halting transactions while reallocating resources.

**Availability**:
- DriverKit

## Declaration

```c
#define kIOServicePowerCapabilityPause
```

#### Discussion

[`IOUserSCSIParallelInterfaceController`](./iouserscsiparallelinterfacecontroller.md) supports this power state, in addition to the [`kIOServicePowerCapabilityOn`](../DriverKit/kioservicepowercapabilityon.md) and [`kIOServicePowerCapabilityOff`](../DriverKit/kioservicepowercapabilityoff.md) power states defined in the base [DriverKit](../DriverKit/DriverKit.md) framework. Implement the [`SetPowerState`](../DriverKit/ioservice/setpowerstate.md) method in your service object and use it to put your driver in a safe state for any of these power states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/kioservicepowercapabilitypause)*