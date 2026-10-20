# forceTerminate()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Attempts to force the receiver to quit.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func forceTerminate() -> Bool
```

```objc
- (BOOL) forceTerminate;
```

#### Return Value

Returns [`true`](../../Swift/true.md) if the application successfully terminated, otherwise [`false`](../../Swift/false.md).

#### Discussion

This method will return [`false`](../../Swift/false.md) if the application is no longer running when the `forceTerminate` message is sent to the receiver.

This method may return before the receiver exits; you should observe the terminated property to determine when the application terminates.

Sandboxed applications can’t use this method to terminate other applciations. This method returns [`false`](../../Swift/false.md) when called from a sandboxed application.

## See Also

### Terminating applications
- [func terminate() -> Bool](./terminate%28%29.md)
  Attempts to quit the receiver normally.
- [var isTerminated: Bool](./isterminated.md)
  Indicates that the receiver’s application has terminated.
- [class func terminateAutomaticallyTerminableApplications()](./terminateautomaticallyterminableapplications%28%29.md)
  Terminates invisibly running applications as if triggered by system memory pressure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/forceterminate())*