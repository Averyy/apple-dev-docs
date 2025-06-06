# getIdentifierForUserVisibleFile(at:completionHandler:)

**Framework**: File Provider  
**Kind**: method

Returns the identifier and domain for a user-visible URL.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func identifierForUserVisibleFile(at url: URL) async throws -> (NSFileProviderItemIdentifier, NSFileProviderDomainIdentifier)
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func identifierForUserVisibleFile(at url: URL) async throws -> (NSFileProviderItemIdentifier, NSFileProviderDomainIdentifier)
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

 You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:

```swift
class func identifierForUserVisibleFile(at url: URL) async throws -> (NSFileProviderItemIdentifier, NSFileProviderDomainIdentifier)
```

For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

If the URL doesn’t refer to an item managed by your File Provider extension, the system returns a [`NSFileNoSuchFileError`](https://developer.apple.com/documentation/foundation/nsfilenosuchfileerror) error.

## Parameters

- `url`: The URL of the item.
- `completionHandler`: A block that the system calls after it gets the items identifier. It has the following parameters:

## See Also

- [func getUserVisibleURL(for: NSFileProviderItemIdentifier, completionHandler: (URL?, (any Error)?) -> Void)](nsfileprovidermanager/getuservisibleurl(for:completionhandler:).md)
  Returns the user-visible URL for an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/getidentifierforuservisiblefile(at:completionhandler:))*