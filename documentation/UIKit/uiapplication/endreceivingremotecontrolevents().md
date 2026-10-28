# endReceivingRemoteControlEvents()

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Tells the app to stop receiving remote-control events.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func endReceivingRemoteControlEvents()
```

```objc
- (void) endReceivingRemoteControlEvents;
```

## Discussion

In iOS 7.1 and later, use the shared [`MPRemoteCommandCenter`](../../MediaPlayer/mpremotecommandcenter.md) object to unregister for remote control events. You do not need to call this method when using the shared command center object.

This method stops the delivery of remote control events using the responder chain. Remote-control events originate as commands issued by headsets and external accessories that are intended to control multimedia presented by an app.

## See Also

### Receiving remote control events
- [func beginReceivingRemoteControlEvents()](./beginreceivingremotecontrolevents%28%29.md)
  Tells the app to begin receiving remote-control events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/endreceivingremotecontrolevents())*