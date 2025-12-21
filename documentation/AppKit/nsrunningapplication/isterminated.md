# isTerminated

**Framework**: AppKit  
**Kind**: property

Indicates that the receiver’s application has terminated.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var isTerminated: Bool { get }
```

#### Discussion

The value of terminated is [`true`](https://developer.apple.com/documentation/Swift/true) if the receiver’s application has terminated, otherwise [`false`](https://developer.apple.com/documentation/Swift/false).

This property is observable using key-value observing.

## See Also

- [func forceTerminate() -> Bool](nsrunningapplication/forceterminate.md)
  Attempts to force the receiver to quit.
- [func terminate() -> Bool](nsrunningapplication/terminate.md)
  Attempts to quit the receiver normally.
- [class func terminateAutomaticallyTerminableApplications()](nsrunningapplication/terminateautomaticallyterminableapplications.md)
  Terminates invisibly running applications as if triggered by system memory pressure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/isterminated)*