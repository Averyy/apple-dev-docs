# Open

**Framework**: HIDDriverKit  
**Kind**: method  
**Role**: Instance Method

Opens a session to the device and begins the delivery of input reports.

**Availability**:
- DriverKit 19.0+
- macOS

## Declaration

```cpp
virtual kern_return_t Open(IOService *forClient, IOOptionBits options, OSAction *action);
```

#### Return Value

[`kIOReturnSuccess`](../../DriverKit/kioreturnsuccess.md) on success, or another value if an error occurs. See [Error Codes](../../DriverKit/error-codes.md).

## Parameters

- `forClient`: The client that opened the interface.
- `options`: Options to use when opening the session. Specify `0` for no options.
- `action`: The `OSAction` object that handles the asynchronous report callback. The action’s callback must conform to the [`ReportAvailable`](./reportavailable.md) method.

## See Also

### Managing the Session
- [Close](./close.md)
  Closes the interface and stops the delivery of input reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidinterface/open)*