# IOHIDCompletionAction

**Framework**: HIDDriverKit  
**Kind**: typealias

A function to call when a report operation completes.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
typedef void (*)(void *, void *, int, unsigned int) IOHIDCompletionAction;
```

## Parameters

- `target`: The target specified in the   struct.
- `parameter`: The parameter specified in the   struct.
- `status`: The completion status.

## See Also

- [IOHIDCompletion](iohidcompletion.md)
  A structure specifying the action to perform when a set/get report completes.
- [HIDReportCommandType](hidreportcommandtype.md)
  The type of the report command for a DriverKit driver.
- [HIDActionType](hidactiontype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidcompletionaction)*