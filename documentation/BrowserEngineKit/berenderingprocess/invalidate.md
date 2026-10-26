# invalidate

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Instance Method

Stops the rendering process.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```objc
- (void) invalidate;
```

#### Discussion

The system halts the rendering extension process for your browser app when you call this function. In platform versions earlier than iOS 18, the system marks the rendering process as no longer in use, and might stop it at a later time to free its resources. The system doesn’t call the interruption handler you pass when you launched the extension.

After you call this method, other method calls on the rendering process throw errors.

## See Also

### Creating and invalidating extension processes
- [+ renderingProcessWithBundleID:interruptionHandler:completion:](./renderingprocesswithbundleid_interruptionhandler_completion_.md)
  Launches a rendering extension process asynchronously.
- [+ renderingProcessWithInterruptionHandler:completion:](./renderingprocesswithinterruptionhandler_completion_.md)
  Launches a rendering extension process asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berenderingprocess/invalidate)*