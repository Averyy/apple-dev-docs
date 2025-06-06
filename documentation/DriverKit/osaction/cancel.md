# Cancel

**Framework**: DriverKit  
**Kind**: method

Cancels the execution of the action’s callbacks.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
kern_return_t Cancel(OSActionCancelHandlerhandler);
```

#### Return Value

[`kIOReturnSuccess`](kioreturnsuccess.md) on success, or another value if an error occurs. See [`Error Codes`](error-codes.md).

#### Discussion

After cancellation, you can only free the action object. You cannot reactivate it.

## Parameters

- `handler`: A handler block for the system to call after any in-flight callbacks finish executing.

## See Also

- [Aborted](osaction/aborted.md)
  Calls the abort handler of the action object.
- [OSActionAbortedHandler](osactionabortedhandler.md)
  The block to call before aborting an action object.
- [OSActionCancelHandler](osactioncancelhandler.md)
  The block to call after the successful cancellation of the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osaction/cancel)*