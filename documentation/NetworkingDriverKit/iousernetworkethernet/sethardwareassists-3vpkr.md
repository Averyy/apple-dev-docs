# setHardwareAssists

**Framework**: NetworkingDriverKit  
**Kind**: method

**Availability**:
- DriverKit 22.0+

## Declaration

```swift
IOReturn setHardwareAssists(uint32_t hardwareAssists, uint32_t hardwareAssistsMask);
```

#### Return Value

Returns kIOReturnSuccess on success, or an error otherwise.

#### Discussion

Driver should implement this function to be able to update itself with requested assists.

## Parameters

- `hardwareAssists`: The requested assists available to the stack.
- `hardwareAssistsMask`: The Specific assist that the driver should set..


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkingdriverkit/iousernetworkethernet/sethardwareassists-3vpkr)*