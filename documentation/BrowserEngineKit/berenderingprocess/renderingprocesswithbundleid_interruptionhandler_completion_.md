# renderingProcessWithBundleID:interruptionHandler:completion:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Type Method

Launches a rendering extension process asynchronously.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS 14.3+

## Declaration

```objc
+ (void) renderingProcessWithBundleID:(NSString *) bundleID interruptionHandler:(void (^)()) interruptionHandler completion:(void (^)(BERenderingProcess *process, NSError *error)) completion;
```

#### Discussion

Your browser app can run one instance of each of its rendering extensions. The first time you call this method, the system launches your rendering extension. If you subsequently call this method with the same bundle identifier, or you call [`renderingProcessWithInterruptionHandler:completion:`](./renderingprocesswithinterruptionhandler_completion_.md) after previously calling this method with `nil` as the bundle identifier, your completion handler gets a reference to the same process.

The system guarantees that the process launched when it calls your completion handler.

## Parameters

- `bundleID`: The bundle identifier of the rendering extension to launch, or `nil` to use the default bundle identifier for this app’s rendering extension.
- `interruptionHandler`: A block the system calls if the rendering extension process exits abnormally.
- `completion`: A block the system calls when the process finishes launching.

## See Also

### Creating and invalidating extension processes
- [+ renderingProcessWithInterruptionHandler:completion:](./renderingprocesswithinterruptionhandler_completion_.md)
  Launches a rendering extension process asynchronously.
- [- invalidate](./invalidate.md)
  Stops the rendering process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/berenderingprocess/renderingprocesswithbundleid:interruptionhandler:completion:)*