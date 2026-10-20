# mediaPresentationSettings(for:)

**Framework**: AVFoundation  
**Kind**: method  
**Role**: Instance Method

For each AVMediaPresentationSelector defined by the AVCustomMediaSelectionScheme of an AVMediaSelectionGroup, returns the AVMediaPresentationSettings that can be satisfied for offline operations, e.g. playback.

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
func mediaPresentationSettings(for mediaSelectionGroup: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : [AVMediaPresentationSetting]]
```

```objc
- (NSDictionary<AVMediaPresentationSelector *,NSArray<AVMediaPresentationSetting *> *> *) mediaPresentationSettingsForMediaSelectionGroup:(AVMediaSelectionGroup *) mediaSelectionGroup;
```

## See Also

### Inspecting the cached media
- [var isPlayableOffline: Bool](./isplayableoffline.md)
  A Boolean value that indicates whether the asset is playable without an internet connection.
- [func mediaSelectionOptions(in: AVMediaSelectionGroup) -> [AVMediaSelectionOption]](./mediaselectionoptions%28in%29.md)
  Returns an array of locally cached media selection options that are available for offline use.
- [func mediaPresentationLanguages(for: AVMediaSelectionGroup) -> [String]](./mediapresentationlanguages%28for%29.md)
  Returns an array of extended language tags for languages that can be selected for offline operations via use of the AVMediaSelectionGroup’s AVCustomMediaSelectionScheme.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetcache/mediapresentationsettings(for:))*