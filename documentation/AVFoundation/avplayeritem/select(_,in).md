# select(_:in:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

Selects a media option in a given media selection group and deselects all other options in that group.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
nonisolated
func select(_ mediaSelectionOption: AVMediaSelectionOption?, in mediaSelectionGroup: AVMediaSelectionGroup)
```

```objc
- (void) selectMediaOption:(AVMediaSelectionOption *) mediaSelectionOption inMediaSelectionGroup:(AVMediaSelectionGroup *) mediaSelectionGroup;
```

## Mentions

- [Selecting subtitles and alternative audio tracks](../selecting-subtitles-and-alternative-audio-tracks.md)

## Discussion

If `mediaSelectionOption` isn’t a member of the `mediaSelectionGroup`, no change in presentation state will result.

If multiple options within a group meet your criteria for selection according to locale or other considerations, and if these options are otherwise indistinguishable to you according to media characteristics that are meaningful for your application, content is typically authored so that the first available option that meets your criteria is appropriate for selection.

## Parameters

- `mediaSelectionOption`: The option to select.

  If the value of the [`allowsEmptySelection`](../avmediaselectiongroup/allowsemptyselection.md) property of `mediaSelectionGroup` is [`true`](../../Swift/true.md), you can pass `nil` to deselect all media selection options in the group.
- `mediaSelectionGroup`: The media selection group, obtained from the receiver’s asset, that contains `mediaSelectionOption`.

## See Also

### Selecting media options
- [func select(AVMediaPresentationSetting, for: AVMediaSelectionGroup)](./select%28_,for%29.md)
  When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular presentation setting, replacing any previous preference for settings of the same media presentation selector.
- [var preferredCustomMediaSelectionSchemes: [AVCustomMediaSelectionScheme]](./preferredcustommediaselectionschemes.md)
  Indicates the AVCustomMediaSelectionSchemes of AVMediaSelectionGroups of the receiver’s asset with which an associated UI implementation should configure its interface for media selection.
- [func effectiveMediaPresentationSettings(for: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : Any]](./effectivemediapresentationsettings%28for%29.md)
  Indicates the media presentation settings with media characteristics that are possessed by the currently selected AVMediaSelectionOption in the specified AVMediaSelectionGroup.
- [func selectMediaPresentationLanguage(String, for: AVMediaSelectionGroup)](./selectmediapresentationlanguage%28_,for%29.md)
  When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular language, replacing any previous preference for available languages of the specified group’s custom media selection scheme.
- [func selectedMediaPresentationLanguage(for: AVMediaSelectionGroup) -> String?](./selectedmediapresentationlanguage%28for%29.md)
  Returns the selected media presentation language for the specified media selection group, if any language has previously been selected via use of -selectMediaPresentationLanguages:forMediaSelectionGroup:.
- [func selectedMediaPresentationSettings(for: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : Any]](./selectedmediapresentationsettings%28for%29.md)
  Indicates the media presentation settings that have most recently been selected for each AVMediaPresentationSelector of the AVCustomMediaSelectionScheme of the specified AVMediaSelectionGroup.
- [var currentMediaSelection: AVMediaSelection](./currentmediaselection.md)
  The current media selections for each of the receiver’s media selection groups.
- [func selectMediaOptionAutomatically(in: AVMediaSelectionGroup)](./selectmediaoptionautomatically%28in%29.md)
  Selects the media option in the specified media selection group that best matches the receiver’s automatic selection criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/select(_:in:))*