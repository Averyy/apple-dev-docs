# launchFlags

**Framework**: Scripting Bridge  
**Kind**: property  
**Role**: Instance Property

The launch flags for the application represented by the receiver.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var launchFlags: LSLaunchFlags { get set }
```

```objc
@property LSLaunchFlags launchFlags;
```

## Discussion

For more information, see [Launch Services](../../coreservices/launch_services.md).

## See Also

### Controlling the Application
- [func activate()](./activate%28%29.md)
  Moves the target application to the foreground immediately.
- [var isRunning: Bool](./isrunning.md)
  A Boolean that indicates whether the target application represented by the receiver is running.
- [var sendMode: AESendMode](./sendmode.md)
  The mode for sending Apple events to the target application.
- [var timeout: Int](./timeout.md)
  The period the application will wait to receive reply Apple events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/launchflags)*