# fork

**Framework**: Dispatch  
**Kind**: property

The process created one or more child processes.

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
static let fork: DispatchSource.ProcessEvent
```

## See Also

- [static let all: DispatchSource.ProcessEvent](dispatchsource/processevent/all.md)
  All process-related events.
- [static let exec: DispatchSource.ProcessEvent](dispatchsource/processevent/exec.md)
  The process became another executable image.
- [static let exit: DispatchSource.ProcessEvent](dispatchsource/processevent/exit.md)
  The process has exited (perhaps cleanly, perhaps not).
- [static let signal: DispatchSource.ProcessEvent](dispatchsource/processevent/signal.md)
  The process received a UNIX signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/processevent/fork)*