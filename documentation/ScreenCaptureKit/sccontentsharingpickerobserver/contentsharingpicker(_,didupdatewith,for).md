# contentSharingPicker(_:didUpdateWith:for:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Tells the observer that a sharing picker updated the content filter for a stream.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 18.2+
- macOS 14.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func contentSharingPicker(_ picker: SCContentSharingPicker, didUpdateWith filter: SCContentFilter, for stream: SCStream?)
```

```objc
- (void) contentSharingPicker:(SCContentSharingPicker *) picker didUpdateWithFilter:(SCContentFilter *) filter forStream:(SCStream *) stream;
```

## Parameters

- `picker`: The content-sharing picker that sent this event.
- `filter`: The new filter applied to streaming content.
- `stream`: The changed stream, if any.

## See Also

### Observing events
- [func contentSharingPicker(SCContentSharingPicker, didCancelFor: SCStream?)](./contentsharingpicker%28_,didcancelfor%29.md)
  Tells the observer that a sharing picker canceled selection for a stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/sccontentsharingpickerobserver/contentsharingpicker(_:didupdatewith:for:))*