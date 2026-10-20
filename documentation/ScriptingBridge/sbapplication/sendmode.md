# sendMode

**Framework**: Scripting Bridge  
**Kind**: property  
**Role**: Instance Property

The mode for sending Apple events to the target application.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var sendMode: AESendMode { get set }
```

```objc
@property AESendMode sendMode;
```

#### Discussion

For more information, see [Apple Event Manager](../../applicationservices/apple_event_manager.md).

The default send mode is [`kAEWaitReply`](../../coreservices/api-1542914-anonymous/kaewaitreply.md). If the send mode is something other than `kAEWaitReply`, the receiver might not correctly handle reply events from the target application.

## See Also

### Controlling the Application
- [func activate()](./activate%28%29.md)
  Moves the target application to the foreground immediately.
- [var isRunning: Bool](./isrunning.md)
  A Boolean that indicates whether the target application represented by the receiver is running.
- [var launchFlags: LSLaunchFlags](./launchflags.md)
  The launch flags for the application represented by the receiver.
- [var timeout: Int](./timeout.md)
  The period the application will wait to receive reply Apple events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/sendmode)*