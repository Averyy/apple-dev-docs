# ReleasePMAssertion

**Framework**: DriverKit  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```cpp
virtual kern_return_t ReleasePMAssertion(uint64_t assertionID);
```

## Return Value

kIOReturnSuccess on success. See IOReturn.h for error codes.

## Discussion

Release a previously created power management assertion.

## Parameters

- `assertionID`: The assertion ID returned by CreatePMAssertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/releasepmassertion)*