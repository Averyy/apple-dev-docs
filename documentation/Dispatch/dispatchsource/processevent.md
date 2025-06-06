# DispatchSource.ProcessEvent

**Framework**: Dispatch  
**Kind**: struct

Events related to a process.

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
struct ProcessEvent
```

## Topics

### Process Event Flags
- [static let all: DispatchSource.ProcessEvent](dispatchsource/processevent/all.md)
  All process-related events.
- [static let exec: DispatchSource.ProcessEvent](dispatchsource/processevent/exec.md)
  The process became another executable image.
- [static let exit: DispatchSource.ProcessEvent](dispatchsource/processevent/exit.md)
  The process has exited (perhaps cleanly, perhaps not).
- [static let fork: DispatchSource.ProcessEvent](dispatchsource/processevent/fork.md)
  The process created one or more child processes.
- [static let signal: DispatchSource.ProcessEvent](dispatchsource/processevent/signal.md)
  The process received a UNIX signal.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [class func makeProcessSource(identifier: pid_t, eventMask: DispatchSource.ProcessEvent, queue: DispatchQueue?) -> any DispatchSourceProcess](dispatchsource/makeprocesssource(identifier:eventmask:queue:).md)
  Creates a new dispatch source object for monitoring the specified process.
- [protocol DispatchSourceProcess](dispatchsourceprocess.md)
  A dispatch source that monitors an external process for events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchsource/processevent)*