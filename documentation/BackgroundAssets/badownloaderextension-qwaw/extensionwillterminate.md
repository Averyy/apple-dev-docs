# extensionWillTerminate()

**Framework**: Background Assets  
**Kind**: method  
**Required**: Yes

This method may be called shortly before the extension is terminated.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 18.4+
- visionOS 2.4+

## Declaration

```swift
func extensionWillTerminate()
```

#### Discussion

This method is invoked if all extension callbacks have returned or if the extension has run over it’s alotted runtime. This callback provides a last chance to tidy up state before process termination.

> ⚠️ **Warning**: This method is advisory only, there will be instances where the extension is terminated before this method is invoked. Do not rely on this method being invoked before the extension is terminated.

This method is advisory only, there will be instances where the extension is terminated before this method is invoked. Do not rely on this method being invoked before the extension is terminated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/backgroundassets/badownloaderextension-qwaw/extensionwillterminate())*