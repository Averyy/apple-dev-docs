# renewExpiringResponseData(for:)

**Framework**: AVFoundation  
**Kind**: method

Tells the delegate that previously provided response data for a content key request is about to expire.

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
func renewExpiringResponseData(for contentKeyRequest: AVContentKeyRequest)
```

## Parameters

- `contentKeyRequest`: The content key request that’s about to expire.

## See Also

- [func expire()](avcontentkeysession/expire.md)
  Tells the delegate that the session expired as the result of normal, intentional processes.
- [func makeSecureTokenForExpirationDate(ofPersistableContentKey: Data, completionHandler: (Data?, (any Error)?) -> Void)](avcontentkeysession/makesecuretokenforexpirationdate(ofpersistablecontentkey:completionhandler:).md)
  Creates a secure server playback context that the client sends to the key server to get an expiration date for the given persistable content key data.
- [var contentProtectionSessionIdentifier: Data?](avcontentkeysession/contentprotectionsessionidentifier.md)
  The identifier for the current content protection session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/renewexpiringresponsedata(for:))*