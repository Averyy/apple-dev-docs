# SetUsedLen

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
virtual kern_return_t SetUsedLen(uint32_t used_len);
```

#### Return Value

0 in case of success. Negative in case of an error.

#### Discussion

This function is called to set the used len of the buffer

## Parameters

- `used_len`: The length of the buffer used by the client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioextensiblepaniclog/setusedlen)*