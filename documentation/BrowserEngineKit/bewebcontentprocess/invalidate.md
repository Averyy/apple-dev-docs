# invalidate

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Stops the web content process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```objc
- (void) invalidate;
```

#### Discussion

The system halts the web content process for your browser app when you call this function. In platform versions earlier than iOS 18, the system marks the web content process as no longer in use, and might stop it at a later time to free its resources. The system doesn’t call the interruption handler that you passed when you launched the extension.

After you call this method, other method calls on the web content process throw errors.

## See Also

### Creating and invalidating extension processes
- [+ webContentProcessWithBundleID:interruptionHandler:completion:](./webcontentprocesswithbundleid_interruptionhandler_completion_.md)
  Launches a web content extension process asynchronously.
- [+ webContentProcessWithInterruptionHandler:completion:](./webcontentprocesswithinterruptionhandler_completion_.md)
  Launches a web content extension process asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentprocess/invalidate)*