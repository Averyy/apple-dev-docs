# invalidate()

**Framework**: BrowserEngineKit  
**Kind**: method

Stops the web content process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
func invalidate()
```

#### Discussion

The system halts the web content process for your browser app when you call this function. In platform versions earlier than iOS 18, the system marks the web content process as no longer in use, and might stop it at a later time to free its resources. The system doesn’t call the interruption handler that you passed when you launched the extension.

After you call this method, other method calls on the web content process throw errors.

## See Also

- [init(bundleIdentifier: String?, onInterruption: () -> Void) async throws](webcontentprocess/init(bundleidentifier:oninterruption:).md)
  Launches a web content process asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/webcontentprocess/invalidate())*