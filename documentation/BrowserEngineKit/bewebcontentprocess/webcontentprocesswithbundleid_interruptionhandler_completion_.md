# webContentProcessWithBundleID:interruptionHandler:completion:

**Framework**: BrowserEngineKit  
**Kind**: method  
**Role**: Type Method

Launches a web content extension process asynchronously.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- macOS 14.3+

## Declaration

```objc
+ (void) webContentProcessWithBundleID:(NSString *) bundleID interruptionHandler:(void (^)()) interruptionHandler completion:(void (^)(BEWebContentProcess *process, NSError *error)) completion;
```

#### Discussion

Your browser app can run multiple web content extension processes.

The system guarantees that the process launched when it calls your completion handler.

## Parameters

- `bundleID`: The bundle identifier of the web content extension to launch, or `nil` to use the default bundle identifier for this app’s web content extension.
- `interruptionHandler`: A block the system calls if the web content extension process exits abnormally.
- `completion`: A block the system calls when the process finishes launching.

## See Also

### Creating and invalidating extension processes
- [+ webContentProcessWithInterruptionHandler:completion:](./webcontentprocesswithinterruptionhandler_completion_.md)
  Launches a web content extension process asynchronously.
- [- invalidate](./invalidate.md)
  Stops the web content process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bewebcontentprocess/webcontentprocesswithbundleid:interruptionhandler:completion:)*