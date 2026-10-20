# isPlayableOffline

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, getter=isPlayableOffline) BOOL playableOffline;
```

#### Discussion

Check the value of this property to determine the asset’s suitability for playback before presenting or attempting to play it.

> **Note**:  A property value of [`true`](../../Swift/true.md) doesn’t indicate that all of the asset’s associated media selection options are available for offline playback. Instead, call [`mediaSelectionOptions(in:)`](./mediaselectionoptions%28in%29.md) to determine which media selections are available.

## See Also

### Inspecting the cached media
- [func mediaSelectionOptions(in: AVMediaSelectionGroup) -> [AVMediaSelectionOption]](./mediaselectionoptions%28in%29.md)
  Returns an array of locally cached media selection options that are available for offline use.
- [func mediaPresentationLanguages(for: AVMediaSelectionGroup) -> [String]](./mediapresentationlanguages%28for%29.md)
  Returns an array of extended language tags for languages that can be selected for offline operations via use of the AVMediaSelectionGroup’s AVCustomMediaSelectionScheme.
- [func mediaPresentationSettings(for: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : [AVMediaPresentationSetting]]](./mediapresentationsettings%28for%29.md)
  For each AVMediaPresentationSelector defined by the AVCustomMediaSelectionScheme of an AVMediaSelectionGroup, returns the AVMediaPresentationSettings that can be satisfied for offline operations, e.g. playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetcache/isplayableoffline)*