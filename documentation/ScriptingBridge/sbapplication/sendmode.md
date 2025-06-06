# sendMode

**Framework**: Scripting Bridge  
**Kind**: property

The mode for sending Apple events to the target application.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var sendMode: AESendMode { get set }
```

#### Discussion

For more information, see [`Apple Event Manager`](https://developer.apple.com/documentation/applicationservices/apple_event_manager).

The default send mode is [`kAEWaitReply`](https://developer.apple.com/documentation/coreservices/1542914-anonymous/kaewaitreply). If the send mode is something other than `kAEWaitReply`, the receiver might not correctly handle reply events from the target application.

## See Also

- [func activate()](sbapplication/activate.md)
  Moves the target application to the foreground immediately.
- [var isRunning: Bool](sbapplication/isrunning.md)
  A Boolean that indicates whether the target application represented by the receiver is running.
- [var launchFlags: LSLaunchFlags](sbapplication/launchflags.md)
  The launch flags for the application represented by the receiver.
- [var timeout: Int](sbapplication/timeout.md)
  The period the application will wait to receive reply Apple events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/sendmode)*