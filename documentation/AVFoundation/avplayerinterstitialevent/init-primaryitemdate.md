# init(primaryItem:date:)

**Framework**: AVFoundation  
**Kind**: init

Creates an interstitial event for the specified date.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
convenience init(primaryItem: AVPlayerItem, date: Date)
```

## Parameters

- `primaryItem`: A player item that provides the primary playback content. It defines the timeline during which an interstitial event occurs. The item must have an asset that provides an intrinsic mapping from its timeline to real-time dates.
- `date`: A date within the timeline of the primary item at which to temporarily suspend playback of primary content, and play interstitial content instead.

## See Also

- [convenience init(primaryItem: AVPlayerItem, time: CMTime)](avplayerinterstitialevent/init(primaryitem:time:).md)
  Creates an interstitial event for the specified time.
- [convenience init(primaryItem: AVPlayerItem, identifier: String?, time: CMTime, templateItems: [AVPlayerItem], restrictions: AVPlayerInterstitialEvent.Restrictions, resumptionOffset: CMTime, playoutLimit: CMTime, userDefinedAttributes: [String : Any])](avplayerinterstitialevent/init(primaryitem:identifier:time:templateitems:restrictions:resumptionoffset:playoutlimit:userdefinedattributes:).md)
  Creates an interstitial event, with user-defined attributes, for the specified time.
- [convenience init(primaryItem: AVPlayerItem, identifier: String?, date: Date, templateItems: [AVPlayerItem], restrictions: AVPlayerInterstitialEvent.Restrictions, resumptionOffset: CMTime, playoutLimit: CMTime, userDefinedAttributes: [String : Any])](avplayerinterstitialevent/init(primaryitem:identifier:date:templateitems:restrictions:resumptionoffset:playoutlimit:userdefinedattributes:).md)
  Creates an interstitial event, with user-defined attributes, for the specified date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/init(primaryitem:date:))*