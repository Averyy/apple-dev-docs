# getIdentifierForUserVisibleFile(at:completionHandler:)

**Framework**: File Provider  
**Kind**: method  
**Role**: Type Method

Returns the identifier and domain for a user-visible URL.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class func getIdentifierForUserVisibleFile(at url: URL, completionHandler: @escaping @Sendable (NSFileProviderItemIdentifier?, NSFileProviderDomainIdentifier?, (any Error)?) -> Void)
```

```swift
class func identifierForUserVisibleFile(at url: URL) async throws -> (NSFileProviderItemIdentifier, NSFileProviderDomainIdentifier)
```

```objc
+ (void) getIdentifierForUserVisibleFileAtURL:(NSURL *) url completionHandler:(void (^)(NSFileProviderItemIdentifier itemIdentifier, NSFileProviderDomainIdentifier domainIdentifier, NSError *error)) completionHandler;
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration:
>
> ```swift
> class func identifierForUserVisibleFile(at url: URL) async throws -> (NSFileProviderItemIdentifier, NSFileProviderDomainIdentifier)
> ```
>
> For information about concurrency and asynchronous code in Swift, see [Calling Objective-C APIs Asynchronously](../../Swift/calling-objective-c-apis-asynchronously.md).

If the URL doesn’t refer to an item managed by your File Provider extension, the system returns a [`NSFileNoSuchFileError`](../../Foundation/nsfilenosuchfileerror-swift.var.md) error.

## Parameters

- `url`: The URL of the item.
- `completionHandler`: A block that the system calls after it gets the items identifier. It has the following parameters:

  - **`itemIdentifier`**: The item’s identifier.
  - **`domainIdentifier`**: The identifier for the item’s domain.
  - **`error`**: If an error occurs, this object contains information about the error; otherwise, it’s `nil`.

## See Also

### Translating user-visible URLs
- [func getUserVisibleURL(for: NSFileProviderItemIdentifier, completionHandler: (URL?, (any Error)?) -> Void)](./getuservisibleurl%28for,completionhandler%29.md)
  Returns the user-visible URL for an item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/getidentifierforuservisiblefile(at:completionhandler:))*