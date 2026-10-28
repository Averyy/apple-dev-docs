# CGDataProviderGetBytesAtPositionCallback

**Framework**: Core Graphics  
**Kind**: typealias  
**Role**: Type Alias

A callback function that copies data from the provider into a Core Graphics buffer.

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
typealias CGDataProviderGetBytesAtPositionCallback = (UnsafeMutableRawPointer?, UnsafeMutableRawPointer, off_t, Int) -> Int
```

```c
typedef unsigned long (*)(void *, void *, long long, unsigned long) CGDataProviderGetBytesAtPositionCallback;
```

## Return Value

The number of bytes copied. If no more data can be written to the buffer, you should return 0.

## Discussion

When Core Graphics is ready to receive data from the provider, your function is called.

## Parameters

- `info`: A generic pointer to private data shared among your callback functions. This is the same pointer you supplied to [`init(directInfo:size:callbacks:)`](./cgdataprovider/init%28directinfo,size,callbacks%29.md).
- `buffer`: The Core Graphics buffer into which you copy the specified number of bytes.
- `position`: Specifies the relative location in the data provider at which to begin copying data.
- `count`: The number of bytes to copy.

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
- [typealias CGDataProviderReleaseBytePointerCallback](./cgdataproviderreleasebytepointercallback.md)
  A callback function that releases the pointer Core Graphics obtained by calling [`CGDataProviderGetBytePointerCallback`](./cgdataprovidergetbytepointercallback.md).
- [typealias CGDataProviderReleaseInfoCallback](./cgdataproviderreleaseinfocallback.md)
  A callback function that releases any private data or resources associated with the data provider.
- [typealias CGDataProviderReleaseDataCallback](./cgdataproviderreleasedatacallback.md)
  A callback function that releases data you supply to the function [`init(dataInfo:data:size:releaseData:)`](./cgdataprovider/init%28datainfo,data,size,releasedata%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataprovidergetbytesatpositioncallback)*