# CallPlatformFunction

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
virtual kern_return_t CallPlatformFunction(OSString *functionName, bool waitForFunction, OSDictionary *inParam, OSDictionary **outParam);
```

#### Return Value

An IOReturn code; kIOReturnSuccess if the function was successfully executed, kIOReturnUnsupported if a service to execute the function could not be found. Other return codes may be returned by the function.

#### Discussion

Calls the platform function with the given name.

## Parameters

- `functionName`: Name of the function to be called.
- `waitForFunction`: If true, CallPlatformFunction will not return until the function has been called.
- `inParam`: Dictionary containing the input parameters.
- `outParam`: Pointer to a storage that will contain the output parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioservice/callplatformfunction)*