# contentKeySession(_:didProvide:)

**Framework**: AVFoundation  
**Kind**: method

Provides the receiver with a new content key request object to process a persistable content key.

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
optional func contentKeySession(_ session: AVContentKeySession, didProvide keyRequest: AVPersistableContentKeyRequest)
```

## Parameters

- `session`: The content key session that is providing the new persistable content key request.
- `keyRequest`: The request for a new persistable content key.

## See Also

- [func contentKeySession(AVContentKeySession, didProvide: AVContentKeyRequest)](avcontentkeysessiondelegate/contentkeysession(_:didprovide:)-3coq5.md)
  Provides the receiver with a new content key request object.
- [func contentKeySession(AVContentKeySession, didProvideRenewingContentKeyRequest: AVContentKeyRequest)](avcontentkeysessiondelegate/contentkeysession(_:didproviderenewingcontentkeyrequest:).md)
  Provides the receiver with a new content key request object for the renewal of an existing content key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysessiondelegate/contentkeysession(_:didprovide:)-2wdgz)*