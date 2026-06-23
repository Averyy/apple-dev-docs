# YieldBuffer

**Framework**: DriverKit  
**Kind**: method

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
virtual kern_return_t YieldBuffer(uint32_t used_len);
```

#### Return Value

0 in case of success. Negative in case of an error.

#### Discussion

This function is called to yield the buffer and set the used_len for the buffer

After this function call, InsertData() and AppendData() can be called.

## Parameters

- `used_len`: The length of the buffer used by the client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/ioextensiblepaniclog/yieldbuffer)*