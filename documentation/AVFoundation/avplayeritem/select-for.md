# select(_:for:)

**Framework**: AVFoundation  
**Kind**: method

When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular presentation setting, replacing any previous preference for settings of the same media presentation selector.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
func select(_ mediaPresentationSetting: AVMediaPresentationSetting, for mediaSelectionGroup: AVMediaSelectionGroup)
```

#### Discussion

Note that preferences for media characteristics indicated by selected AVMediaPresentationSettings are treated as supplemental to the associated AVPlayer’s media selection criteria for the AVMediaSelectionGroup. An AVPlayer’s default media selection criteria can also indicate preferences for media characteristics, such as those indicating the availability of accessibility affordances such as audio descriptions, and these media characteristics can be left up to the AVPlayer to manage even when an AVCustomMediaSelectionScheme is in use. But if you wish to do so, you can use AVMediaPresentationSettings offered by a AVCustomMediaSelectionScheme in combination with custom AVPlayerMediaSelectionCriteria. If the specified setting isn’t offered by an AVMediaPresentationSelector of the AVCustomMediaSelectionScheme of the specified AVMediaSelectionGroup, no change in the presentation of the media will result. This method has no effect when the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property has a value of NO, in which case you must use -selectMediaOption:inMediaSelectionGroup: instead in order to alter the presentation state of the media.

## Parameters

- `mediaPresentationSetting`: The setting to select.
- `mediaSelectionGroup`: The media selection group, obtained from the receiver’s asset, to which the specified setting is to be applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/select(_:for:))*