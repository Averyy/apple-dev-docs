# isPlayableOffline

**Framework**: Avfoundation  
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

> **Note**:  A property value of [`true`](https://developer.apple.com/documentation/swift/true) doesn’t indicate that all of the asset’s associated media selection options are available for offline playback. Instead, call [`mediaSelectionOptions(in:)`](avassetcache/mediaselectionoptions(in:).md) to determine which media selections are available.

## See Also

- [func mediaSelectionOptions(in: AVMediaSelectionGroup) -> [AVMediaSelectionOption]](avassetcache/mediaselectionoptions(in:).md)
  Returns an array of locally cached media selection options that are available for offline use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avassetcache/isplayableoffline)*