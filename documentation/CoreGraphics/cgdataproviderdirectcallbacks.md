# CGDataProviderDirectCallbacks

**Framework**: Core Graphics  
**Kind**: struct

Defines pointers to client-defined callback functions that manage the sending of data for a direct-access data provider.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CGDataProviderDirectCallbacks
```

#### Overview

You supply a [`CGDataProviderDirectCallbacks`](cgdataproviderdirectcallbacks.md) structure to the function [`init(directInfo:size:callbacks:)`](cgdataprovider/init(directinfo:size:callbacks:).md) to create a data provider for direct access. The functions specified by the [`CGDataProviderDirectCallbacks`](cgdataproviderdirectcallbacks.md) structure are responsible for copying data a block at a time to a memory buffer for Core Graphics to use. The functions are also responsible for handling the data provider’s basic memory management. For the callback to work, one of the `getBytePointer` and `getBytesAtPosition` parameters must be non-`NULL`. If both are non-`NULL`, then `getBytePointer` is used to access the data.

## Topics

### Initializers
- [init()](cgdataproviderdirectcallbacks/init.md)
- [init(version: UInt32, getBytePointer: CGDataProviderGetBytePointerCallback?, releaseBytePointer: CGDataProviderReleaseBytePointerCallback?, getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback?, releaseInfo: CGDataProviderReleaseInfoCallback?)](cgdataproviderdirectcallbacks/init(version:getbytepointer:releasebytepointer:getbytesatposition:releaseinfo:).md)
### Instance Properties
- [var getBytePointer: CGDataProviderGetBytePointerCallback?](cgdataproviderdirectcallbacks/getbytepointer.md)
  A pointer to a function that returns a pointer to the provider’s data. For more information, see [`CGDataProviderGetBytePointerCallback`](cgdataprovidergetbytepointercallback.md).
- [var getBytesAtPosition: CGDataProviderGetBytesAtPositionCallback?](cgdataproviderdirectcallbacks/getbytesatposition.md)
  A pointer to a function that copies data from the provider.
- [var releaseBytePointer: CGDataProviderReleaseBytePointerCallback?](cgdataproviderdirectcallbacks/releasebytepointer.md)
  A pointer to a function that Core Graphics calls to release a pointer to the provider’s data. For more information, see [`CGDataProviderReleaseBytePointerCallback`](cgdataproviderreleasebytepointercallback.md).
- [var releaseInfo: CGDataProviderReleaseInfoCallback?](cgdataproviderdirectcallbacks/releaseinfo.md)
  A pointer to a function that handles clean-up for the data provider, or `NULL`. For more information, see [`CGDataProviderReleaseInfoCallback`](cgdataproviderreleaseinfocallback.md).
- [var version: UInt32](cgdataproviderdirectcallbacks/version.md)
  The version of this structure. It should be set to 0.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init?(directInfo: UnsafeMutableRawPointer?, size: off_t, callbacks: UnsafePointer<CGDataProviderDirectCallbacks>)](cgdataprovider/init(directinfo:size:callbacks:).md)
  Creates a direct-access data provider.
- [init?(data: CFData)](cgdataprovider/init(data:).md)
  Creates a data provider that reads from a CFData object.
- [init?(url: CFURL)](cgdataprovider/init(url:).md)
  Creates a direct-access data provider that uses a URL to supply data.
- [init?(dataInfo: UnsafeMutableRawPointer?, data: UnsafeRawPointer, size: Int, releaseData: CGDataProviderReleaseDataCallback)](cgdataprovider/init(datainfo:data:size:releasedata:).md)
  Creates a direct-access data provider that uses data your program supplies.
- [init?(filename: UnsafePointer<CChar>)](cgdataprovider/init(filename:).md)
  Creates a direct-access data provider that uses a file to supply data.
- [typealias CGDataProviderGetBytePointerCallback](cgdataprovidergetbytepointercallback.md)
  A callback function that returns a generic pointer to the provider data.
- [typealias CGDataProviderGetBytesAtPositionCallback](cgdataprovidergetbytesatpositioncallback.md)
  A callback function that copies data from the provider into a Core Graphics buffer.
- [typealias CGDataProviderReleaseBytePointerCallback](cgdataproviderreleasebytepointercallback.md)
  A callback function that releases the pointer Core Graphics obtained by calling [`CGDataProviderGetBytePointerCallback`](cgdataprovidergetbytepointercallback.md).
- [typealias CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md)
  A callback function that releases any private data or resources associated with the data provider.
- [typealias CGDataProviderReleaseDataCallback](cgdataproviderreleasedatacallback.md)
  A callback function that releases data you supply to the function [`init(dataInfo:data:size:releaseData:)`](cgdataprovider/init(datainfo:data:size:releasedata:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataproviderdirectcallbacks)*