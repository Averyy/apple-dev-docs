# Open

**Framework**: HIDDriverKit  
**Kind**: method

Opens a session to the device and begins the delivery of input reports.

**Availability**:
- DriverKit 19.0+
- macOS ?+

## Declaration

```swift
kern_return_t Open(IOService * forClient, IOOptionBits options, OSAction * action);
```

#### Return Value

[`kIOReturnSuccess`](https://developer.apple.com/documentation/DriverKit/kIOReturnSuccess) on success, or another value if an error occurs. See [`Error Codes`](https://developer.apple.com/documentation/DriverKit/error-codes).

## Parameters

- `forClient`: The client that opened the interface.
- `options`: Options to use when opening the session. Specify   for no options.
- `action`: The   object that handles the asynchronous report callback. The action’s callback must conform to the   method.

## See Also

- [Close](iohidinterface/close.md)
  Closes the interface and stops the delivery of input reports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidinterface/open)*