# updateConfiguration(_:completionHandler:)

**Framework**: ScreenCaptureKit  
**Kind**: method  
**Role**: Instance Method

Updates the stream with a new configuration.

**Availability**:
- Mac Catalyst 18.2+
- macOS 12.3+

## Declaration

```swift
func updateConfiguration(_ streamConfig: SCStreamConfiguration, completionHandler: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func updateConfiguration(_ streamConfig: SCStreamConfiguration) async throws
```

```objc
- (void) updateConfiguration:(SCStreamConfiguration *) streamConfig completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Parameters

- `streamConfig`: An object that provides the updated stream configuration.
- `completionHandler`: A completion handler the system calls when this method completes. It includes an error if the update fails.

## See Also

### Updating stream configuration
- [func updateContentFilter(SCContentFilter, completionHandler: (((any Error)?) -> Void)?)](./updatecontentfilter%28_,completionhandler%29.md)
  Updates the stream by applying a new content filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/screencapturekit/scstream/updateconfiguration(_:completionhandler:))*