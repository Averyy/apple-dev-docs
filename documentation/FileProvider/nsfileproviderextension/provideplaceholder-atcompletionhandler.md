# providePlaceholder(at:completionHandler:)

**Framework**: File Provider  
**Kind**: method

Triggers the creation of a placeholder for the given URL.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
func providePlaceholder(at url: URL) async throws
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func providePlaceholder(at url: URL) async throws
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
func providePlaceholder(at url: URL) async throws
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

The system calls this method when it needs a placeholder for a document that’s returned by the File Provider extension, but is not stored locally. Override `providePlaceholder(at:completionHandler:)` to create a placeholder for the given URL. This task can be broken into three steps: looking up the document’s file provider item, writing the placeholder, and calling the completion handler.

> ❗ **Important**:  Both the [`providePlaceholder(at:completionHandler:)`](nsfileproviderextension/provideplaceholder(at:completionhandler:).md) and [`startProvidingItem(at:completionHandler:)`](nsfileproviderextension/startprovidingitem(at:completionhandler:).md) methods can be triggered as other processes attempt to access documents provided by the File Provider extension. These methods may be called in response to user interaction with the document browser, or due to a coordinated read or coordinated write of the document’s URL. Exactly which methods are triggered, and their sequence, depends on the type of coordinated access. For example, a coordinated read using the `NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly` option triggers only the creation of a placeholder. As a result, your extension should not create dependencies between these methods. They may be called in any order.

 Both the [`providePlaceholder(at:completionHandler:)`](nsfileproviderextension/provideplaceholder(at:completionhandler:).md) and [`startProvidingItem(at:completionHandler:)`](nsfileproviderextension/startprovidingitem(at:completionhandler:).md) methods can be triggered as other processes attempt to access documents provided by the File Provider extension. These methods may be called in response to user interaction with the document browser, or due to a coordinated read or coordinated write of the document’s URL.

Exactly which methods are triggered, and their sequence, depends on the type of coordinated access. For example, a coordinated read using the `NSFileCoordinatorReadingImmediatelyAvailableMetadataOnly` option triggers only the creation of a placeholder. As a result, your extension should not create dependencies between these methods. They may be called in any order.

##### Look Up the Documents File Provider Item

1. Get the document’s persistent identifier by calling [`persistentIdentifierForItem(at:)`](nsfileproviderextension/persistentidentifierforitem(at:).md), and pass in the value of the `url` parameter.
2. Call [`item(for:)`](nsfileproviderextension/item(for:).md), and pass in the persistent identifier. This method returns the file provider item for the document.

##### Write the Placeholder

1. Get the placeholder URL by calling [`placeholderURL(for:)`](nsfileprovidermanager/placeholderurl(for:).md), and pass in the value of the url parameter.
2. Call [`writePlaceholder(at:withMetadata:)`](nsfileprovidermanager/writeplaceholder(at:withmetadata:).md), and pass in the placeholder URL and the file provider item.

##### Call the Completion Handler

After writing the placeholder to disk, call the completion handler. If any errors occur, pass them to the completion handler. The system then passes the error back to the original coordinated read or write.

##### Sample Implementation

```swift
override func providePlaceholder(at url: URL, completionHandler: @escaping (Error?) -> Void) {
    
    guard let identifier = persistentIdentifierForItem(at: url) else {
        completionHandler(NSFileProviderError(.noSuchItem))
        return
    }
    
    do {
        let fileProviderItem = try item(for: identifier)
        
        let placeholderURL = NSFileProviderManager.placeholderURL(for: url)
        try NSFileProviderManager.writePlaceholder(at: placeholderURL,
                                                   withMetadata: fileProviderItem)
        
        completionHandler(nil)
    }
    catch let error {
        completionHandler(error)
    }
}
```

## Parameters

- `url`: The URL of a shared document.
- `completionHandler`: The completion handler takes the following parameter:

## See Also

- [func itemChanged(at: URL)](nsfileproviderextension/itemchanged(at:).md)
  Tells the File Provider extension that a document has changed.
- [func startProvidingItem(at: URL, completionHandler: ((any Error)?) -> Void)](nsfileproviderextension/startprovidingitem(at:completionhandler:).md)
  Provides an actual file on disk for a placeholder.
- [func stopProvidingItem(at: URL)](nsfileproviderextension/stopprovidingitem(at:).md)
  Tells the File Provider extension that a given document is no longer being accessed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/provideplaceholder(at:completionhandler:))*