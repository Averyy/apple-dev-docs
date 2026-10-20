# exec

**Framework**: Dispatch  
**Kind**: property  
**Role**: Type Property

The process became another executable image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
static let exec: DispatchSource.ProcessEvent
```

#### Discussion

The process has become another executable image via an `exec` or `posix_spawn` function family call.

## See Also

### Process Event Flags
- [static let all: DispatchSource.ProcessEvent](./all.md)
  All process-related events.
- [static let exit: DispatchSource.ProcessEvent](./exit.md)
  The process has exited (perhaps cleanly, perhaps not).
- [static let fork: DispatchSource.ProcessEvent](./fork.md)
  The process created one or more child processes.
- [static let signal: DispatchSource.ProcessEvent](./signal.md)
  The process received a UNIX signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/processevent/exec)*