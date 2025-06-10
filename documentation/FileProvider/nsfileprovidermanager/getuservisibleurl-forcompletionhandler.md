# getUserVisibleURL(for:completionHandler:)

**Framework**: File Provider  
**Kind**: method

Returns the user-visible URL for an item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func getUserVisibleURL(for itemIdentifier: NSFileProviderItemIdentifier) async throws -> URL
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
func getUserVisibleURL(for itemIdentifier: NSFileProviderItemIdentifier) async throws -> URL
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Calling this method marks the process so that accessing the URL won’t materialize the item. Instead, any attempt to read or write to an unmaterialized item fails with a [`EDEADLK`](https://developer.apple.com/documentation/Foundation/POSIXError/EDEADLK) POSIX error.

## Parameters

- `itemIdentifier`: The item’s identifier.
- `completionHandler`: A block that the system calls after determining the item’s URL. The system passes the following parameters:

## See Also

- [class func getIdentifierForUserVisibleFile(at: URL, completionHandler: (NSFileProviderItemIdentifier?, NSFileProviderDomainIdentifier?, (any Error)?) -> Void)](nsfileprovidermanager/getidentifierforuservisiblefile(at:completionhandler:).md)
  Returns the identifier and domain for a user-visible URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/getuservisibleurl(for:completionhandler:))*