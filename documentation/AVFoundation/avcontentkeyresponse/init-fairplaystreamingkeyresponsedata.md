# init(fairPlayStreamingKeyResponseData:)

**Framework**: AVFoundation  
**Kind**: init

Creates a content key response with an encrypted key response data blob when FairPlay Streaming is the key delivery method.

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
convenience init(fairPlayStreamingKeyResponseData keyResponseData: Data)
```

#### Return Value

Returns a new [`AVContentKeyResponse`](avcontentkeyresponse.md) object to decrypt content.

#### Discussion

Use the results of this initializer when the content key session creates a key request using the [`fairPlayStreaming`](avcontentkeysystem/fairplaystreaming.md) parameter. The results are then passed to the [`processContentKeyResponse(_:)`](avcontentkeyrequest/processcontentkeyresponse(_:).md) method to supply the decrypter with key data.

## Parameters

- `keyResponseData`: The key data from the FairPlay Streaming key server.

## See Also

- [convenience init(clearKeyData: Data, initializationVector: Data?)](avcontentkeyresponse/init(clearkeydata:initializationvector:).md)
  Creates a new key response object for key data and initialization vector sent in the clear.
- [convenience init(authorizationTokenData: Data)](avcontentkeyresponse/init(authorizationtokendata:).md)
  Creates a content key response with an authorization token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyresponse/init(fairplaystreamingkeyresponsedata:))*