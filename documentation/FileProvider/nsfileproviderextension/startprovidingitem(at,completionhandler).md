# startProvidingItem(at:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Instance Method

Provides an actual file on disk for a placeholder.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- visionOS 1.0+

## Declaration

```swift
func startProvidingItem(at url: URL, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func startProvidingItem(at url: URL) async throws
```

```objc
- (void) startProvidingItemAtURL:(NSURL *) url completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> func startProvidingItem(at url: URL) async throws
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

This method is called whenever another process tries to access a placeholder for a shared document.

Override this method to download, create, or otherwise provide the file. As soon as the file is available, call the provided completion handler. If any errors occur during this process, pass the error to the completion handler. The system then passes the error back to the original coordinated read or write.

You must override this method. Do not call `super` in your implementations.

> **Note**:  Do not use file coordination inside this method. The system already guarantees that no other process can access the file while this method is executing.

## Parameters

- `url`: The URL of a shared document.
- `completionHandler`: A block to be called as soon as the file is available.

  The completion handler takes the following parameter:

  - **error**: If the document was produced, this value is `nil`. Otherwise, it holds an `NSError` object describing the error.

## See Also

### Managing shared files
- [func itemChanged(at: URL)](./itemchanged%28at%29.md)
  Tells the File Provider extension that a document has changed.
- [func providePlaceholder(at: URL, completionHandler: ((any Error)?) -> Void)](./provideplaceholder%28at,completionhandler%29.md)
  Triggers the creation of a placeholder for the given URL.
- [func stopProvidingItem(at: URL)](./stopprovidingitem%28at%29.md)
  Tells the File Provider extension that a given document is no longer being accessed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/startprovidingitem(at:completionhandler:))*