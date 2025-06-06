# domain

**Framework**: File Provider  
**Kind**: property

The domain managed by this file provider object.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var domain: NSFileProviderDomain? { get }
```

#### Discussion

If the File Provider extension does not use domains, this property is set to `nil`. By default, a File Provider extension does not have any domains.

A new [`NSFileProviderExtension`](nsfileproviderextension.md) object is created for each domain added to the File Provider manager. The new File Provider’s [`domain`](nsfileproviderextension/domain.md) property is set to the added domain, and any items returned by the File Provider belong to that domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderextension/domain)*