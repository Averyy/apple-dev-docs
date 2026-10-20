# contentSharingPicker(_:didCancelFor:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the observer that a sharing picker canceled selection for a stream.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 14.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func contentSharingPicker(_ picker: SCContentSharingPicker, didCancelFor stream: SCStream?)
```

```objc
- (void) contentSharingPicker:(SCContentSharingPicker *) picker didCancelForStream:(SCStream *) stream;
```

## Parameters

- `picker`: The content-sharing picker that sent this event.
- `stream`: The canceled stream, if any.

## See Also

### Observing events
- [func contentSharingPicker(SCContentSharingPicker, didUpdateWith: SCContentFilter, for: SCStream?)](./contentsharingpicker%28_,didupdatewith,for%29.md)
  Tells the observer that a sharing picker updated the content filter for a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerobserver/contentsharingpicker(_:didcancelfor:))*