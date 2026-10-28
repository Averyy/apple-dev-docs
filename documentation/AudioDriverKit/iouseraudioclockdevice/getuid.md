# GetUID

**Framework**: AudioDriverKit  
**Kind**: method  
**Role**: Instance Method

Gets the unique identifier of the clock device.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
OSSharedPtr<OSString> GetUID();
```

## Return Value

A pointer to an [`OSString`](../../DriverKit/osstring.md) containing the UID.

## Discussion

This method synchronizes by using the work queue created by the object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/iouseraudioclockdevice/getuid)*