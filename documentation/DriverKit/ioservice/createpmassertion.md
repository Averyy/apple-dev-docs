# CreatePMAssertion

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t CreatePMAssertion(uint32_t assertionBits, uint64_t * assertionID, bool synced);
```

#### Return Value

kIOReturnSuccess on success. See IOReturn.h for error codes.

#### Discussion

Create a power management assertion.

## Parameters

- `assertionBits`: Bit masks including all the flavors that require to be asserted.
- `assertionID`: Pointer that will contain the unique identifier of the created   power assertion.
- `synced`: Indicates if the assertion must prevent an imminent sleep transition.   When set to true, and if a system sleep is irreversible, the call will return   kIOReturnBusy, in which case the assertion is not created. Only   kIOServicePMAssertionCPUBit is valid for assertionBits if sleepSafe is set to   true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/createpmassertion)*