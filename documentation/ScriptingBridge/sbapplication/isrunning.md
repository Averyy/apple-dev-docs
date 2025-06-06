# isRunning

**Framework**: Scripting Bridge  
**Kind**: property

A Boolean that indicates whether the target application represented by the receiver is running.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var isRunning: Bool { get }
```

#### Discussion

[`true`](https://developer.apple.com/documentation/swift/true) if the application is running, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

This may be [`true`](https://developer.apple.com/documentation/swift/true) for instances initialized with a bundle identifier or URL because `SBApplication` launches the application only when it’s necessary to send it an event.

## See Also

- [func activate()](sbapplication/activate.md)
  Moves the target application to the foreground immediately.
- [var launchFlags: LSLaunchFlags](sbapplication/launchflags.md)
  The launch flags for the application represented by the receiver.
- [var sendMode: AESendMode](sbapplication/sendmode.md)
  The mode for sending Apple events to the target application.
- [var timeout: Int](sbapplication/timeout.md)
  The period the application will wait to receive reply Apple events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/isrunning)*