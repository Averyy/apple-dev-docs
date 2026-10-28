# CGDataProviderReleaseBytePointerCallback

**Framework**: Core Graphics  
**Kind**: typealias  
**Role**: Type Alias

A callback function that releases the pointer Core Graphics obtained by calling [`CGDataProviderGetBytePointerCallback`](./cgdataprovidergetbytepointercallback.md).

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias CGDataProviderReleaseBytePointerCallback = (UnsafeMutableRawPointer?, UnsafeRawPointer) -> Void
```

```c
typedef void (*)(void *, const void *) CGDataProviderReleaseBytePointerCallback;
```

## Discussion

When Core Graphics no longer needs direct access to your provider data, your function is called. You may safely modify, move, or release your provider data at this time.

For information on how to associate your function with a direct-access data provider, see `CGDataProviderCreateDirectAccess` and `CGDataProviderDirectAccessCallbacks`.

## Parameters

- `info`: A generic pointer to private data shared among your callback functions.  This is the same pointer you supplied to `CGDataProviderCreateDirectAccess`.
- `pointer`: A pointer to your provider data. This is the same pointer you returned in [`CGDataProviderGetBytePointerCallback`](./cgdataprovidergetbytepointercallback.md).

## See Also

### Creating Direct-Access Data Providers
- [init?(directInfo: UnsafeMutableRawPointer?, size: off_t, callbacks: UnsafePointer<CGDataProviderDirectCallbacks>)](./cgdataprovider/init%28directinfo,size,callbacks%29.md)
  Creates a direct-access data provider.
- [init?(data: CFData)](./cgdataprovider/init%28data%29.md)
  Creates a data provider that reads from a CFData object.
- [init?(url: CFURL)](./cgdataprovider/init%28url%29.md)
  Creates a direct-access data provider that uses a URL to supply data.
- [init?(dataInfo: UnsafeMutableRawPointer?, data: UnsafeRawPointer, size: Int, releaseData: CGDataProviderReleaseDataCallback)](./cgdataprovider/init%28datainfo,data,size,releasedata%29.md)
  Creates a direct-access data provider that uses data your program supplies.
- [init?(filename: UnsafePointer<CChar>)](./cgdataprovider/init%28filename%29.md)
  Creates a direct-access data provider that uses a file to supply data.
- [struct CGDataProviderDirectCallbacks](./cgdataproviderdirectcallbacks.md)
  Defines pointers to client-defined callback functions that manage the sending of data for a direct-access data provider.
- [typealias CGDataProviderGetBytePointerCallback](./cgdataprovidergetbytepointercallback.md)
  A callback function that returns a generic pointer to the provider data.
- [typealias CGDataProviderGetBytesAtPositionCallback](./cgdataprovidergetbytesatpositioncallback.md)
  A callback function that copies data from the provider into a Core Graphics buffer.
- [typealias CGDataProviderReleaseInfoCallback](./cgdataproviderreleaseinfocallback.md)
  A callback function that releases any private data or resources associated with the data provider.
- [typealias CGDataProviderReleaseDataCallback](./cgdataproviderreleasedatacallback.md)
  A callback function that releases data you supply to the function [`init(dataInfo:data:size:releaseData:)`](./cgdataprovider/init%28datainfo,data,size,releasedata%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataproviderreleasebytepointercallback)*