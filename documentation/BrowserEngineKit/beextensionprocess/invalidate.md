# invalidate()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Required**: Yes

Stops the extension process.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+

## Declaration

```swift
func invalidate()
```

#### Discussion

When you call this method, you tell the system your app no longer needs this extension process. If this is the last connection from the host process to the extension process, the system terminates the extension process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/beextensionprocess/invalidate())*