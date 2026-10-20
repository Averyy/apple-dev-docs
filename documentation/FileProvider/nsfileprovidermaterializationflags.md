# NSFileProviderMaterializationFlags

**Framework**: File Provider  
**Kind**: struct  
**Role**: Structure

Flags that provides additional information about the provided content.

**Availability**:
- macOS 12.3+

## Declaration

```swift
struct NSFileProviderMaterializationFlags
```

```c
enum NSFileProviderMaterializationFlags : NSUInteger;
```

## Topics

### Accessing Flags
- [static var knownSparseRanges: NSFileProviderMaterializationFlags](./nsfileprovidermaterializationflags/knownsparseranges.md)
  A flag indicating that the system should consider the file fully materialized, even if it’s a sparse file.
### Creating Flags
- [init(rawValue: UInt)](./nsfileprovidermaterializationflags/init%28rawvalue%29.md)
  Creates a new materialization flag.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Fetching Ranges from a File
- [func fetchPartialContents(for: NSFileProviderItemIdentifier, version: NSFileProviderItemVersion, request: NSFileProviderRequest, minimalRange: NSRange, aligningTo: Int, options: NSFileProviderFetchContentsOptions, completionHandler: (URL?, NSFileProviderItem?, NSRange, NSFileProviderMaterializationFlags, (any Error)?) -> Void) -> Progress](./nsfileproviderpartialcontentfetching/fetchpartialcontents%28for,version,request,minimalrange,aligningto,options,completionhandler%29.md)
  Tells the file provider to download the requested item from remote storage.
- [struct NSFileProviderFetchContentsOptions](./nsfileproviderfetchcontentsoptions.md)
  Options for fetching a range of data from a file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidermaterializationflags)*