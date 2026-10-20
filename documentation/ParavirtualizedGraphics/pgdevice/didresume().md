# didResume()

**Framework**: Paravirtualized Graphics  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the device object to finish any remaining work to resume processing of a previously saved device’s suspend state.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
func didResume()
```

```objc
- (void) didResume;
```

#### Discussion

After you call this method, the virtualized device can generate new interrupts immediately, even before the call completes. Similarly, guest memory must also be accessible before you call this method.

## See Also

### Suspending and Resuming Graphics Processing
- [func willSuspend()](./willsuspend%28%29.md)
  Notifies the virtual graphics device to start suspending graphics activities.
- [func finishSuspend() -> Data?](./finishsuspend%28%29.md)
  Notifies the virtualized graphics device to finish suspending graphics activities.
- [func willResume(withSuspendState: Data, error: NSErrorPointer) -> Bool](./willresume%28withsuspendstate,error%29.md)
  Tells a new device object to load a previously saved device’s suspend state.
- [let PGResumeErrorDomain: String](../pgresumeerrordomain.md)
  The error domain for suspend-resume actions.
- [enum PGResumeErrorCode](../pgresumeerrorcode.md)
  Error codes for suspend-resume actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevice/didresume())*