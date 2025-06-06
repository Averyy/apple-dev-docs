# timeout

**Framework**: Scripting Bridge  
**Kind**: property

The period the application will wait to receive reply Apple events.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var timeout: Int { get set }
```

#### Discussion

For more information, see [`Apple Event Manager`](https://developer.apple.com/documentation/applicationservices/apple_event_manager).

The default timeout value is [`kAEDefaultTimeout`](https://developer.apple.com/documentation/coreservices/1542814-timeout_constants/kaedefaulttimeout), which is about a minute. If you want the receiver to wait indefinitely for reply Apple events, use [`kNoTimeOut`](https://developer.apple.com/documentation/coreservices/1542814-timeout_constants/knotimeout). For more information, see [`Apple Event Manager`](https://developer.apple.com/documentation/applicationservices/apple_event_manager).

## See Also

- [func activate()](sbapplication/activate.md)
  Moves the target application to the foreground immediately.
- [var isRunning: Bool](sbapplication/isrunning.md)
  A Boolean that indicates whether the target application represented by the receiver is running.
- [var launchFlags: LSLaunchFlags](sbapplication/launchflags.md)
  The launch flags for the application represented by the receiver.
- [var sendMode: AESendMode](sbapplication/sendmode.md)
  The mode for sending Apple events to the target application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/timeout)*