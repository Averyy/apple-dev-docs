# documentStorageURL

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

The root URL for all shared documents.

**Availability**:
- iOS 8.0+ - Deprecated in 11.0
- iPadOS 8.0+ - Deprecated in 11.0
- Mac Catalyst 8.0+ - Deprecated in 11.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`NSFileProviderManager`](../nsfileprovidermanager.md) class’s [`documentStorageURL`](../nsfileprovidermanager/documentstorageurl.md) method instead.

## Declaration

```swift
var documentStorageURL: URL { get }
```

```objc
@property (nonatomic, readonly) NSURL * documentStorageURL;
```

## Discussion

This property contains the URL `<container URL>/File Provider Storage`, where *container URL* is the value returned by the [`containerURL(forSecurityApplicationGroupIdentifier:)`](../../Foundation/filemanager/containerurl%28forsecurityapplicationgroupidentifier%29.md) method.

The container URL refers to an app group container directory used by the `NSFileProviderExtension` extension. You can specify this shared container using the `NSExtensionFileProviderDocumentGroup` key in the File Provider extension’s `info.plist` file.

## See Also

### Accessing the document storage
- [var providerIdentifier: String](./provideridentifier.md)
  A purpose identifier for coordinated reads and writes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/documentstorageurl)*