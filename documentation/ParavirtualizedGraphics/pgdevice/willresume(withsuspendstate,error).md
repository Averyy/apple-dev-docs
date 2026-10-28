# willResume(withSuspendState:error:)

**Framework**: Paravirtualized Graphics  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells a new device object to load a previously saved device’s suspend state.

**Availability**:
- Mac Catalyst 14.0+
- macOS 11.0+

## Declaration

```swift
func willResume(withSuspendState suspendState: Data, error: NSErrorPointer) -> Bool
```

```objc
- (bool) willResumeWithSuspendState:(NSData *) suspendState error:(NSError **) error;
```

## Return Value

A Boolean value that indicates whether the framework was able to start restoring the graphics data.

## Discussion

This method sets up the device to appear in the same state it was in before the suspend. The device object doesn’t access guest memory during the call to this method.

When resuming from an earlier suspended device, this must be the first method that you call on the newly created device object. When you call this method, ensure that the guest CPUs aren’t running.

After you call this method, reattach any suspended displays before calling [`didResume()`](./didresume%28%29.md).

## Parameters

- `suspendState`: The suspend data that you previously saved when you suspended an earlier device object.

## See Also

### Suspending and Resuming Graphics Processing
- [func willSuspend()](./willsuspend%28%29.md)
  Notifies the virtual graphics device to start suspending graphics activities.
- [func finishSuspend() -> Data?](./finishsuspend%28%29.md)
  Notifies the virtualized graphics device to finish suspending graphics activities.
- [func didResume()](./didresume%28%29.md)
  Tells the device object to finish any remaining work to resume processing of a previously saved device’s suspend state.
- [let PGResumeErrorDomain: String](../pgresumeerrordomain.md)
  The error domain for suspend-resume actions.
- [enum PGResumeErrorCode](../pgresumeerrorcode.md)
  Error codes for suspend-resume actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paravirtualizedgraphics/pgdevice/willresume(withsuspendstate:error:))*