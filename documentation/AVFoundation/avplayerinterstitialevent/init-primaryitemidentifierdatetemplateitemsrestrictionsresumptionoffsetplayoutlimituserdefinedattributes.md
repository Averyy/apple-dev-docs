# init(primaryItem:identifier:date:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:)

**Framework**: AVFoundation  
**Kind**: init

Creates an interstitial event, with user-defined attributes, for the specified date.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
convenience init(primaryItem: AVPlayerItem, identifier: String?, date: Date, templateItems: [AVPlayerItem], restrictions: AVPlayerInterstitialEvent.Restrictions = [], resumptionOffset: CMTime = .indefinite, playoutLimit: CMTime = .invalid, userDefinedAttributes: [String : Any] = [:])
```

## Parameters

- `primaryItem`: The player item that represents the primary content. The item must contain an   that provides intrinsic mappings from its timeline to real-time dates.
- `identifier`: An external identifier for the event.
- `date`: A date within the date range of the primary item that playback of interstitial content begins.
- `templateItems`: An array of player item configurations to use as templates for player items that play interstitial content.
- `restrictions`: Restrictions on access to playback controls during the event.
- `resumptionOffset`: The time offset for resuming playback of the primary content after interstitial content finishes. You can specify a definite time, or specify   to indicate that the effective resumption time offset needs to align with time elapsed during interstitial playback.
- `playoutLimit`: The time offset from the beginning of the interstitial when interstitial playback needs to end, if interstitial assets are longer. Pass a positive numeric value, or   to indicate no play out limit.
- `userDefinedAttributes`: Custom attributes to add to the event.

## See Also

- [convenience init(primaryItem: AVPlayerItem, time: CMTime)](avplayerinterstitialevent/init(primaryitem:time:).md)
  Creates an interstitial event for the specified time.
- [convenience init(primaryItem: AVPlayerItem, date: Date)](avplayerinterstitialevent/init(primaryitem:date:).md)
  Creates an interstitial event for the specified date.
- [convenience init(primaryItem: AVPlayerItem, identifier: String?, time: CMTime, templateItems: [AVPlayerItem], restrictions: AVPlayerInterstitialEvent.Restrictions, resumptionOffset: CMTime, playoutLimit: CMTime, userDefinedAttributes: [String : Any])](avplayerinterstitialevent/init(primaryitem:identifier:time:templateitems:restrictions:resumptionoffset:playoutlimit:userdefinedattributes:).md)
  Creates an interstitial event, with user-defined attributes, for the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/init(primaryitem:identifier:date:templateitems:restrictions:resumptionoffset:playoutlimit:userdefinedattributes:))*