# Aborted

**Framework**: DriverKit  
**Kind**: method

Calls the abort handler of the action object.

**Availability**:
- DriverKit ?+
- iOS ?+
- iPadOS ?+
- macOS ?+

## Declaration

```swift
void Aborted();
```

#### Discussion

Don’t call this method directly. The system calls it when no other objects reference the action object.

## See Also

- [Cancel](osaction/cancel.md)
  Cancels the execution of the action’s callbacks.
- [OSActionAbortedHandler](osactionabortedhandler.md)
  The block to call before aborting an action object.
- [OSActionCancelHandler](osactioncancelhandler.md)
  The block to call after the successful cancellation of the action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/driverkit/osaction/aborted)*