# DISPATCH_PROC_FORK

**Framework**: Dispatch  
**Kind**: var  
**Role**: Global Variable

The process created one or more child processes.

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
var DISPATCH_PROC_FORK: Int32 { get }
```

```c
#define DISPATCH_PROC_FORK
```

## See Also

### Process Event Flags
- [var DISPATCH_PROC_EXEC: Int32](./dispatch_proc_exec.md)
  The process became another executable image.
- [var DISPATCH_PROC_EXIT: UInt32](./dispatch_proc_exit.md)
  The process has exited (perhaps cleanly, perhaps not).
- [var DISPATCH_PROC_SIGNAL: Int32](./dispatch_proc_signal.md)
  The process received a UNIX signal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_proc_fork)*