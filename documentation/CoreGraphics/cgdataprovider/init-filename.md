# init(filename:)

**Framework**: Core Graphics  
**Kind**: init

Creates a direct-access data provider that uses a file to supply data.

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
init?(filename: UnsafePointer<CChar>)
```

#### Return Value

A new data provider or `NULL` if the file could not be opened. In Objective-C, you’re responsible for releasing this object using [`CGDataProviderRelease`](cgdataproviderrelease.md).

#### Discussion

You use this function to create a direct-access data provider that supplies data from a file. When you supply Core Graphics with a direct-access data provider, Core Graphics obtains data from your program in a single block.

## Parameters

- `filename`: The full or relative pathname to use for the data provider. When you supply Core Graphics data via the provider, it reads the data from the specified file.

## See Also

- [init?(directInfo: UnsafeMutableRawPointer?, size: off_t, callbacks: UnsafePointer<CGDataProviderDirectCallbacks>)](cgdataprovider/init(directinfo:size:callbacks:).md)
  Creates a direct-access data provider.
- [init?(data: CFData)](cgdataprovider/init(data:).md)
  Creates a data provider that reads from a CFData object.
- [init?(url: CFURL)](cgdataprovider/init(url:).md)
  Creates a direct-access data provider that uses a URL to supply data.
- [init?(dataInfo: UnsafeMutableRawPointer?, data: UnsafeRawPointer, size: Int, releaseData: CGDataProviderReleaseDataCallback)](cgdataprovider/init(datainfo:data:size:releasedata:).md)
  Creates a direct-access data provider that uses data your program supplies.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataprovider/init(filename:))*