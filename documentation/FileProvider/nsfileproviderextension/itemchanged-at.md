# itemChanged(at:)

**Framework**: File Provider  
**Kind**: method

Tells the File Provider extension that a document has changed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
func itemChanged(at url: URL)
```

#### Discussion

The system calls this method when a shared file’s content changes, typically in response to coordinated writes from the host app.

You must override this method and respond to these changes. Do not call `super` in your implementations.

In your implementation, defer all networking, asynchronous, or long-running operations to background tasks. For networking tasks, create a background [`URLSession`](https://developer.apple.com/documentation/Foundation/URLSession) task, and then register the task with the file provider manager by calling the manager’s [`register(_:forItemWithIdentifier:completionHandler:)`](nsfileprovidermanager/register(_:foritemwithidentifier:completionhandler:).md) method.

## Parameters

- `url`: The URL of a shared document.

## See Also

- [func providePlaceholder(at: URL, completionHandler: ((any Error)?) -> Void)](nsfileproviderextension/provideplaceholder(at:completionhandler:).md)
  Triggers the creation of a placeholder for the given URL.
- [func startProvidingItem(at: URL, completionHandler: ((any Error)?) -> Void)](nsfileproviderextension/startprovidingitem(at:completionhandler:).md)
  Provides an actual file on disk for a placeholder.
- [func stopProvidingItem(at: URL)](nsfileproviderextension/stopprovidingitem(at:).md)
  Tells the File Provider extension that a given document is no longer being accessed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/itemchanged(at:))*