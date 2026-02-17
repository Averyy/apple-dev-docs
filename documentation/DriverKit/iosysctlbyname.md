# IOSysCtlByName

**Framework**: DriverKit  
**Kind**: func

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t IOSysCtlByName(const char *name, void *oldp, size_t *oldlenp, void *newp, size_t newlen);
```

#### Return Value

kIOReturnSuccess if successful, or an IOReturn code indicating the error

#### Discussion

Get or set system information. Depending on the sysctl vector, only priviledged drivers might be able to set certain system information.

## Parameters

- `name`: An ASCII representation of the sysctl vector
- `oldp`: Buffer to receive the system information
- `oldlenp`: Length of the buffer receiving the system information
- `newp`: Buffer containing the value to be set
- `newlen`: Length of the buffer containing the value to be set


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/iosysctlbyname)*