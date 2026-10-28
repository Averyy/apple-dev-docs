# originatingRecipient

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

The AVContentKeyRecipient which initiated this request, if any.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
weak var originatingRecipient: (any AVContentKeyRecipient)? { get }
```

```objc
@property (weak, readonly, nullable) id<AVContentKeyRecipient> originatingRecipient;
```

## Discussion

The originatingRecipient is an AVFoundation object responsible for initiating an AVContentKeyRequest. For example, an AVURLAsset used for playback can trigger an AVContentKeyRequest.

If an application triggers key loading directly, for example with -[AVContentKeySession processContentKeyRequestWithIdentifier:initializationData:options:], the value of originatingRecipient will be nil.

The originatingRecipient of key requests from HLS interstitials will always be the corresponding interstitial AVURLAsset. To receive key requests for DRM-protected interstitial content, applications must ensure their AVContentKeySession is attached to these interstitial AVURLAssets.

These interstitial AVURLAssets may be retrieved from the primary AVURLAsset via AVPlayerInterstitialEventMonitor.

## See Also

### Getting content key request properties
- [var identifier: (any Sendable)?](./identifier.md)
  The identifier for the content key.
- [var canProvidePersistableContentKey: Bool](./canprovidepersistablecontentkey.md)
  The content key request used to create a persistable content key or respond to a previous request with a persistable content key.
- [var error: (any Error)?](./error.md)
  The error description for a failed key request.
- [var initializationData: Data?](./initializationdata.md)
  The data used to obtain a key response.
- [var renewsExpiringResponseData: Bool](./renewsexpiringresponsedata.md)
  A Boolean value that indicates whether the content key request renews previously provided response data.
- [var status: AVContentKeyRequest.Status](./status-swift.property.md)
  The current state of the content key request.
- [AVContentKeyRequest.Status](./status-swift.enum.md)
  The status for a content key request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/originatingrecipient)*