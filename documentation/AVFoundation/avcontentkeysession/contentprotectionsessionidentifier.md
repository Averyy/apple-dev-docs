# contentProtectionSessionIdentifier

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The identifier for the current content protection session.

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
var contentProtectionSessionIdentifier: Data? { get }
```

```objc
@property (readonly, nullable) NSData * contentProtectionSessionIdentifier;
```

#### Discussion

The content protection session identifier is a unique string the session generates.

## See Also

### Managing expiration
- [func expire()](./expire%28%29.md)
  Tells the delegate that the session expired as the result of normal, intentional processes.
- [func makeSecureTokenForExpirationDate(ofPersistableContentKey: Data, completionHandler: (Data?, (any Error)?) -> Void)](./makesecuretokenforexpirationdate%28ofpersistablecontentkey,completionhandler%29.md)
  Creates a secure server playback context that the client sends to the key server to get an expiration date for the given persistable content key data.
- [func renewExpiringResponseData(for: AVContentKeyRequest)](./renewexpiringresponsedata%28for%29.md)
  Tells the delegate that previously provided response data for a content key request is about to expire.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeysession/contentprotectionsessionidentifier)*