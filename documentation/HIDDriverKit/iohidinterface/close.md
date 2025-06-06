# Close

**Framework**: HIDDriverKit  
**Kind**: method

Closes the interface and stops the delivery of input reports.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t Close(IOService * forClient, IOOptionBits options);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `forClient`: The client that closed the interface.
- `options`: Options to use when closing the session. Specify   for no options.

## See Also

- [Open](iohidinterface/open.md)
  Opens a session to the device and begins the delivery of input reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidinterface/close)*