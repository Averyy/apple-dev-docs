# enumerator(for:request:)

**Framework**: File Provider  
**Kind**: method  
**Required**: Yes

Tells the file provider to return an enumerator for the provided directory.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func enumerator(for containerItemIdentifier: NSFileProviderItemIdentifier, request: NSFileProviderRequest) throws -> any NSFileProviderEnumerator
```

## Mentions

- [Synchronizing the File Provider Extension](synchronizing-the-file-provider-extension.md)

#### Return Value

An enumerator for the specified directory.

#### Discussion

The system calls this method to request an enumerator for the specified item.

Possible item identifiers include:

Your implementation should create and return an [`NSFileProviderEnumerator`](nsfileproviderenumerator.md) object that provides the requested content.

##### Handle Errors

If you can’t return the requested enumerator, you must throw an error in Swift, or if you return nil in Objective-C, you must set the `error` out parameter.

If the `containerItemIdentifier` parameter is [`trashContainer`](nsfileprovideritemidentifier/trashcontainer.md) and your extension doesn’t support trashing items, then it should fail with the [`NSFeatureUnsupportedError`](https://developer.apple.com/documentation/Foundation/NSFeatureUnsupportedError-swift.var) error code from the [`NSCocoaErrorDomain`](https://developer.apple.com/documentation/Foundation/NSCocoaErrorDomain) domain. Additionally, make sure the items managed by your File Provider extension don’t have the [`allowsTrashing`](nsfileprovideritemcapabilities/allowstrashing.md) capability enabled.

If the `containerItemIdentifier` parameter doesn’t exist in your remote storage, you should fail with an [`NSFileProviderError.Code.noSuchItem`](nsfileprovidererror/code/nosuchitem.md) error. The system then attempts to delete the item from disk.

If you pass [`NSFileProviderError.Code.notAuthenticated`](nsfileprovidererror/code/notauthenticated.md) or [`NSFileProviderError.Code.serverUnreachable`](nsfileprovidererror/code/serverunreachable.md) to the handler, the system presents an appropriate alert to the user, but doesn’t try to access the metadata until triggered again by the user.

The system considers any other errors to be transient, and automatically retries the method call.

## Parameters

- `containerItemIdentifier`: The item identifier for the directory.
- `request`: An object that identifies the context of that request, such as the requesting app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderenumerating/enumerator(for:request:))*