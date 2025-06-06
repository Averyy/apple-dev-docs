# contentSharingPicker(_:didUpdateWith:for:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Required**: Yes

Tells the observer that a sharing picker updated the content filter for a stream.

**Availability**:
- Mac Catalyst 18.2+
- macOS 14.0+

## Declaration

```swift
func contentSharingPicker(_ picker: SCContentSharingPicker, didUpdateWith filter: SCContentFilter, for stream: SCStream?)
```

## Parameters

- `picker`: The content-sharing picker that sent this event.
- `filter`: The new filter applied to streaming content.
- `stream`: The changed stream, if any.

## See Also

- [func contentSharingPicker(SCContentSharingPicker, didCancelFor: SCStream?)](sccontentsharingpickerobserver/contentsharingpicker(_:didcancelfor:).md)
  Tells the observer that a sharing picker canceled selection for a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerobserver/contentsharingpicker(_:didupdatewith:for:))*