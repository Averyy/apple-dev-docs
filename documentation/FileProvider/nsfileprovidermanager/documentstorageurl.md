# documentStorageURL

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

The root URL for all shared documents.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+

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

> **Note**:  While this property is available on macOS 11+, you don’t need to use it when creating a file provider extension that adopts the [`NSFileProviderReplicatedExtension`](../nsfileproviderreplicatedextension.md) protocol.

## See Also

### Accessing File Provider data
- [class var `default`: NSFileProviderManager](./default.md)
  A property that returns the shared file provider manager object.
- [var providerIdentifier: String](./provideridentifier.md)
  A purpose identifier for coordinated reads and writes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/documentstorageurl)*