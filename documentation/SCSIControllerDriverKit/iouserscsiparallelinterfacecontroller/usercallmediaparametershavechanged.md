# UserCallMediaParametersHaveChanged

**Framework**: SCSIControllerDriverKit  
**Kind**: method

Indicates to the system that the media parameters changed.

**Availability**:
- DriverKit ?+

## Declaration

```swift
virtual kern_return_t UserCallMediaParametersHaveChanged();
```

#### Return Value

A value that indicates the result of handling the change. [`kIOReturnSuccess`](https://developer.apple.com/documentation/driverkit/kioreturnsuccess) indicates success. For error definitions, see [`IOKit Constants`](https://developer.apple.com/documentation/iokit/iokit_constants).

#### Discussion

After calling this method, the framework checks the medium-capacity data — the block size and block count — and takes necessary action if they changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usercallmediaparametershavechanged)*