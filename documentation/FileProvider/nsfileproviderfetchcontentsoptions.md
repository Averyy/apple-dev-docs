# NSFileProviderFetchContentsOptions

**Framework**: File Provider  
**Kind**: struct

Options for fetching a range of data from a file.

**Availability**:
- macOS 12.3+

## Declaration

```swift
struct NSFileProviderFetchContentsOptions
```

## Topics

### Accessing Options
- [static var strictVersioning: NSFileProviderFetchContentsOptions](nsfileproviderfetchcontentsoptions/strictversioning.md)
  An option that indicates the system requires an exact match of the requested item’s version.
### Creating Options
- [init(rawValue: UInt)](nsfileproviderfetchcontentsoptions/init(rawvalue:).md)
  Creates an option instance from the raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func fetchPartialContents(for: NSFileProviderItemIdentifier, version: NSFileProviderItemVersion, request: NSFileProviderRequest, minimalRange: NSRange, aligningTo: Int, options: NSFileProviderFetchContentsOptions, completionHandler: (URL?, NSFileProviderItem?, NSRange, NSFileProviderMaterializationFlags, (any Error)?) -> Void) -> Progress](nsfileproviderpartialcontentfetching/fetchpartialcontents(for:version:request:minimalrange:aligningto:options:completionhandler:).md)
  Tells the file provider to download the requested item from remote storage.
- [struct NSFileProviderMaterializationFlags](nsfileprovidermaterializationflags.md)
  Flags that provides additional information about the provided content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderfetchcontentsoptions)*