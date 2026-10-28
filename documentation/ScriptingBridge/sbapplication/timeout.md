# timeout

**Framework**: Scripting Bridge  
**Kind**: property  
**Role**: Instance Property

The period the application will wait to receive reply Apple events.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var timeout: Int { get set }
```

```objc
@property long timeout;
```

## Discussion

For more information, see [Apple Event Manager](../../applicationservices/apple_event_manager.md).

The default timeout value is [`kAEDefaultTimeout`](../../coreservices/api-1542814-timeout_constants/kaedefaulttimeout.md), which is about a minute. If you want the receiver to wait indefinitely for reply Apple events, use [`kNoTimeOut`](../../coreservices/api-1542814-timeout_constants/knotimeout.md). For more information, see [Apple Event Manager](../../applicationservices/apple_event_manager.md).

## See Also

### Controlling the Application
- [func activate()](./activate%28%29.md)
  Moves the target application to the foreground immediately.
- [var isRunning: Bool](./isrunning.md)
  A Boolean that indicates whether the target application represented by the receiver is running.
- [var launchFlags: LSLaunchFlags](./launchflags.md)
  The launch flags for the application represented by the receiver.
- [var sendMode: AESendMode](./sendmode.md)
  The mode for sending Apple events to the target application.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/timeout)*