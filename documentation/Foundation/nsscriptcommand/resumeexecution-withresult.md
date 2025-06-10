# resumeExecution(withResult:)

**Framework**: Foundation  
**Kind**: method

If a successful, unmatched, invocation of [`suspendExecution()`](nsscriptcommand/suspendexecution().md) has been made, resume the execution of the command.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func resumeExecution(withResult result: Any?)
```

#### Discussion

Resumes the execution of the command if a successful, unmatched, invocation of [`suspendExecution()`](nsscriptcommand/suspendexecution().md) has been made—otherwise, does nothing. The value for `result` is dependent on the segment of command execution that was suspended:

- If [`suspendExecution()`](nsscriptcommand/suspendexecution().md) was invoked from within a command handler of one of the command’s receivers, `result` is considered to be the return value of the handler. Unless the command has received a [`scriptErrorNumber`](nsscriptcommand/scripterrornumber.md) message with a nonzero error number, execution of the command will continue and the command handlers of other receivers will be invoked.
- If [`suspendExecution()`](nsscriptcommand/suspendexecution().md) was invoked from within an override of [`performDefaultImplementation()`](nsscriptcommand/performdefaultimplementation().md) the result is treated as if it were the return value of the invocation of [`performDefaultImplementation()`](nsscriptcommand/performdefaultimplementation().md).

[`resumeExecution(withResult:)`](nsscriptcommand/resumeexecution(withresult:).md) may be invoked in any thread, not just the one in which the corresponding invocation of [`suspendExecution()`](nsscriptcommand/suspendexecution().md) occurred.

> ❗ **Important**:  The script command handler that is being executed when [`suspendExecution()`](nsscriptcommand/suspendexecution().md) is invoked must return before you invoke [`resumeExecution(withResult:)`](nsscriptcommand/resumeexecution(withresult:).md). That is, it is not valid to suspend a command’s execution and then resume it immediately.

## See Also

- [func suspendExecution()](nsscriptcommand/suspendexecution.md)
  Suspends the execution of the receiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsscriptcommand/resumeexecution(withresult:))*