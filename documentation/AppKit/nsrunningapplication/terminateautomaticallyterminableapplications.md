# terminateAutomaticallyTerminableApplications()

**Framework**: AppKit  
**Kind**: method

Terminates invisibly running applications as if triggered by system memory pressure.

**Availability**:
- macOS 10.6+

## Declaration

```swift
class func terminateAutomaticallyTerminableApplications()
```

#### Discussion

This method is intended for installer applications and similar applications to ensure that nothing is unexpectedly relying on the files they’re replacing.

## See Also

- [func forceTerminate() -> Bool](nsrunningapplication/forceterminate.md)
  Attempts to force the receiver to quit.
- [func terminate() -> Bool](nsrunningapplication/terminate.md)
  Attempts to quit the receiver normally.
- [var isTerminated: Bool](nsrunningapplication/isterminated.md)
  Indicates that the receiver’s application has terminated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsrunningapplication/terminateautomaticallyterminableapplications())*