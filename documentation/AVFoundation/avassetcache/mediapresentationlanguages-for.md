# mediaPresentationLanguages(for:)

**Framework**: AVFoundation  
**Kind**: method

Returns an array of extended language tags for languages that can be selected for offline operations via use of the AVMediaSelectionGroup’s AVCustomMediaSelectionScheme.

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
func mediaPresentationLanguages(for mediaSelectionGroup: AVMediaSelectionGroup) -> [String]
```

## See Also

- [var isPlayableOffline: Bool](avassetcache/isplayableoffline.md)
  A Boolean value that indicates whether the asset is playable without an internet connection.
- [func mediaSelectionOptions(in: AVMediaSelectionGroup) -> [AVMediaSelectionOption]](avassetcache/mediaselectionoptions(in:).md)
  Returns an array of locally cached media selection options that are available for offline use.
- [func mediaPresentationSettings(for: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : [AVMediaPresentationSetting]]](avassetcache/mediapresentationsettings(for:).md)
  For each AVMediaPresentationSelector defined by the AVCustomMediaSelectionScheme of an AVMediaSelectionGroup, returns the AVMediaPresentationSettings that can be satisfied for offline operations, e.g. playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetcache/mediapresentationlanguages(for:))*