# isRunning

**Framework**: Scripting Bridge  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether the target application represented by the receiver is running.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
var isRunning: Bool { get }
```

```objc
@property (readonly, getter=isRunning) BOOL running;
```

#### Discussion

[`true`](../../Swift/true.md) if the application is running, [`false`](../../Swift/false.md) otherwise.

This may be [`true`](../../Swift/true.md) for instances initialized with a bundle identifier or URL because `SBApplication` launches the application only when it’s necessary to send it an event.

## See Also

### Controlling the Application
- [func activate()](./activate%28%29.md)
  Moves the target application to the foreground immediately.
- [var launchFlags: LSLaunchFlags](./launchflags.md)
  The launch flags for the application represented by the receiver.
- [var sendMode: AESendMode](./sendmode.md)
  The mode for sending Apple events to the target application.
- [var timeout: Int](./timeout.md)
  The period the application will wait to receive reply Apple events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/isrunning)*