# requestDownload(options:completion:)

**Framework**: ImageCaptureCore  
**Kind**: method

Requests a download and executes the completion block in place of the delegate.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func requestDownload(options: [ICDownloadOption : Any]? = nil, completion: @escaping (String?, (any Error)?) -> Void) -> Progress?
```

#### Discussion

The completion block executes on an any available queue; often this is not the main queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccamerafile/requestdownload(options:completion:))*