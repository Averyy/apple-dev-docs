# AVAssetCache

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVAssetCache : NSObject
```

#### Overview

You can download HTTP Live Streaming assets to an iOS device using the [`AVAssetDownloadURLSession`](./avassetdownloadurlsession.md) and [`AVAssetDownloadTask`](./avassetdownloadtask.md) classes.

## Topics

### Inspecting the cached media
- [var isPlayableOffline: Bool](./avassetcache/isplayableoffline.md)
  A Boolean value that indicates whether the asset is playable without an internet connection.
- [func mediaSelectionOptions(in: AVMediaSelectionGroup) -> [AVMediaSelectionOption]](./avassetcache/mediaselectionoptions%28in%29.md)
  Returns an array of locally cached media selection options that are available for offline use.
- [func mediaPresentationLanguages(for: AVMediaSelectionGroup) -> [String]](./avassetcache/mediapresentationlanguages%28for%29.md)
  Returns an array of extended language tags for languages that can be selected for offline operations via use of the AVMediaSelectionGroup’s AVCustomMediaSelectionScheme.
- [func mediaPresentationSettings(for: AVMediaSelectionGroup) -> [AVMediaPresentationSelector : [AVMediaPresentationSetting]]](./avassetcache/mediapresentationsettings%28for%29.md)
  For each AVMediaPresentationSelector defined by the AVCustomMediaSelectionScheme of an AVMediaSelectionGroup, returns the AVMediaPresentationSettings that can be satisfied for offline operations, e.g. playback.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetcache)*