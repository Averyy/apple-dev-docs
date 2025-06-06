# contentSharingPicker(_:didCancelFor:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Required**: Yes

Tells the observer that a sharing picker canceled selection for a stream.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
func contentSharingPicker(_ picker: SCContentSharingPicker, didCancelFor stream: SCStream?)
```

## Parameters

- `picker`: The content-sharing picker that sent this event.
- `stream`: The canceled stream, if any.

## See Also

- [func contentSharingPicker(SCContentSharingPicker, didUpdateWith: SCContentFilter, for: SCStream?)](sccontentsharingpickerobserver/contentsharingpicker(_:didupdatewith:for:).md)
  Tells the observer that a sharing picker updated the content filter for a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerobserver/contentsharingpicker(_:didcancelfor:))*