# selectMediaOptionAutomatically(in:)

**Framework**: AVFoundation  
**Kind**: method

Selects the media option in the specified media selection group that best matches the receiver’s automatic selection criteria.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
func selectMediaOptionAutomatically(in mediaSelectionGroup: AVMediaSelectionGroup)
```

#### Discussion

This method has no effect unless the [`appliesMediaSelectionCriteriaAutomatically`](avplayer/appliesmediaselectioncriteriaautomatically.md) property of the associated [`AVPlayer`](avplayer.md) is [`true`](https://developer.apple.com/documentation/Swift/true) and unless automatic media selection has previously been overridden by invoking [`select(_:in:)`](avplayeritem/select(_:in:).md).

## Parameters

- `mediaSelectionGroup`: The media selection group, obtained from the receiver’s  , that contains the specified option.

## See Also

- [func select(AVMediaPresentationSetting, for: AVMediaSelectionGroup)](avplayeritem/select(_:for:).md)
  When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular presentation setting, replacing any previous preference for settings of the same media presentation selector.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/selectmediaoptionautomatically(in:))*