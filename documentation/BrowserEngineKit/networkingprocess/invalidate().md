# invalidate()

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Stops the networking process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```swift
func invalidate()
```

#### Discussion

The system halts the networking process for your browser app when you call this function. In platform versions earlier than iOS 18, the system marks the networking process as no longer in use, and might stop it at a later time to free its resources. The system doesn’t call the interruption handler that you passed when you launched the extension.

After you call this method, other method calls on the networking process throw errors.

## See Also

### Creating and invalidating extension processes
- [init(bundleIdentifier: String?, onInterruption: () -> Void) async throws](./init%28bundleidentifier,oninterruption%29.md)
  Launches a networking extension process asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/networkingprocess/invalidate())*