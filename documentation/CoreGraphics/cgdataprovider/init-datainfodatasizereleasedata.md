# init(dataInfo:data:size:releaseData:)

**Framework**: Core Graphics  
**Kind**: init

Creates a direct-access data provider that uses data your program supplies.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(dataInfo info: UnsafeMutableRawPointer?, data: UnsafeRawPointer, size: Int, releaseData: CGDataProviderReleaseDataCallback)
```

#### Return Value

A new data provider. In Objective-C, you’re responsible for releasing this object using [`CGDataProviderRelease`](cgdataproviderrelease.md).

#### Discussion

You use this function to create a direct-access data provider that uses callback functions to read data from your program an entire block at one time.

## Parameters

- `info`: A pointer to data of any type, or  . When Core Graphics calls the function specified in the   parameter, it sends this pointer as its first argument.
- `data`: A pointer to the array of data that the provider contains.
- `size`: A value that specifies the number of bytes that the data provider contains.
- `releaseData`: A pointer to a release callback for the data provider, or  . Your release function is called when Core Graphics frees the data provider. For more information, see  .

## See Also

- [init?(directInfo: UnsafeMutableRawPointer?, size: off_t, callbacks: UnsafePointer<CGDataProviderDirectCallbacks>)](cgdataprovider/init(directinfo:size:callbacks:).md)
  Creates a direct-access data provider.
- [init?(data: CFData)](cgdataprovider/init(data:).md)
  Creates a data provider that reads from a CFData object.
- [init?(url: CFURL)](cgdataprovider/init(url:).md)
  Creates a direct-access data provider that uses a URL to supply data.
- [init?(filename: UnsafePointer<CChar>)](cgdataprovider/init(filename:).md)
  Creates a direct-access data provider that uses a file to supply data.
- [struct CGDataProviderDirectCallbacks](cgdataproviderdirectcallbacks.md)
  Defines pointers to client-defined callback functions that manage the sending of data for a direct-access data provider.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataprovider/init(datainfo:data:size:releasedata:))*