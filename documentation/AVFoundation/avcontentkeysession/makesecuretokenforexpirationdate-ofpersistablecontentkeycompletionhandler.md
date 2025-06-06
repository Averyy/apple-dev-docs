# makeSecureTokenForExpirationDate(ofPersistableContentKey:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method

Creates a secure server playback context that the client sends to the key server to get an expiration date for the given persistable content key data.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func makeSecureTokenForExpirationDate(ofPersistableContentKey persistableContentKeyData: Data) async throws -> Data
```

## Parameters

- `persistableContentKeyData`: The previously created persistable content key data.
- `handler`: A block called after the secure token is ready.

## See Also

- [func expire()](avcontentkeysession/expire.md)
  Tells the delegate that the session expired as the result of normal, intentional processes.
- [func renewExpiringResponseData(for: AVContentKeyRequest)](avcontentkeysession/renewexpiringresponsedata(for:).md)
  Tells the delegate that previously provided response data for a content key request is about to expire.
- [var contentProtectionSessionIdentifier: Data?](avcontentkeysession/contentprotectionsessionidentifier.md)
  The identifier for the current content protection session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/makesecuretokenforexpirationdate(ofpersistablecontentkey:completionhandler:))*