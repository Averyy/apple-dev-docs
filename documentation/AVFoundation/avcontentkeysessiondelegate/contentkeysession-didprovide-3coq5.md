# contentKeySession(_:didProvide:)

**Framework**: AVFoundation  
**Kind**: method  
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

## Parameters

- `session`: The content key session that is providing the new content key request.
- `keyRequest`: The request for a new content key.

## See Also

- [func contentKeySession(AVContentKeySession, didProvideRenewingContentKeyRequest: AVContentKeyRequest)](avcontentkeysessiondelegate/contentkeysession(_:didproviderenewingcontentkeyrequest:).md)
  Provides the receiver with a new content key request object for the renewal of an existing content key.
- [func contentKeySession(AVContentKeySession, didProvide: AVPersistableContentKeyRequest)](avcontentkeysessiondelegate/contentkeysession(_:didprovide:)-2wdgz.md)
  Provides the receiver with a new content key request object to process a persistable content key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:didprovide:)-3coq5)*