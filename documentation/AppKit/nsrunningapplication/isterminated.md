# isTerminated

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Indicates that the receiver’s application has terminated.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var isTerminated: Bool { get }
```

```objc
@property (readonly, getter=isTerminated) BOOL terminated;
```

#### Discussion

The value of terminated is [`true`](../../Swift/true.md) if the receiver’s application has terminated, otherwise [`false`](../../Swift/false.md).

This property is observable using key-value observing.

## See Also

### Terminating applications
- [func forceTerminate() -> Bool](./forceterminate%28%29.md)
  Attempts to force the receiver to quit.
- [func terminate() -> Bool](./terminate%28%29.md)
  Attempts to quit the receiver normally.
- [class func terminateAutomaticallyTerminableApplications()](./terminateautomaticallyterminableapplications%28%29.md)
  Terminates invisibly running applications as if triggered by system memory pressure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/isterminated)*