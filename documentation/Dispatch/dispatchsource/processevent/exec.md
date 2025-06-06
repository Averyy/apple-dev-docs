# exec

**Framework**: Dispatch  
**Kind**: property

The process became another executable image.

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
static let exec: DispatchSource.ProcessEvent
```

#### Discussion

The process has become another executable image via an `exec` or `posix_spawn` function family call.

## See Also

- [static let all: DispatchSource.ProcessEvent](dispatchsource/processevent/all.md)
  All process-related events.
- [static let exit: DispatchSource.ProcessEvent](dispatchsource/processevent/exit.md)
  The process has exited (perhaps cleanly, perhaps not).
- [static let fork: DispatchSource.ProcessEvent](dispatchsource/processevent/fork.md)
  The process created one or more child processes.
- [static let signal: DispatchSource.ProcessEvent](dispatchsource/processevent/signal.md)
  The process received a UNIX signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/processevent/exec)*