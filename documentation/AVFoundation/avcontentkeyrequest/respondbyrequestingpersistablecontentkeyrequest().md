# respondByRequestingPersistableContentKeyRequest()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the receiver that the app requires a persistable content key request object for processing.

**Availability**:
- iOS 10.3+ - Deprecated in 11.2
- iPadOS 10.3+ - Deprecated in 11.2
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`respondByRequestingPersistableContentKeyRequestAndReturnError()`](./respondbyrequestingpersistablecontentkeyrequestandreturnerror%28%29.md).

## Declaration

```swift
func respondByRequestingPersistableContentKeyRequest()
```

```objc
- (void) respondByRequestingPersistableContentKeyRequest;
```

## Discussion

To create a key that persists across multiple playback sessions, use this method to request an [`AVPersistableContentKeyRequest`](../avpersistablecontentkeyrequest.md) object. If the underlying protocol supports persistable content keys, the delegate receives a persistable content key request via the [`contentKeySession(_:didProvide:)`](../avcontentkeysessiondelegate/contentkeysession%28_,didprovide%29-2wdgz.md) method. An [`internalInconsistencyException`](../../Foundation/nsexceptionname/internalinconsistencyexception.md) is returned if your delegate does not respond to [`contentKeySession(_:didProvide:)`](../avcontentkeysessiondelegate/contentkeysession%28_,didprovide%29-2wdgz.md).

## See Also

### Responding to the content key request
- [func processContentKeyResponse(AVContentKeyResponse)](./processcontentkeyresponse%28_%29.md)
  Sends the specified content key response to the receiver for processing.
- [func processContentKeyResponseError(any Error)](./processcontentkeyresponseerror%28_%29.md)
  Tells the receiver that the app was unable to obtain a content key response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequest())*