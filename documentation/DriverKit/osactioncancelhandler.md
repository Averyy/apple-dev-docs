# OSActionCancelHandler

**Framework**: DriverKit  
**Kind**: typealias  
**Role**: Type Alias

The block to call after the successful cancellation of the action.

**Availability**:
- DriverKit
- iOS
- iPadOS
- macOS

## Declaration

```c
typedef void (^)(void) OSActionCancelHandler;
```

## See Also

### Ending the Action Early
- [Cancel](./osaction/cancel.md)
  Cancels the execution of the action’s callbacks.
- [Aborted](./osaction/aborted.md)
  Calls the abort handler of the action object.
- [OSActionAbortedHandler](./osactionabortedhandler.md)
  The block to call before aborting an action object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osactioncancelhandler)*