# extensionWillTerminate()

**Framework**: Background Assets  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

This method may be called shortly before the extension is terminated.

**Availability**:
- iOS 16.1+ - Deprecated in 16.4
- iPadOS 16.1+ - Deprecated in 16.4
- Mac Catalyst 16.1+ - Deprecated in 16.4
- macOS 13.0+ - Deprecated in 13.3
- visionOS 2.4+ - Deprecated in 2.4

> **Deprecated**: extensionWillTerminate will not be invoked in all applicable circumstances and should not be relied upon.

## Declaration

```swift
func extensionWillTerminate()
```

## Discussion

This method is invoked if all extension callbacks have returned or if the extension has run over it’s alotted runtime. This callback provides a last chance to tidy up state before process termination.

> ⚠️ **Warning**: This method is advisory only, there will be instances where the extension is terminated before this method is invoked. Do not rely on this method being invoked before the extension is terminated.

## Default Implementations

### BADownloaderExtension Implementations
- [func extensionWillTerminate()](./extensionwillterminate%28%29-236ac.md)

## See Also

### Reacting to extension events
- [func extensionWillTerminate()](./extensionwillterminate%28%29-236ac.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw/extensionwillterminate())*