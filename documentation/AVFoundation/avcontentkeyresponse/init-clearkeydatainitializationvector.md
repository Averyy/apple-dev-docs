# init(clearKeyData:initializationVector:)

**Framework**: AVFoundation  
**Kind**: init

Creates a new key response object for key data and initialization vector sent in the clear.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
convenience init(clearKeyData keyData: Data, initializationVector: Data?)
```

#### Return Value

Returns a new [`AVContentKeyResponse`](avcontentkeyresponse.md) object to decrypt content.

#### Discussion

Use the results of this initializer when the content key session creates a key request using the [`clearKey`](avcontentkeysystem/clearkey.md) parameter. The results are then passed to the [`processContentKeyResponse(_:)`](avcontentkeyrequest/processcontentkeyresponse(_:).md) method to supply the decrypter with key data.

## Parameters

- `keyData`: The key used for decrypting content.
- `initializationVector`: The initialization vector used for decrypting content. This value is   when the initialization vector is contained in the media to be decrypted.

## See Also

- [convenience init(fairPlayStreamingKeyResponseData: Data)](avcontentkeyresponse/init(fairplaystreamingkeyresponsedata:).md)
  Creates a content key response with an encrypted key response data blob when FairPlay Streaming is the key delivery method.
- [convenience init(authorizationTokenData: Data)](avcontentkeyresponse/init(authorizationtokendata:).md)
  Creates a content key response with an authorization token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyresponse/init(clearkeydata:initializationvector:))*