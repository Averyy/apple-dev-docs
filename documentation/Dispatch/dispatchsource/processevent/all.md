# all

**Framework**: Dispatch  
**Kind**: property  
**Role**: Type Property

All process-related events.

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
static let all: DispatchSource.ProcessEvent
```

## See Also

### Process Event Flags
- [static let exec: DispatchSource.ProcessEvent](./exec.md)
  The process became another executable image.
- [static let exit: DispatchSource.ProcessEvent](./exit.md)
  The process has exited (perhaps cleanly, perhaps not).
- [static let fork: DispatchSource.ProcessEvent](./fork.md)
  The process created one or more child processes.
- [static let signal: DispatchSource.ProcessEvent](./signal.md)
  The process received a UNIX signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/processevent/all)*