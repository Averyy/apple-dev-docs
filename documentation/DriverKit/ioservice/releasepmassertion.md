# ReleasePMAssertion

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t ReleasePMAssertion(uint64_t assertionID);
```

#### Return Value

kIOReturnSuccess on success. See IOReturn.h for error codes.

## Parameters

- `assertionID`: The assertion ID returned by CreatePMAssertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/releasepmassertion)*