# stopProvidingItem(at:)

**Framework**: File Provider  
**Kind**: method

Tells the File Provider extension that a given document is no longer being accessed.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
func stopProvidingItem(at url: URL)
```

#### Discussion

The system calls this method as soon as all other processes have stopped accessing the given file. You can override this method to remove the document from the local file system, thus freeing up storage space. You must provide placeholders for any documents you remove.

You must override this method, even if you only provide an empty implementation. Do not call `super` in your implementations.

## Parameters

- `url`: The URL of a shared document.

## See Also

- [func itemChanged(at: URL)](nsfileproviderextension/itemchanged(at:).md)
  Tells the File Provider extension that a document has changed.
- [func providePlaceholder(at: URL, completionHandler: ((any Error)?) -> Void)](nsfileproviderextension/provideplaceholder(at:completionhandler:).md)
  Triggers the creation of a placeholder for the given URL.
- [func startProvidingItem(at: URL, completionHandler: ((any Error)?) -> Void)](nsfileproviderextension/startprovidingitem(at:completionhandler:).md)
  Provides an actual file on disk for a placeholder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/stopprovidingitem(at:))*