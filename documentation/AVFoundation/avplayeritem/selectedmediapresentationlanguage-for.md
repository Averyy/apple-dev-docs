# selectedMediaPresentationLanguage(for:)

**Framework**: AVFoundation  
**Kind**: method

Returns the selected media presentation language for the specified media selection group, if any language has previously been selected via use of -selectMediaPresentationLanguages:forMediaSelectionGroup:.

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
func selectedMediaPresentationLanguage(for mediaSelectionGroup: AVMediaSelectionGroup) -> String?
```

## Parameters

- `mediaSelectionGroup`: The media selection group, obtained from the receiver’s asset, for which the selected media presentation language is requested.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avplayeritem/selectedmediapresentationlanguage(for:))*