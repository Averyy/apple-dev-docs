# exit

**Framework**: Dispatch  
**Kind**: property

The process has exited (perhaps cleanly, perhaps not).

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
static let exit: DispatchSource.ProcessEvent
```

## See Also

- [static let all: DispatchSource.ProcessEvent](dispatchsource/processevent/all.md)
  All process-related events.
- [static let exec: DispatchSource.ProcessEvent](dispatchsource/processevent/exec.md)
  The process became another executable image.
- [static let fork: DispatchSource.ProcessEvent](dispatchsource/processevent/fork.md)
  The process created one or more child processes.
- [static let signal: DispatchSource.ProcessEvent](dispatchsource/processevent/signal.md)
  The process received a UNIX signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/processevent/exit)*