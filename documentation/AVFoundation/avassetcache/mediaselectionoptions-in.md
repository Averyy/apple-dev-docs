# mediaSelectionOptions(in:)

**Framework**: AVFoundation  
**Kind**: method

Returns an array of locally cached media selection options that are available for offline use.

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
func mediaSelectionOptions(in mediaSelectionGroup: AVMediaSelectionGroup) -> [AVMediaSelectionOption]
```

#### Return Value

The array of media selection options, or an empty array if none are available.

## Parameters

- `mediaSelectionGroup`: The containing media selection group.

## See Also

- [var isPlayableOffline: Bool](avassetcache/isplayableoffline.md)
  A Boolean value that indicates whether the asset is playable without an internet connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetcache/mediaselectionoptions(in:))*