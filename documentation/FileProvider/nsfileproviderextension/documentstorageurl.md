# documentStorageURL

**Framework**: File Provider  
**Kind**: property

The root URL for all shared documents.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- visionOS 1.0+

## Declaration

```swift
var documentStorageURL: URL { get }
```

#### Discussion

This property contains the URL `<container URL>/File Provider Storage`, where  is the value returned by the [`containerURL(forSecurityApplicationGroupIdentifier:)`](https://developer.apple.com/documentation/Foundation/FileManager/containerURL(forSecurityApplicationGroupIdentifier:)) method.

The container URL refers to an app group container directory used by the `NSFileProviderExtension` extension. You can specify this shared container using the `NSExtensionFileProviderDocumentGroup` key in the File Provider extension’s `info.plist` file.

## See Also

- [var providerIdentifier: String](nsfileproviderextension/provideridentifier.md)
  A purpose identifier for coordinated reads and writes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/documentstorageurl)*