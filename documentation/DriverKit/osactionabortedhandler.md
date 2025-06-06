# OSActionAbortedHandler

**Framework**: DriverKit  
**Kind**: typealias

The block to call before aborting an action object.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
typedef void (^)(void) OSActionAbortedHandler;
```

## See Also

- [Cancel](osaction/cancel.md)
  Cancels the execution of the action’s callbacks.
- [Aborted](osaction/aborted.md)
  Calls the abort handler of the action object.
- [OSActionCancelHandler](osactioncancelhandler.md)
  The block to call after the successful cancellation of the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osactionabortedhandler)*