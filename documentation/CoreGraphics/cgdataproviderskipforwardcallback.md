# CGDataProviderSkipForwardCallback

**Framework**: Core Graphics  
**Kind**: typealias

A callback function that advances the current position in the data stream supplied by the provider.

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
typealias CGDataProviderSkipForwardCallback = (UnsafeMutableRawPointer?, off_t) -> off_t
```

#### Return Value

The number of bytes that were actually skipped.

#### Discussion

When Core Graphics needs to advance forward in the provider’s data stream, your function is called.

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to  .
- `count`: The number of bytes to skip.

## See Also

- [init?(sequentialInfo: UnsafeMutableRawPointer?, callbacks: UnsafePointer<CGDataProviderSequentialCallbacks>)](cgdataprovider/init(sequentialinfo:callbacks:).md)
  Creates a sequential-access data provider.
- [struct CGDataProviderSequentialCallbacks](cgdataprovidersequentialcallbacks.md)
  Defines a structure containing pointers to client-defined callback functions that manage the sending of data for a sequential-access data provider.
- [typealias CGDataProviderRewindCallback](cgdataproviderrewindcallback.md)
  A callback function that moves the current position in the data stream back to the beginning.
- [typealias CGDataProviderGetBytesCallback](cgdataprovidergetbytescallback.md)
  A callback function that copies from a provider data stream into a Core Graphics buffer.
- [typealias CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md)
  A callback function that releases any private data or resources associated with the data provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataproviderskipforwardcallback)*