# PGResumeErrorDomain

**Framework**: Paravirtualized Graphics  
**Kind**: var  
**Role**: Global Variable

The error domain for suspend-resume actions.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
let PGResumeErrorDomain: String
```

```c
extern NSErrorDomain const PGResumeErrorDomain;
```

## See Also

### Suspending and Resuming Graphics Processing
- [func willSuspend()](./pgdevice/willsuspend%28%29.md)
  Notifies the virtual graphics device to start suspending graphics activities.
- [func finishSuspend() -> Data?](./pgdevice/finishsuspend%28%29.md)
  Notifies the virtualized graphics device to finish suspending graphics activities.
- [func willResume(withSuspendState: Data, error: NSErrorPointer) -> Bool](./pgdevice/willresume%28withsuspendstate,error%29.md)
  Tells a new device object to load a previously saved device’s suspend state.
- [func didResume()](./pgdevice/didresume%28%29.md)
  Tells the device object to finish any remaining work to resume processing of a previously saved device’s suspend state.
- [enum PGResumeErrorCode](./pgresumeerrorcode.md)
  Error codes for suspend-resume actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgresumeerrordomain)*