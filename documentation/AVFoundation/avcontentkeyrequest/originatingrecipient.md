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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcontentkeyrequest/originatingrecipient)*