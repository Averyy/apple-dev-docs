# init(authorizationTokenData:)

**Framework**: AVFoundation  
**Kind**: init

Creates a content key response with an authorization token.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
convenience init(authorizationTokenData: Data)
```

## Parameters

- `authorizationTokenData`: A data value that contains the authorization token.

## See Also

- [convenience init(clearKeyData: Data, initializationVector: Data?)](avcontentkeyresponse/init(clearkeydata:initializationvector:).md)
  Creates a new key response object for key data and initialization vector sent in the clear.
- [convenience init(fairPlayStreamingKeyResponseData: Data)](avcontentkeyresponse/init(fairplaystreamingkeyresponsedata:).md)
  Creates a content key response with an encrypted key response data blob when FairPlay Streaming is the key delivery method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyresponse/init(authorizationtokendata:))*