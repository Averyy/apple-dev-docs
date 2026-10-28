# Close

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Closes the interface and stops the delivery of input reports.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual kern_return_t Close(IOService *forClient, IOOptionBits options);
```

## Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `forClient`: The client that closed the interface.
- `options`: Options to use when closing the session. Specify `0` for no options.

## See Also

### Managing the Session
- [Open](./open.md)
  Opens a session to the device and begins the delivery of input reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidinterface/close)*