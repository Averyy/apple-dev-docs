# finishSuspend()

**Framework**: Paravirtualized Graphics  
**Kind**: method  
**Required**: Yes

Notifies the virtualized graphics device to finish suspending graphics activities.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
func finishSuspend() -> Data?
```

#### Return Value

The suspend state data, or `nil` if an error occurred.

#### Discussion

This method may take an arbitrary amount of time as the device needs to complete any unfinished GPU work. After this call completes, you can’t perform any further operations on this device object and must release it.

Typically, your app serializes the suspend state data to persistant storage. Pass the suspend state data to a new device object when you want to resume graphics operations.

## See Also

- [func willSuspend()](pgdevice/willsuspend.md)
  Notifies the virtual graphics device to start suspending graphics activities.
- [func willResume(withSuspendState: Data, error: NSErrorPointer) -> Bool](pgdevice/willresume(withsuspendstate:error:).md)
  Tells a new device object to load a previously saved device’s suspend state.
- [func didResume()](pgdevice/didresume.md)
  Tells the device object to finish any remaining work to resume processing of a previously saved device’s suspend state.
- [let PGResumeErrorDomain: String](pgresumeerrordomain.md)
  The error domain for suspend-resume actions.
- [enum PGResumeErrorCode](pgresumeerrorcode.md)
  Error codes for suspend-resume actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevice/finishsuspend())*