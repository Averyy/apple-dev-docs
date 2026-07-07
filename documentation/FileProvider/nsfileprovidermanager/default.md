# default

**Framework**: File Provider  
**Kind**: property

A property that returns the shared file provider manager object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class var `default`: NSFileProviderManager { get }
```

#### Discussion

This property returns a manager for the default domain on iOS. You can access the default domain in both the containing app and the File Provider extension. On macOS, use an explicit domain by calling [`init(for:)`](nsfileprovidermanager/init(for:).md) instead.

## See Also

- [var documentStorageURL: URL](nsfileprovidermanager/documentstorageurl.md)
  The root URL for all shared documents.
- [var providerIdentifier: String](nsfileprovidermanager/provideridentifier.md)
  A purpose identifier for coordinated reads and writes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/default)*