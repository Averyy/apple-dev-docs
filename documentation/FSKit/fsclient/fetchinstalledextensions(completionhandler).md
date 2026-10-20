# fetchInstalledExtensions(completionHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method

Asynchronously retrieves an list of installed file system modules.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func fetchInstalledExtensions(completionHandler: @escaping @Sendable ([FSModuleIdentity]?, (any Error)?) -> Void)
```

```swift
var installedExtensions: [FSModuleIdentity] { get async throws }
```

```objc
- (void) fetchInstalledExtensionsWithCompletionHandler:(void (^)(NSArray<FSModuleIdentity *> *, NSError *)) completionHandler;
```

#### Discussion

In Swift, you can either call this method and pass a completion handler closure, or get the value of the `installedExtensions` property with the `async` keyword.

## Parameters

- `completionHandler`: A block or closure that executes when FSKit finishes its fetch process. If the fetch succeeds, the first parameter contains an array of [`FSModuleIdentity`](../fsmoduleidentity.md) instances that identify installed modules. If the fetch fails, the second parameter contains an error detailing the failure.

## See Also

### Discovering installed extensions
- [class FSModuleIdentity](../fsmoduleidentity.md)
  An installed file system module.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsclient/fetchinstalledextensions(completionhandler:))*