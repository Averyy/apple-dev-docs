# launchFlags

**Framework**: Scripting Bridge  
**Kind**: property

The launch flags for the application represented by the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var launchFlags: LSLaunchFlags { get set }
```

#### Discussion

For more information, see [`Launch Services`](https://developer.apple.com/documentation/coreservices/launch_services).

## See Also

- [func activate()](sbapplication/activate.md)
  Moves the target application to the foreground immediately.
- [var isRunning: Bool](sbapplication/isrunning.md)
  A Boolean that indicates whether the target application represented by the receiver is running.
- [var sendMode: AESendMode](sbapplication/sendmode.md)
  The mode for sending Apple events to the target application.
- [var timeout: Int](sbapplication/timeout.md)
  The period the application will wait to receive reply Apple events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/launchflags)*