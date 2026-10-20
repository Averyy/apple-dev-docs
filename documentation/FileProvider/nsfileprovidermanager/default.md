# default

**Framework**: File Provider  
**Kind**: property  
**Role**: Type Property

A property that returns the shared file provider manager object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+

## Declaration

```swift
class var `default`: NSFileProviderManager { get }
```

```objc
@property (class, strong, readonly) NSFileProviderManager * defaultManager;
```

#### Discussion

This property returns a manager for the default domain on iOS. You can access the default domain in both the containing app and the File Provider extension. On macOS, use an explicit domain by calling [`init(for:)`](./init%28for%29.md) instead.

## See Also

### Accessing File Provider data
- [var documentStorageURL: URL](./documentstorageurl.md)
  The root URL for all shared documents.
- [var providerIdentifier: String](./provideridentifier.md)
  A purpose identifier for coordinated reads and writes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermanager/default)*