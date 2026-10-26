# notifyTermination()

**Framework**: Photos  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

This notification will be called if the host is going to suspend/terminate the current execution. Extension clients should use this to stop the current execution. When the extension is activated, a new call will be presented by the host.

**Availability**:
- iOS 26.1+ - Deprecated in 27.0
- iPadOS 26.1+ - Deprecated in 27.0

> **Deprecated**: Adopt PHBackgroundResourceUploadJobExtension instead

## Declaration

```swift
func notifyTermination()
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/photos/phbackgroundresourceuploadextension/notifytermination())*