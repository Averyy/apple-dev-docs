# providerIdentifier

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

A purpose identifier for coordinated reads and writes.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 8.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`NSFileProviderManager`](../nsfileprovidermanager.md) class’s [`providerIdentifier`](../nsfileprovidermanager/provideridentifier.md) method instead.

## Declaration

```swift
var providerIdentifier: String { get }
```

```objc
@property (nonatomic, readonly) NSString * providerIdentifier;
```

#### Discussion

This property contains a unique string that can be used as a purpose identifier for file coordination. The File Provider extension should use this identifier when performing coordinated reads and writes, to help prevent deadlocks.

Pass this identifier to the file coordinator’s `setPurposeIdentifier:` method before performing a coordinated read or write.

This method returns the containing app’s bundle identifier.

## See Also

### Accessing the document storage
- [var documentStorageURL: URL](./documentstorageurl.md)
  The root URL for all shared documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/provideridentifier)*