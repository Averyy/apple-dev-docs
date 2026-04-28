# respondByRequestingPersistableContentKeyRequest()

**Framework**: AVFoundation  
**Kind**: method

Tells the receiver that the app requires a persistable content key request object for processing.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+

## Declaration

```swift
func respondByRequestingPersistableContentKeyRequest()
```

#### Discussion

To create a key that persists across multiple playback sessions, use this method to request an [`AVPersistableContentKeyRequest`](avpersistablecontentkeyrequest.md) object. If the underlying protocol supports persistable content keys, the delegate receives a persistable content key request via the [`contentKeySession(_:didProvide:)`](avcontentkeysessiondelegate/contentkeysession(_:didprovide:)-2wdgz.md) method. An [`internalInconsistencyException`](https://developer.apple.com/documentation/Foundation/NSExceptionName/internalInconsistencyException) is returned if your delegate does not respond to [`contentKeySession(_:didProvide:)`](avcontentkeysessiondelegate/contentkeysession(_:didprovide:)-2wdgz.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequest()-1ci4q)*