# updateConfiguration(_:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method

Updates the stream with a new configuration.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
func updateConfiguration(_ streamConfig: SCStreamConfiguration) async throws
```

## Parameters

- `streamConfig`: An object that provides the updated stream configuration.
- `completionHandler`: A completion handler the system calls when this method completes. It includes an error if the update fails.

## See Also

- [func updateContentFilter(SCContentFilter, completionHandler: (((any Error)?) -> Void)?)](scstream/updatecontentfilter(_:completionhandler:).md)
  Updates the stream by applying a new content filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/updateconfiguration(_:completionhandler:))*