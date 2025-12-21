# destroy(options:)

**Framework**: IOUSBHost  
**Kind**: method

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
func destroy(options: IOUSBHostObjectDestroyOptions = [])
```

#### Discussion

Removes underlying allocations of the IOUSBHostObject object along with user client

Extends destroy to take an options to modify the destroy behavior.  Currently only the IOUSBHostObjectDestroyOptionsDeviceSurrender is defined to support surrendering ownersip of the kernel service.  To be used when accepting the kUSBHostMessageDeviceIsRequestingClose message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/destroy(options:))*