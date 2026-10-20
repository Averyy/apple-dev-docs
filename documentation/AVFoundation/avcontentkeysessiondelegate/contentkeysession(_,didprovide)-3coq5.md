# contentKeySession(_:didProvide:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Provides the receiver with a new content key request object.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- macOS 10.12.4+
- tvOS 10.2+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func contentKeySession(_ session: AVContentKeySession, didProvide keyRequest: AVContentKeyRequest)
```

```objc
- (void) contentKeySession:(AVContentKeySession *) session didProvideContentKeyRequest:(AVContentKeyRequest *) keyRequest;
```

## Parameters

- `session`: The content key session that is providing the new content key request.
- `keyRequest`: The request for a new content key.

## See Also

### Providing new content key requests
- [func contentKeySession(AVContentKeySession, didProvideRenewingContentKeyRequest: AVContentKeyRequest)](./contentkeysession%28_,didproviderenewingcontentkeyrequest%29.md)
  Provides the receiver with a new content key request object for the renewal of an existing content key.
- [func contentKeySession(AVContentKeySession, didProvide: AVPersistableContentKeyRequest)](./contentkeysession%28_,didprovide%29-2wdgz.md)
  Provides the receiver with a new content key request object to process a persistable content key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:didprovide:)-3coq5)*