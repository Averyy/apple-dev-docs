# interstitialEventWithPrimaryItem:identifier:date:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Type Method

Creates an interstitial event, with user-defined attributes, for the specified date.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0
- iPadOS 15.0+ - Deprecated in 18.0
- Mac Catalyst 15.0+ - Deprecated in 18.0
- macOS 12.0+ - Deprecated in 15.0
- tvOS 15.0+ - Deprecated in 18.0
- watchOS 8.0+ - Deprecated in 11.0

> **Deprecated**: Use [`init(primaryItem:date:)`](./init%28primaryitem,date%29.md) instead.

## Declaration

```objc
+ (instancetype) interstitialEventWithPrimaryItem:(AVPlayerItem *) primaryItem identifier:(NSString *) identifier date:(NSDate *) date templateItems:(NSArray<AVPlayerItem *> *) templateItems restrictions:(AVPlayerInterstitialEventRestrictions) restrictions resumptionOffset:(CMTime) resumptionOffset playoutLimit:(CMTime) playoutLimit userDefinedAttributes:(NSDictionary *) userDefinedAttributes;
```

## Parameters

- `primaryItem`: The player item that represents the primary content. The item must contain an [`AVAsset`](../avasset.md) that provides intrinsic mappings from its timeline to real-time dates.
- `identifier`: An external identifier for the event.
- `date`: A date within the date range of the primary item that playback of interstitial content begins.
- `templateItems`: An array of player item configurations to use as templates for player items that play interstitial content.
- `restrictions`: Restrictions on access to playback controls during the event.
- `resumptionOffset`: The time offset for resuming playback of the primary content after interstital content finishes. You can specify a definite time, or specify [`indefinite`](../../CoreMedia/cmtime/indefinite.md) to indicate that the effective resumption time offset needs to align with time elapsed during interstitial playback.
- `playoutLimit`: The time offset from the beginning of the interstitial when interstitial playback needs to end, if interstitial assets are longer. Pass a positive numeric value, or [`invalid`](../../CoreMedia/cmtime/invalid.md) to indicate no playout limit.
- `userDefinedAttributes`: Custom attributes to add to the event.

## See Also

### Creating an event
- [convenience init(primaryItem: AVPlayerItem, time: CMTime)](./init%28primaryitem,time%29.md)
  Creates an interstitial event for the specified time.
- [convenience init(primaryItem: AVPlayerItem, date: Date)](./init%28primaryitem,date%29.md)
  Creates an interstitial event for the specified date.
- [+ interstitialEventWithPrimaryItem:identifier:time:templateItems:restrictions:resumptionOffset:playoutLimit:userDefinedAttributes:](./interstitialeventwithprimaryitem_identifier_time_templateitems_restrictions_resumptionoffset_playoutlimit_userdefinedattributes_.md)
  Creates an interstitial event, with user-defined attributes, for the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/interstitialeventwithprimaryitem:identifier:date:templateitems:restrictions:resumptionoffset:playoutlimit:userdefinedattributes:)*