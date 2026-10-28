# remoteVideoURL

**Framework**: Link Presentation  
**Kind**: property  
**Role**: Instance Property

A remote URL corresponding to a representative video for the URL.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var remoteVideoURL: URL? { get set }
```

```objc
@property (nonatomic, retain, nullable) NSURL * remoteVideoURL;
```

## Discussion

This may reference a remote video file that [AVFoundation](../../AVFoundation/AVFoundation.md) can stream.

## See Also

### Getting the link’s video
- [var videoProvider: NSItemProvider?](./videoprovider.md)
  An object that retrieves data corresponding to a representative video for the URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/linkpresentation/lplinkmetadata/remotevideourl)*