# UserCallMediaParametersHaveChanged

**Framework**: SCSIControllerDriverKit  
**Kind**: method  
**Role**: Instance Method

Indicates to the system that the media parameters changed.

**Availability**:
- DriverKit

## Declaration

```cpp
virtual kern_return_t UserCallMediaParametersHaveChanged();
```

#### Return Value

A value that indicates the result of handling the change. [`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) indicates success. For error definitions, see [IOKit Constants](../../iokit/iokit_constants.md).

#### Discussion

After calling this method, the framework checks the medium-capacity data — the block size and block count — and takes necessary action if they changed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scsicontrollerdriverkit/iouserscsiparallelinterfacecontroller/usercallmediaparametershavechanged)*