# renderingProcessWithInterruptionHandler:completion:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Type Method

Launches a rendering extension process asynchronously.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```objc
+ (void) renderingProcessWithInterruptionHandler:(void (^)()) interruptionHandler completion:(void (^)(BERenderingProcess *process, NSError *error)) completion;
```

#### Discussion

Your browser app can run one instance of each of its rendering extensions. The first time you call this method, the system launches your rendering extension. If you subsequently call this method, or you call [`renderingProcessWithBundleID:interruptionHandler:completion:`](./renderingprocesswithbundleid_interruptionhandler_completion_.md) with `nil` as the bundle identifier, your completion handler gets a reference to the same process.

The system guarantees that the process launched when it calls your completion handler.

This method is equivalent to calling [`renderingProcessWithBundleID:interruptionHandler:completion:`](./renderingprocesswithbundleid_interruptionhandler_completion_.md), passing `nil` as the bundle identifier.

## Parameters

- `interruptionHandler`: A block the system calls if the rendering extension process exits abnormally.
- `completion`: A block the system calls when the process finishes launching.

## See Also

### Creating and invalidating extension processes
- [+ renderingProcessWithBundleID:interruptionHandler:completion:](./renderingprocesswithbundleid_interruptionhandler_completion_.md)
  Launches a rendering extension process asynchronously.
- [- invalidate](./invalidate.md)
  Stops the rendering process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berenderingprocess/renderingprocesswithinterruptionhandler:completion:)*