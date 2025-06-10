# selectMediaPresentationLanguage(_:for:)

**Framework**: AVFoundation  
**Kind**: method

When the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property is set to YES, configures the player item to prefer a particular language, replacing any previous preference for available languages of the specified group’s custom media selection scheme.

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
func selectMediaPresentationLanguage(_ language: String, for mediaSelectionGroup: AVMediaSelectionGroup)
```

#### Discussion

Overrides preferences for languages specified by the AVPlayer’s current media selection criteria. This method has no effect when the associated AVPlayer’s appliesMediaSelectionCriteriaAutomatically property has a value of NO, in which case you must use -selectMediaOption:inMediaSelectionGroup: instead in order to alter the presentation state of the media.

## Parameters

- `mediaSelectionGroup`: The media selection group, obtained from the receiver’s asset, to which the specified setting is to be applied.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/selectmediapresentationlanguage(_:for:))*