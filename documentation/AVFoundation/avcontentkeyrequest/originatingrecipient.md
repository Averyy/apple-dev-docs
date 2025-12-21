# originatingRecipient

**Framework**: AVFoundation  
**Kind**: property

The AVContentKeyRecipient which initiated this request, if any.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
weak var originatingRecipient: (any AVContentKeyRecipient)? { get }
```

#### Discussion

The originatingRecipient is an AVFoundation object responsible for initiating an AVContentKeyRequest. For example, an AVURLAsset used for playback can trigger an AVContentKeyRequest.

If an application triggers key loading directly, for example with -[AVContentKeySession processContentKeyRequestWithIdentifier:initializationData:options:], the value of originatingRecipient will be nil.

The originatingRecipient of key requests from HLS interstitials will always be the corresponding interstitial AVURLAsset. To receive key requests for DRM-protected interstitial content, applications must ensure their AVContentKeySession is attached to these interstitial AVURLAssets.

These interstitial AVURLAssets may be retrieved from the primary AVURLAsset via AVPlayerInterstitialEventMonitor.

## See Also

- [var identifier: (any Sendable)?](avcontentkeyrequest/identifier.md)
  The identifier for the content key.
- [var canProvidePersistableContentKey: Bool](avcontentkeyrequest/canprovidepersistablecontentkey.md)
  The content key request used to create a persistable content key or respond to a previous request with a persistable content key.
- [var error: (any Error)?](avcontentkeyrequest/error.md)
  The error description for a failed key request.
- [var initializationData: Data?](avcontentkeyrequest/initializationdata.md)
  The data used to obtain a key response.
- [var renewsExpiringResponseData: Bool](avcontentkeyrequest/renewsexpiringresponsedata.md)
  A Boolean value that indicates whether the content key request renews previously provided response data.
- [var status: AVContentKeyRequest.Status](avcontentkeyrequest/status-swift.property.md)
  The current state of the content key request.
- [AVContentKeyRequest.Status](avcontentkeyrequest/status-swift.enum.md)
  The status for a content key request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/originatingrecipient)*