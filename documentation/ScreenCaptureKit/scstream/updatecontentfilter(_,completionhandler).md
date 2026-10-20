# updateContentFilter(_:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method

Updates the stream by applying a new content filter.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
func updateContentFilter(_ contentFilter: SCContentFilter, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func updateContentFilter(_ contentFilter: SCContentFilter) async throws
```

```objc
- (void) updateContentFilter:(SCContentFilter *) contentFilter completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `contentFilter`: The content filter to apply.
- `completionHandler`: A completion handler the system calls when this method completes. It includes an error if the update fails.

## See Also

### Updating stream configuration
- [func updateConfiguration(SCStreamConfiguration, completionHandler: (((any Error)?) -> Void)?)](./updateconfiguration%28_,completionhandler%29.md)
  Updates the stream with a new configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/updatecontentfilter(_:completionhandler:))*