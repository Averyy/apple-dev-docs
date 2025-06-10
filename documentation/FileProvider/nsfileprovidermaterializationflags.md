# NSFileProviderMaterializationFlags

**Framework**: File Provider  
**Kind**: struct

Flags that provides additional information about the provided content.

**Availability**:
- macOS 12.3+

## Declaration

```swift
struct NSFileProviderMaterializationFlags
```

## Topics

### Accessing Flags
- [static var knownSparseRanges: NSFileProviderMaterializationFlags](nsfileprovidermaterializationflags/knownsparseranges.md)
  A flag indicating that the system should consider the file fully materialized, even if it’s a sparse file.
### Creating Flags
- [init(rawValue: UInt)](nsfileprovidermaterializationflags/init(rawvalue:).md)
  Creates a new materialization flag.

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
- [struct NSFileProviderFetchContentsOptions](nsfileproviderfetchcontentsoptions.md)
  Options for fetching a range of data from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermaterializationflags)*