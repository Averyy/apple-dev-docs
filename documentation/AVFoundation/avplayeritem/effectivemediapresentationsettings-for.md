# effectiveMediaPresentationSettings(for:)

**Framework**: AVFoundation  
**Kind**: method

Indicates the media presentation settings with media characteristics that are possessed by the currently selected AVMediaSelectionOption in the specified AVMediaSelectionGroup.

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
func effectiveMediaPresentationSettings(for mediaSelectionGroup: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : Any]
```

#### Return Value

A dictionary with AVMediaPresentationSelectors as keys and AVMediaPresentationSettings as values, unless the AVMediaSelectionOption currently selected in the group possesses none of the characteristics associated with the selector’s settings. In that case the dictionary value will be NSNull.

#### Discussion

Effective media presentation settings can differ from the currently effective media presentation settings if no AVMediaSelectionOption of the specified AVMediaSelectionGroup with the currently selected media presentation language possesses all of the characteristics associated with the currently selected settings. A value of NSNull for an AVMediaPresentationSelector can occur if either the content is inappropriately authored for the use of the AVCustomMediaSelectionScheme or if the currently selected AVMediaSelectionOption has been selected by means other than through the use of AVMediaPresentationSettings.

## Parameters

- `mediaSelectionGroup`: An AVMediaSelectionGroup obtained from the receiver’s asset for which the currently effective media presentation settings are desired.

## See Also

- [func select(AVMediaPresentationSetting, for: AVMediaSelectionGroup)](avplayeritem/select(_:for:).md)
  When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular presentation setting, replacing any previous preference for settings of the same media presentation selector.
- [var preferredCustomMediaSelectionSchemes: [AVCustomMediaSelectionScheme]](avplayeritem/preferredcustommediaselectionschemes.md)
  Indicates the AVCustomMediaSelectionSchemes of AVMediaSelectionGroups of the receiver’s asset with which an associated UI implementation should configure its interface for media selection.
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

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/effectivemediapresentationsettings(for:))*