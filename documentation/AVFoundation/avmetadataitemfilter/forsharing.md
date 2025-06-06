# forSharing()

**Framework**: AVFoundation  
**Kind**: method

Returns a metadata filter to use for sharing assets.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func forSharing() -> AVMetadataItemFilter
```

#### Return Value

An instance of an `AVMetadataItemFilter`.

#### Discussion

Removes user-identifying metadata items, such as location information, and leaves only metadata related to commerce or playback itself. For example, playback, copyright, and commercial-related metadata, such as a purchaser’s ID as set by a vendor of digital media, along with metadata either derivable from the media itself or necessary for its proper behavior are all left intact.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmetadataitemfilter/forsharing())*