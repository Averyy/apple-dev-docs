# webContentProcessWithInterruptionHandler:completion:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Type Method

Launches a web content extension process asynchronously.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.3+

## Declaration

```objc
+ (void) webContentProcessWithInterruptionHandler:(void (^)()) interruptionHandler completion:(void (^)(BEWebContentProcess *process, NSError *error)) completion;
```

#### Discussion

Your browser app can run multiple web content extension processes.

The system guarantees that the process launched when it calls your completion handler.

This method is equivalent to calling [`webContentProcessWithBundleID:interruptionHandler:completion:`](./webcontentprocesswithbundleid_interruptionhandler_completion_.md), passing `nil` as the bundle identifier.

## Parameters

- `interruptionHandler`: A block the system calls if the web content extension process exits abnormally.
- `completion`: A block the system calls when the process finishes launching.

## See Also

### Creating and invalidating extension processes
- [+ webContentProcessWithBundleID:interruptionHandler:completion:](./webcontentprocesswithbundleid_interruptionhandler_completion_.md)
  Launches a web content extension process asynchronously.
- [- invalidate](./invalidate.md)
  Stops the web content process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentprocess/webcontentprocesswithinterruptionhandler:completion:)*