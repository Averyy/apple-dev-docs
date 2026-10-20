# respondByRequestingPersistableContentKeyRequestAndReturnError()

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Tells the receiver that the app requires a persistable content key request object for processing.

**Availability**:
- iOS 11.2+
- iPadOS 11.2+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

*iOS, iPadOS, Mac Catalyst*

```swift
func respondByRequestingPersistableContentKeyRequestAndReturnError() throws
```

*macOS, tvOS, visionOS, watchOS*

```swift
func respondByRequestingPersistableContentKeyRequest() throws
```

```objc
- (BOOL) respondByRequestingPersistableContentKeyRequestAndReturnError:(NSError **) outError;
```

#### Discussion

To create a key that persists across multiple playback sessions, use this method to request an [`AVPersistableContentKeyRequest`](../avpersistablecontentkeyrequest.md) object. If the underlying protocol supports persistable content keys, the delegate receives a persistable content key request via the [`contentKeySession(_:didProvide:)`](../avcontentkeysessiondelegate/contentkeysession%28_,didprovide%29-2wdgz.md) method. An [`internalInconsistencyException`](../../Foundation/nsexceptionname/internalinconsistencyexception.md) is returned if your delegate does not respond to [`contentKeySession(_:didProvide:)`](../avcontentkeysessiondelegate/contentkeysession%28_,didprovide%29-2wdgz.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/respondbyrequestingpersistablecontentkeyrequestandreturnerror())*