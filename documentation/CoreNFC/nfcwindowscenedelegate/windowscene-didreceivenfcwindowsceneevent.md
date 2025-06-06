# windowScene(_:didReceiveNFCWindowSceneEvent:)

**Framework**: Core NFC  
**Kind**: method  
**Required**: Yes

Informs your app that the system has received an NFC-related event.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst ?+

## Declaration

```swift
func windowScene(_ windowScene: UIWindowScene, didReceiveNFCWindowSceneEvent event: NFCWindowSceneEvent)
```

## Parameters

- `windowScene`: A scene in your app that handles the event.
- `event`: The NFC-related event that triggered the delegate callback.

## See Also

- [enum NFCWindowSceneEvent](nfcwindowsceneevent.md)
  An NFC-related event that your app uses to update its user interface.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcwindowscenedelegate/windowscene(_:didreceivenfcwindowsceneevent:))*