# willTerminate()

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Called by the host before suspending or terminating the extension process. Extension clients should use this to stop any in-progress work. When the extension is activated again, a new call will be made by the host.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+

## Declaration

```swift
func willTerminate() async
```

## Mentions

- [Uploading asset resources in the background](../../PhotoKit/uploading-asset-resources-in-the-background.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phbackgroundresourceuploadjobextension/willterminate())*