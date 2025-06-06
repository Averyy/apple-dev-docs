# documentStorageURL

**Framework**: Fileprovider  
**Kind**: property

The root URL for all shared documents.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var documentStorageURL: URL { get }
```

#### Discussion

This property contains the URL `<container URL>/File Provider Storage`, where  is the value returned by the [`containerURL(forSecurityApplicationGroupIdentifier:)`](https://developer.apple.com/documentation/foundation/filemanager/1412643-containerurl) method.

The container URL refers to an app group container directory used by the `NSFileProviderExtension` extension. You can specify this shared container using the `NSExtensionFileProviderDocumentGroup` key in the File Provider extension’s `info.plist` file.

> **Note**:  While this property is available on macOS 11+, you don’t need to use it when creating a file provider extension that adopts the [`NSFileProviderReplicatedExtension`](nsfileproviderreplicatedextension.md) protocol.

## See Also

- [class var `default`: NSFileProviderManager](nsfileprovidermanager/default.md)
  A property that returns the shared file provider manager object.
- [var providerIdentifier: String](nsfileprovidermanager/provideridentifier.md)
  A purpose identifier for coordinated reads and writes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/FileProvider/nsfileprovidermanager/documentstorageurl)*