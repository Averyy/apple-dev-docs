# makeSecureTokenForExpirationDate(ofPersistableContentKey:completionHandler:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

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
func makeSecureTokenForExpirationDate(ofPersistableContentKey persistableContentKeyData: Data, completionHandler handler: @escaping @Sendable (Data?, (any Error)?) -> Void)
```

```swift
func makeSecureTokenForExpirationDate(ofPersistableContentKey persistableContentKeyData: Data) async throws -> Data
```

```objc
- (void) makeSecureTokenForExpirationDateOfPersistableContentKey:(NSData *) persistableContentKeyData completionHandler:(void (^)(NSData *secureTokenData, NSError *error)) handler;
```

## Parameters

- `persistableContentKeyData`: The previously created persistable content key data.
- `handler`: A block called after the secure token is ready.

  - **secureTokenData**: The new secure token.
  - **error**: A parameter that holds the error object that explains the error. If no error occurred, the value of this parameter is `nil`.

## See Also

### Managing expiration
- [func expire()](./expire%28%29.md)
  Tells the delegate that the session expired as the result of normal, intentional processes.
- [func renewExpiringResponseData(for: AVContentKeyRequest)](./renewexpiringresponsedata%28for%29.md)
  Tells the delegate that previously provided response data for a content key request is about to expire.
- [var contentProtectionSessionIdentifier: Data?](./contentprotectionsessionidentifier.md)
  The identifier for the current content protection session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/makesecuretokenforexpirationdate(ofpersistablecontentkey:completionhandler:))*