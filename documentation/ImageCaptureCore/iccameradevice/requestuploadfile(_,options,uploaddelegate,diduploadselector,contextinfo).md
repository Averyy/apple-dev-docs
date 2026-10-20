# requestUploadFile(_:options:uploadDelegate:didUploadSelector:contextInfo:)

**Framework**: ImageCaptureCore  
**Kind**: method  
**Role**: Instance Method

Uploads a file to the camera.

**Availability**:
- macOS 10.4+ - Deprecated in 14.0

> **Deprecated**: Sandbox restrictions prohibit writing directly to device hardware

## Declaration

```swift
func requestUploadFile(_ fileURL: URL, options: [ICUploadOption : Any] = [:], uploadDelegate: Any, didUploadSelector selector: Selector, contextInfo: UnsafeMutableRawPointer?)
```

```objc
- (void) requestUploadFile:(NSURL *) fileURL options:(NSDictionary<NSString *,id> *) options uploadDelegate:(id) uploadDelegate didUploadSelector:(SEL) selector contextInfo:(void *) contextInfo;
```

#### Discussion

The `uploadDelegate` must implement a function with the signature `- (void)didUploadFile:(NSURL*)fileURL error:(NSError*)error contextInfo:(void*)contextInfo`, to be called when the request is completed.

## See Also

### Uploading Files
- [struct ICUploadOption](../icuploadoption.md)
  An option for uploading a file to the camera.


---

*[View on Apple Developer](https://developer.apple.com/documentation/imagecapturecore/iccameradevice/requestuploadfile(_:options:uploaddelegate:diduploadselector:contextinfo:))*