# selectedMediaPresentationSettings(for:)

**Framework**: AVFoundation  
**Kind**: method

Indicates the media presentation settings that have most recently been selected for each AVMediaPresentationSelector of the AVCustomMediaSelectionScheme of the specified AVMediaSelectionGroup.

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
func selectedMediaPresentationSettings(for mediaSelectionGroup: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : Any]
```

#### Return Value

A dictionary with AVMediaPresentationSelectors as keys and AVMediaPresentationSettings as values, providing the most recently selected setting for each selector or, if no setting has previously been selected, NSNull.

## Parameters

- `mediaSelectionGroup`: An AVMediaSelectionGroup obtained from the receiver’s asset for which the currently selected media presentation settings are desired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/selectedmediapresentationsettings(for:))*