# init(data:)

**Framework**: Core Graphics  
**Kind**: init  
**Role**: Initializer

Creates a data provider that reads from a CFData object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(data: CFData)
```

```c
extern CGDataProviderRefCGDataProviderCreateWithCFData(CFDataRef data);
```

#### Return Value

A new data provider. In Objective-C, you’re responsible for releasing this object using [`CGDataProviderRelease`](../cgdataproviderrelease.md).

#### Discussion

You can use this function when you need to represent Core Graphics data as a CFData type. For example, you might create a CFData object when reading data from the pasteboard.

## Parameters

- `data`: The CFData object to read from.

## See Also

### Creating Direct-Access Data Providers
- [init?(directInfo: UnsafeMutableRawPointer?, size: off_t, callbacks: UnsafePointer<CGDataProviderDirectCallbacks>)](./init%28directinfo,size,callbacks%29.md)
  Creates a direct-access data provider.
- [init?(url: CFURL)](./init%28url%29.md)
  Creates a direct-access data provider that uses a URL to supply data.
- [init?(dataInfo: UnsafeMutableRawPointer?, data: UnsafeRawPointer, size: Int, releaseData: CGDataProviderReleaseDataCallback)](./init%28datainfo,data,size,releasedata%29.md)
  Creates a direct-access data provider that uses data your program supplies.
- [init?(filename: UnsafePointer<CChar>)](./init%28filename%29.md)
  Creates a direct-access data provider that uses a file to supply data.
- [struct CGDataProviderDirectCallbacks](../cgdataproviderdirectcallbacks.md)
  Defines pointers to client-defined callback functions that manage the sending of data for a direct-access data provider.
- [typealias CGDataProviderGetBytePointerCallback](../cgdataprovidergetbytepointercallback.md)
  A callback function that returns a generic pointer to the provider data.
- [typealias CGDataProviderGetBytesAtPositionCallback](../cgdataprovidergetbytesatpositioncallback.md)
  A callback function that copies data from the provider into a Core Graphics buffer.
- [typealias CGDataProviderReleaseBytePointerCallback](../cgdataproviderreleasebytepointercallback.md)
  A callback function that releases the pointer Core Graphics obtained by calling [`CGDataProviderGetBytePointerCallback`](../cgdataprovidergetbytepointercallback.md).
- [typealias CGDataProviderReleaseInfoCallback](../cgdataproviderreleaseinfocallback.md)
  A callback function that releases any private data or resources associated with the data provider.
- [typealias CGDataProviderReleaseDataCallback](../cgdataproviderreleasedatacallback.md)
  A callback function that releases data you supply to the function [`init(dataInfo:data:size:releaseData:)`](./init%28datainfo,data,size,releasedata%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataprovider/init(data:))*