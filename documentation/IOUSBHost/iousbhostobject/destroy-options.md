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

```None
         <code>IOUSBHostObjectDestroyOptionsDeviceSurrender</code> is defined to support surrendering ownersip of
         the kernel service.  To be used when accepting the <code>kUSBHostMessageDeviceIsRequestingClose</code> message.
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostobject/destroy(options:))*