# DispatchSource.ProcessEvent

**Framework**: Dispatch  
**Kind**: struct  
**Role**: Structure

Events related to a process.

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
struct ProcessEvent
```

## Topics

### Process Event Flags
- [static let all: DispatchSource.ProcessEvent](./processevent/all.md)
  All process-related events.
- [static let exec: DispatchSource.ProcessEvent](./processevent/exec.md)
  The process became another executable image.
- [static let exit: DispatchSource.ProcessEvent](./processevent/exit.md)
  The process has exited (perhaps cleanly, perhaps not).
- [static let fork: DispatchSource.ProcessEvent](./processevent/fork.md)
  The process created one or more child processes.
- [static let signal: DispatchSource.ProcessEvent](./processevent/signal.md)
  The process received a UNIX signal.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Creating a Process Source
- [class func makeProcessSource(identifier: pid_t, eventMask: DispatchSource.ProcessEvent, queue: DispatchQueue?) -> any DispatchSourceProcess](./makeprocesssource%28identifier,eventmask,queue%29.md)
  Creates a new dispatch source object for monitoring the specified process.
- [protocol DispatchSourceProcess](../dispatchsourceprocess.md)
  A dispatch source that monitors an external process for events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/processevent)*