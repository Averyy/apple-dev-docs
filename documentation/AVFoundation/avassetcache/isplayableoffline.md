# isPlayableOffline

**Framework**: AVFoundation  
**Kind**: property

A Boolean value that indicates whether the asset is playable without an internet connection.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
var isPlayableOffline: Bool { get }
```

#### Discussion

Check the value of this property to determine the asset’s suitability for playback before presenting or attempting to play it.

> **Note**:  A property value of [`true`](https://developer.apple.com/documentation/Swift/true) doesn’t indicate that all of the asset’s associated media selection options are available for offline playback. Instead, call [`mediaSelectionOptions(in:)`](avassetcache/mediaselectionoptions(in:).md) to determine which media selections are available.

## See Also

- [func mediaSelectionOptions(in: AVMediaSelectionGroup) -> [AVMediaSelectionOption]](avassetcache/mediaselectionoptions(in:).md)
  Returns an array of locally cached media selection options that are available for offline use.
- [func mediaPresentationLanguages(for: AVMediaSelectionGroup) -> [String]](avassetcache/mediapresentationlanguages(for:).md)
  Returns an array of extended language tags for languages that can be selected for offline operations via use of the AVMediaSelectionGroup’s AVCustomMediaSelectionScheme.
- [func mediaPresentationSettings(for: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : [AVMediaPresentationSetting]]](avassetcache/mediapresentationsettings(for:).md)
  For each AVMediaPresentationSelector defined by the AVCustomMediaSelectionScheme of an AVMediaSelectionGroup, returns the AVMediaPresentationSettings that can be satisfied for offline operations, e.g. playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetcache/isplayableoffline)*