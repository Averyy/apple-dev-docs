# requestMetadataDictionary(options:completion:)

**Framework**: ImageCaptureCore  
**Kind**: method

Requests metadata and executes the completion block in place of the delegate.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func requestMetadataDictionary(options: [ICCameraItemMetadataOption : Any]? = nil) async throws -> [AnyHashable : Any]
```

#### Discussion

The completion block executes on an any available queue; often this is not the main queue.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccamerafile/requestmetadatadictionary(options:completion:))*