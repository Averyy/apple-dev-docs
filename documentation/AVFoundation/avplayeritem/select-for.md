# select(_:for:)

**Framework**: AVFoundation  
**Kind**: method

When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular presentation setting, replacing any previous preference for settings of the same media presentation selector.

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
@MainActor
func select(_ mediaPresentationSetting: AVMediaPresentationSetting, for mediaSelectionGroup: AVMediaSelectionGroup)
```

#### Discussion

Note that preferences for media characteristics indicated by selected AVMediaPresentationSettings are treated as supplemental to the associated AVPlayer’s media selection criteria for the AVMediaSelectionGroup. An AVPlayer’s default media selection criteria can also indicate preferences for media characteristics, such as those indicating the availability of accessibility affordances such as audio descriptions, and these media characteristics can be left up to the AVPlayer to manage even when an AVCustomMediaSelectionScheme is in use. But if you wish to do so, you can use AVMediaPresentationSettings offered by a AVCustomMediaSelectionScheme in combination with custom AVPlayerMediaSelectionCriteria. If the specified setting isn’t offered by an AVMediaPresentationSelector of the AVCustomMediaSelectionScheme of the specified AVMediaSelectionGroup, no change in the presentation of the media will result. This method has no effect when the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property has a value of NO, in which case you must use -selectMediaOption:inMediaSelectionGroup: instead in order to alter the presentation state of the media.

## Parameters

- `mediaPresentationSetting`: The setting to select.
- `mediaSelectionGroup`: The media selection group, obtained from the receiver’s asset, to which the specified setting is to be applied.

## See Also

- [var preferredCustomMediaSelectionSchemes: [AVCustomMediaSelectionScheme]](avplayeritem/preferredcustommediaselectionschemes.md)
  Indicates the AVCustomMediaSelectionSchemes of AVMediaSelectionGroups of the receiver’s asset with which an associated UI implementation should configure its interface for media selection.
- [func effectiveMediaPresentationSettings(for: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : Any]](avplayeritem/effectivemediapresentationsettings(for:).md)
  Indicates the media presentation settings with media characteristics that are possessed by the currently selected AVMediaSelectionOption in the specified AVMediaSelectionGroup.
- [func selectMediaPresentationLanguage(String, for: AVMediaSelectionGroup)](avplayeritem/selectmediapresentationlanguage(_:for:).md)
  When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular language, replacing any previous preference for available languages of the specified group’s custom media selection scheme.
- [func selectedMediaPresentationLanguage(for: AVMediaSelectionGroup) -> String?](avplayeritem/selectedmediapresentationlanguage(for:).md)
  Returns the selected media presentation language for the specified media selection group, if any language has previously been selected via use of -selectMediaPresentationLanguages:forMediaSelectionGroup:.
- [func selectedMediaPresentationSettings(for: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : Any]](avplayeritem/selectedmediapresentationsettings(for:).md)
  Indicates the media presentation settings that have most recently been selected for each AVMediaPresentationSelector of the AVCustomMediaSelectionScheme of the specified AVMediaSelectionGroup.
- [var currentMediaSelection: AVMediaSelection](avplayeritem/currentmediaselection.md)
  The current media selections for each of the receiver’s media selection groups.
- [func select(AVMediaSelectionOption?, in: AVMediaSelectionGroup)](avplayeritem/select(_:in:).md)
  Selects a media option in a given media selection group and deselects all other options in that group.
- [func selectMediaOptionAutomatically(in: AVMediaSelectionGroup)](avplayeritem/selectmediaoptionautomatically(in:).md)
  Selects the media option in the specified media selection group that best matches the receiver’s automatic selection criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/select(_:for:))*