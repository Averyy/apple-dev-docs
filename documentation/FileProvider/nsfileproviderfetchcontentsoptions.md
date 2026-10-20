# NSFileProviderFetchContentsOptions

**Framework**: File Provider  
**Kind**: struct  
**Role**: Structure

Options for fetching a range of data from a file.

**Availability**:
- macOS 12.3+

## Declaration

```swift
struct NSFileProviderFetchContentsOptions
```

```c
enum NSFileProviderFetchContentsOptions : NSUInteger;
```

## Topics

### Accessing Options
- [static var strictVersioning: NSFileProviderFetchContentsOptions](./nsfileproviderfetchcontentsoptions/strictversioning.md)
  An option that indicates the system requires an exact match of the requested item’s version.
### Creating Options
- [init(rawValue: UInt)](./nsfileproviderfetchcontentsoptions/init%28rawvalue%29.md)
  Creates an option instance from the raw value.

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
- [struct NSFileProviderMaterializationFlags](./nsfileprovidermaterializationflags.md)
  Flags that provides additional information about the provided content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileproviderfetchcontentsoptions)*