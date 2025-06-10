# effectiveMediaPresentationSettings(for:)

**Framework**: AVFoundation  
**Kind**: method

Indicates the media presentation settings with media characteristics that are possessed by the currently selected AVMediaSelectionOption in the specified AVMediaSelectionGroup.

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
func effectiveMediaPresentationSettings(for mediaSelectionGroup: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : Any]
```

#### Return Value

A dictionary with AVMediaPresentationSelectors as keys and AVMediaPresentationSettings as values, unless the AVMediaSelectionOption currently selected in the group possesses none of the characteristics associated with the selector’s settings. In that case the dictionary value will be NSNull.

#### Discussion

Effective media presentation settings can differ from the currently effective media presentation settings if no AVMediaSelectionOption of the specified AVMediaSelectionGroup with the currently selected media presentation language possesses all of the characteristics associated with the currently selected settings. A value of NSNull for an AVMediaPresentationSelector can occur if either the content is inappropriately authored for the use of the AVCustomMediaSelectionScheme or if the currently selected AVMediaSelectionOption has been selected by means other than through the use of AVMediaPresentationSettings.

## Parameters

- `mediaSelectionGroup`: An AVMediaSelectionGroup obtained from the receiver’s asset for which the currently effective media presentation settings are desired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/effectivemediapresentationsettings(for:))*