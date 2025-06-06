# NFCWindowSceneDelegate

**Framework**: Core NFC  
**Kind**: protocol

A protocol to notify your app’s user interface about NFC-related events.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+

## Declaration

```swift
protocol NFCWindowSceneDelegate
```

#### Overview

When the device is eligible to receive NFC-related events, use this protocol to update your user interface. The received [`NFCWindowSceneEvent`](nfcwindowsceneevent.md) indicates whether the event represents the presence of a card reader or a gesture to initiate a contactless transaction by the person using the app.

You typically add conformance to this protocol in your app’s main scene delegate, where you already conform to [`UIWindowSceneDelegate`](https://developer.apple.com/documentation/UIKit/UIWindowSceneDelegate).

## Topics

### Handling events
- [func windowScene(UIWindowScene, didReceiveNFCWindowSceneEvent: NFCWindowSceneEvent)](nfcwindowscenedelegate/windowscene(_:didreceivenfcwindowsceneevent:).md)
  Informs your app that the system has received an NFC-related event.
- [enum NFCWindowSceneEvent](nfcwindowsceneevent.md)
  An NFC-related event that your app uses to update its user interface.

## See Also

- [enum NFCWindowSceneEvent](nfcwindowsceneevent.md)
  An NFC-related event that your app uses to update its user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcwindowscenedelegate)*