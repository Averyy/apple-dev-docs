# IOHIDCompletion

**Framework**: HIDDriverKit  
**Kind**: struct

A structure specifying the action to perform when a set/get report completes.

**Availability**:
- DriverKit ?+
- macOS ?+

## Declaration

```swift
typedef struct IOHIDCompletion { ... } IOHIDCompletion;
```

## Topics

### Getting the Completion Handler Properties
- [target](iohidcompletion/target.md)
  The target to pass to the action function.
- [action](iohidcompletion/action.md)
  The function to call.
- [parameter](iohidcompletion/parameter.md)
  The parameter to pass to the action function.

## See Also

- [IOHIDCompletionAction](iohidcompletionaction.md)
  A function to call when a report operation completes.
- [HIDReportCommandType](hidreportcommandtype.md)
  The type of the report command for a DriverKit driver.
- [HIDActionType](hidactiontype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/hiddriverkit/iohidcompletion)*