# videoProvider

**Framework**: Link Presentation  
**Kind**: property

An object that retrieves data corresponding to a representative video for the URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var videoProvider: NSItemProvider? { get set }
```

#### Discussion

The item provider returns a video that [`AVFoundation`](https://developer.apple.com/documentation/AVFoundation) can play.

## See Also

- [var remoteVideoURL: URL?](lplinkmetadata/remotevideourl.md)
  A remote URL corresponding to a representative video for the URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lplinkmetadata/videoprovider)*