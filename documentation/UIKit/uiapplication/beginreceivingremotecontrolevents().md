# beginReceivingRemoteControlEvents()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the app to begin receiving remote-control events.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func beginReceivingRemoteControlEvents()
```

```objc
- (void) beginReceivingRemoteControlEvents;
```

## Discussion

In iOS 7.1 and later, use the shared [`MPRemoteCommandCenter`](../../MediaPlayer/mpremotecommandcenter.md) object to register for remote control events. You do not need to call this method when using the shared command center object.

This method starts the delivery of remote control events using the responder chain. Remote-control events originate as commands issued by headsets and external accessories that are intended to control multimedia presented by an app. To stop the reception of remote-control events, you must call [`endReceivingRemoteControlEvents()`](./endreceivingremotecontrolevents%28%29.md).

## See Also

### Receiving remote control events
- [func endReceivingRemoteControlEvents()](./endreceivingremotecontrolevents%28%29.md)
  Tells the app to stop receiving remote-control events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/beginreceivingremotecontrolevents())*