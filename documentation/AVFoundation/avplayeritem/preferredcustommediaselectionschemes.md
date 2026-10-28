# preferredCustomMediaSelectionSchemes

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

Indicates the AVCustomMediaSelectionSchemes of AVMediaSelectionGroups of the receiver’s asset with which an associated UI implementation should configure its interface for media selection.

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
var preferredCustomMediaSelectionSchemes: [AVCustomMediaSelectionScheme] { get set }
```

```objc
@property (nonatomic, copy) NSArray<AVCustomMediaSelectionScheme *> * preferredCustomMediaSelectionSchemes;
```

## Discussion

Recommended usage: if use of a custom media selection scheme is desired, set this property before either replacing an AVPlayer’s current item with the receiver or adding the receiver to an AVQueuePlayer’s play queue. This will satisfy requirements of UI implementations that commit to a configuration of UI elements as the receiver becomes ready to play.

## See Also

### Selecting media options
- [func select(AVMediaPresentationSetting, for: AVMediaSelectionGroup)](./select%28_,for%29.md)
  When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular presentation setting, replacing any previous preference for settings of the same media presentation selector.
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
- [func select(AVMediaSelectionOption?, in: AVMediaSelectionGroup)](./select%28_,in%29.md)
  Selects a media option in a given media selection group and deselects all other options in that group.
- [func selectMediaOptionAutomatically(in: AVMediaSelectionGroup)](./selectmediaoptionautomatically%28in%29.md)
  Selects the media option in the specified media selection group that best matches the receiver’s automatic selection criteria.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/preferredcustommediaselectionschemes)*