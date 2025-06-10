# AVAssetCache

**Framework**: AVFoundation  
**Kind**: class

An object that you use to inspect locally cached media data.

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
class AVAssetCache
```

#### Overview

You can download HTTP Live Streaming assets to an iOS device using the [`AVAssetDownloadURLSession`](avassetdownloadurlsession.md) and [`AVAssetDownloadTask`](avassetdownloadtask.md) classes.

## Topics

### Inspecting the Cached Media
- [var isPlayableOffline: Bool](avassetcache/isplayableoffline.md)
  A Boolean value that indicates whether the asset is playable without an internet connection.
- [func mediaSelectionOptions(in: AVMediaSelectionGroup) -> [AVMediaSelectionOption]](avassetcache/mediaselectionoptions(in:).md)
  Returns an array of locally cached media selection options that are available for offline use.
### Instance Methods
- [func mediaPresentationLanguages(for: AVMediaSelectionGroup) -> [String]](avassetcache/mediapresentationlanguages(for:).md)
  Returns an array of extended language tags for languages that can be selected for offline operations via use of the AVMediaSelectionGroup’s AVCustomMediaSelectionScheme.
- [func mediaPresentationSettings(for: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : [AVMediaPresentationSetting]]](avassetcache/mediapresentationsettings(for:).md)
  For each AVMediaPresentationSelector defined by the AVCustomMediaSelectionScheme of an AVMediaSelectionGroup, returns the AVMediaPresentationSettings that can be satisfied for offline operations, e.g. playback.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetcache)*