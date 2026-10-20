# ICUploadOption

**Framework**: ImageCaptureCore  
**Kind**: struct  
**Role**: Structure

An option for uploading a file to the camera.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- visionOS 1.0+

## Declaration

```swift
struct ICUploadOption
```

```c
typedef NSString * ICUploadOption;
```

## Topics

### Initializers
- [init(rawValue: String)](./icuploadoption/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Uploading Files
- [func requestUploadFile(URL, options: [ICUploadOption : Any], uploadDelegate: Any, didUploadSelector: Selector, contextInfo: UnsafeMutableRawPointer?)](./iccameradevice/requestuploadfile%28_,options,uploaddelegate,diduploadselector,contextinfo%29.md)
  Uploads a file to the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/icuploadoption)*