# CGDataProviderReleaseInfoCallback

**Framework**: Core Graphics  
**Kind**: typealias

A callback function that releases any private data or resources associated with the data provider.

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
typealias CGDataProviderReleaseInfoCallback = (UnsafeMutableRawPointer?) -> Void
```

#### Discussion

When Core Graphics frees a data provider that has an associated release function, the release function is called.

For information on how to associate your callback function with a data provider, see [`CGDataProvider`](cgdataprovider.md) and [`CGDataProviderSequentialCallbacks`](cgdataprovidersequentialcallbacks.md).

## Parameters

- `info`: A generic pointer to private information shared among your callback functions. This is the same pointer you supplied to  .

## See Also

- [init?(sequentialInfo: UnsafeMutableRawPointer?, callbacks: UnsafePointer<CGDataProviderSequentialCallbacks>)](cgdataprovider/init(sequentialinfo:callbacks:).md)
  Creates a sequential-access data provider.
- [struct CGDataProviderSequentialCallbacks](cgdataprovidersequentialcallbacks.md)
  Defines a structure containing pointers to client-defined callback functions that manage the sending of data for a sequential-access data provider.
- [typealias CGDataProviderRewindCallback](cgdataproviderrewindcallback.md)
  A callback function that moves the current position in the data stream back to the beginning.
- [typealias CGDataProviderGetBytesCallback](cgdataprovidergetbytescallback.md)
  A callback function that copies from a provider data stream into a Core Graphics buffer.
- [typealias CGDataProviderSkipForwardCallback](cgdataproviderskipforwardcallback.md)
  A callback function that advances the current position in the data stream supplied by the provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataproviderreleaseinfocallback)*