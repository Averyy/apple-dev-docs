# mediaPresentationSettings(for:)

**Framework**: AVFoundation  
**Kind**: method

For each AVMediaPresentationSelector defined by the AVCustomMediaSelectionScheme of an AVMediaSelectionGroup, returns the AVMediaPresentationSettings that can be satisfied for offline operations, e.g. playback.

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
func mediaPresentationSettings(for mediaSelectionGroup: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : [AVMediaPresentationSetting]]
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetcache/mediapresentationsettings(for:))*