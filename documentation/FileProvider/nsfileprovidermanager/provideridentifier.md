# providerIdentifier

**Framework**: Fileprovider  
**Kind**: property

A purpose identifier for coordinated reads and writes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var providerIdentifier: String { get }
```

#### Discussion

This property contains a unique string that can be used as a purpose identifier for file coordination. The File Provider extension should use this identifier when performing coordinated reads and writes, to help prevent deadlocks.

Pass this identifier to the file coordinator’s `setPurposeIdentifier:` method before performing a coordinated read or write.

This method returns the containing app’s bundle identifier.

> **Note**:  While this property is available on macOS 11+, you don’t need to use it when creating a file provider extension that adopts the [`NSFileProviderReplicatedExtension`](nsfileproviderreplicatedextension.md) protocol.

## See Also

- [class var `default`: NSFileProviderManager](nsfileprovidermanager/default.md)
  A property that returns the shared file provider manager object.
- [var documentStorageURL: URL](nsfileprovidermanager/documentstorageurl.md)
  The root URL for all shared documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/FileProvider/nsfileprovidermanager/provideridentifier)*