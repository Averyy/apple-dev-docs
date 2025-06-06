# CGDataProviderSequentialCallbacks

**Framework**: Core Graphics  
**Kind**: struct

Defines a structure containing pointers to client-defined callback functions that manage the sending of data for a sequential-access data provider.

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
struct CGDataProviderSequentialCallbacks
```

#### Overview

The functions specified by the `CGDataProviderSequentialCallbacks` structure are responsible for sequentially copying data to a memory buffer for Core Graphics to use. The functions are also responsible for handling the data provider’s basic memory management. You supply a `CGDataProviderSequentialCallbacks` structure to the function [`init(sequentialInfo:callbacks:)`](cgdataprovider/init(sequentialinfo:callbacks:).md) to create a sequential-access data provider.

## Topics

### Initializers
- [init()](cgdataprovidersequentialcallbacks/init.md)
- [init(version: UInt32, getBytes: CGDataProviderGetBytesCallback?, skipForward: CGDataProviderSkipForwardCallback?, rewind: CGDataProviderRewindCallback?, releaseInfo: CGDataProviderReleaseInfoCallback?)](cgdataprovidersequentialcallbacks/init(version:getbytes:skipforward:rewind:releaseinfo:).md)
### Instance Properties
- [var getBytes: CGDataProviderGetBytesCallback?](cgdataprovidersequentialcallbacks/getbytes.md)
  A pointer to a function that copies data from the provider. For more information, see [`CGDataProviderGetBytesCallback`](cgdataprovidergetbytescallback.md).
- [var releaseInfo: CGDataProviderReleaseInfoCallback?](cgdataprovidersequentialcallbacks/releaseinfo.md)
  A pointer to a function that handles clean-up for the data provider, or `NULL`. For more information, see [`CGDataProviderReleaseInfoCallback`](cgdataproviderreleaseinfocallback.md).
- [var rewind: CGDataProviderRewindCallback?](cgdataprovidersequentialcallbacks/rewind.md)
  A pointer to a function Core Graphics calls to return the provider to the beginning of the data stream. For more information, see [`CGDataProviderRewindCallback`](cgdataproviderrewindcallback.md).
- [var skipForward: CGDataProviderSkipForwardCallback?](cgdataprovidersequentialcallbacks/skipforward.md)
  A pointer to a function that Core Graphics calls to advance the stream of data supplied by the provider.
- [var version: UInt32](cgdataprovidersequentialcallbacks/version.md)
  The version of this structure. It should be set to 0.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [init?(sequentialInfo: UnsafeMutableRawPointer?, callbacks: UnsafePointer<CGDataProviderSequentialCallbacks>)](cgdataprovider/init(sequentialinfo:callbacks:).md)
  Creates a sequential-access data provider.
- [typealias CGDataProviderRewindCallback](cgdataproviderrewindcallback.md)
  A callback function that moves the current position in the data stream back to the beginning.
- [typealias CGDataProviderGetBytesCallback](cgdataprovidergetbytescallback.md)
  A callback function that copies from a provider data stream into a Core Graphics buffer.
- [typealias CGDataProviderSkipForwardCallback](cgdataproviderskipforwardcallback.md)
  A callback function that advances the current position in the data stream supplied by the provider.
- [typealias CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md)
  A callback function that releases any private data or resources associated with the data provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataprovidersequentialcallbacks)*