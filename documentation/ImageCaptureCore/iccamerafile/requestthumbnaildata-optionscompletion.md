# requestThumbnailData(options:completion:)

**Framework**: ImageCaptureCore  
**Kind**: method

Requests a thumbnail and executes the completion block in place of the delegate.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func requestThumbnailData(options: [ICCameraItemThumbnailOption : Any]? = nil) async throws -> Data
```

#### Discussion

The completion block executes on an any available queue; often this is not the main queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccamerafile/requestthumbnaildata(options:completion:))*