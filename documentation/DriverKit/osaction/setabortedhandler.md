# SetAbortedHandler

**Framework**: DriverKit  
**Kind**: method

Install a handler for the system to call when no other processes reference the action object.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t SetAbortedHandler(OSActionAbortedHandlerhandler);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

#### Discussion

The system calls your handler when no other objects reference the action object. If you want to keep the action object, use your handler to retain it. If you don’t retain the object, the system releases it shortly after your handler returns.

## Parameters

- `handler`: A handler block for the system to call. Specify   to remove the handler block from your action object.

## See Also

- [free](osaction/free.md)
  Performs any final cleanup for the action object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osaction/setabortedhandler)*