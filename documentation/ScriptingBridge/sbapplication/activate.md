# activate()

**Framework**: Scripting Bridge  
**Kind**: method

Moves the target application to the foreground immediately.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.5+

## Declaration

```swift
func activate()
```

#### Discussion

If the target application is not already running, this method launches it.

## See Also

- [var isRunning: Bool](sbapplication/isrunning.md)
  A Boolean that indicates whether the target application represented by the receiver is running.
- [var launchFlags: LSLaunchFlags](sbapplication/launchflags.md)
  The launch flags for the application represented by the receiver.
- [var sendMode: AESendMode](sbapplication/sendmode.md)
  The mode for sending Apple events to the target application.
- [var timeout: Int](sbapplication/timeout.md)
  The period the application will wait to receive reply Apple events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scriptingbridge/sbapplication/activate())*