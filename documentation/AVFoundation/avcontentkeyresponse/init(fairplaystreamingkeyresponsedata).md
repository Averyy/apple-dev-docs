# init(fairPlayStreamingKeyResponseData:)

**Framework**: AVFoundation  
**Kind**: init  
**Role**: Initializer

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

```objc
+ (instancetype) contentKeyResponseWithFairPlayStreamingKeyResponseData:(NSData *) keyResponseData;
```

#### Return Value

Returns a new [`AVContentKeyResponse`](../avcontentkeyresponse.md) object to decrypt content.

#### Discussion

Use the results of this initializer when the content key session creates a key request using the [`fairPlayStreaming`](../avcontentkeysystem/fairplaystreaming.md) parameter. The results are then passed to the [`processContentKeyResponse(_:)`](../avcontentkeyrequest/processcontentkeyresponse%28_%29.md) method to supply the decrypter with key data.

## Parameters

- `keyResponseData`: The key data from the FairPlay Streaming key server.

## See Also

### Creating new content key responses
- [convenience init(clearKeyData: Data, initializationVector: Data?)](./init%28clearkeydata,initializationvector%29.md)
  Creates a new key response object for key data and initialization vector sent in the clear.
- [convenience init(authorizationTokenData: Data)](./init%28authorizationtokendata%29.md)
  Creates a content key response with an authorization token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyresponse/init(fairplaystreamingkeyresponsedata:))*