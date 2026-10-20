# setHardwareAssists

**Framework**: NetworkingDriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit 22.0+

## Declaration

```cpp
virtual IOReturn setHardwareAssists(uint32_t hardwareAssists, uint32_t hardwareAssistsMask);
```

#### Return Value

Returns kIOReturnSuccess on success, or an error otherwise.

#### Discussion

Set the stack requested hardware assists.

Driver should implement this function to be able to update itself with requested assists.

## Parameters

- `hardwareAssists`: The requested assists available to the stack.
- `hardwareAssistsMask`: The Specific assist that the driver should set..


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/sethardwareassists-3vpkr)*