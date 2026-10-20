# requestUploadFile(_:options:uploadDelegate:didUploadSelector:contextInfo:)

**Framework**: ImageCaptureCore  
**Kind**: method

Uploads a file to the camera.

**Availability**:
- macOS 10.4+

## Declaration

```swift
func requestUploadFile(_ fileURL: URL, options: [ICUploadOption : Any] = [:], uploadDelegate: Any, didUploadSelector selector: Selector, contextInfo: UnsafeMutableRawPointer?)
```

#### Discussion

The `uploadDelegate` must implement a function with the signature `- (void)didUploadFile:(NSURL*)fileURL error:(NSError*)error contextInfo:(void*)contextInfo`, to be called when the request is completed.

## See Also

- [struct ICUploadOption](icuploadoption.md)
  An option for uploading a file to the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/requestuploadfile(_:options:uploaddelegate:diduploadselector:contextinfo:))*