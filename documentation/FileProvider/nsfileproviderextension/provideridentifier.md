# providerIdentifier

**Framework**: File Provider  
**Kind**: property

A purpose identifier for coordinated reads and writes.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
var providerIdentifier: String { get }
```

#### Discussion

This property contains a unique string that can be used as a purpose identifier for file coordination. The File Provider extension should use this identifier when performing coordinated reads and writes, to help prevent deadlocks.

Pass this identifier to the file coordinator’s `setPurposeIdentifier:` method before performing a coordinated read or write.

This method returns the containing app’s bundle identifier.

## See Also

- [var documentStorageURL: URL](nsfileproviderextension/documentstorageurl.md)
  The root URL for all shared documents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/provideridentifier)*