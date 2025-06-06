# GetUID

**Framework**: AudioDriverKit  
**Kind**: method

Gets the unique identifier of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
OSSharedPtr<OSString> GetUID();
```

#### Return Value

A pointer to an [`OSString`](https://developer.apple.com/documentation/DriverKit/OSString) containing the UID.

#### Discussion

This method synchronizes by using the work queue created by the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getuid)*