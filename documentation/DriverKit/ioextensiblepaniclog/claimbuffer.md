# ClaimBuffer

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
virtual kern_return_t ClaimBuffer(uint64_t *addr, uint64_t *len);
```

#### Return Value

0 in case of success. Negative in case of an error.

#### Discussion

This function is called to get a pointer to the ext paniclog buffer

After this function is called, the user is responsible for copying data into the buffer. The entire buffer is copied when a system panics. After claiming the buffer, YieldBuffer() has to be called to set the used_len of the buffer before calling InsertData() or AppendData()

## Parameters

- `addr`: Address of the mapped buffer
- `len`: The length of the mapped buffer. This is same value as the max_len in the Create() function


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioextensiblepaniclog/claimbuffer)*