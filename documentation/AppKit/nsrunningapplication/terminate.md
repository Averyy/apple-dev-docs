# terminate()

**Framework**: AppKit  
**Kind**: method

Attempts to quit the receiver normally.

**Availability**:
- macOS 10.6+

## Declaration

```swift
func terminate() -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if the request was successfully sent, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

#### Discussion

This method will return [`false`](https://developer.apple.com/documentation/Swift/false) if the application is no longer running when the terminate message is sent to the receiver.

This method may return before the receiver exits; you should observe the terminated property to determine when the application terminates.

Sandboxed applications can’t use this method to terminate other applications. This method returns [`false`](https://developer.apple.com/documentation/Swift/false) when called from a sandboxed application.

## See Also

- [func forceTerminate() -> Bool](nsrunningapplication/forceterminate.md)
  Attempts to force the receiver to quit.
- [var isTerminated: Bool](nsrunningapplication/isterminated.md)
  Indicates that the receiver’s application has terminated.
- [class func terminateAutomaticallyTerminableApplications()](nsrunningapplication/terminateautomaticallyterminableapplications.md)
  Terminates invisibly running applications as if triggered by system memory pressure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/terminate())*