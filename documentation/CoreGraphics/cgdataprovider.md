# CGDataProvider

**Framework**: Core Graphics  
**Kind**: class

An abstraction for data-reading tasks that eliminates the need to manage a raw memory buffer.

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
class CGDataProvider
```

#### Overview

Data provider objects abstract the data-access task and eliminate the need for applications to manage data through a raw memory buffer.

For information on how to use CGDataProvider functions, see [`Quartz 2D Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) Programming Guide.

See also [`CGDataConsumer`](cgdataconsumer.md).

## Topics

### Creating Sequential-Access Data Providers
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
- [typealias CGDataProviderReleaseInfoCallback](cgdataproviderreleaseinfocallback.md)
  A callback function that releases any private data or resources associated with the data provider.
### Creating Direct-Access Data Providers
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
### Getting Data from a Data Provider
- [var data: CFData?](cgdataprovider/data.md)
  Returns a copy of the provider’s data.
### Working with Core Foundation Types
- [class var typeID: CFTypeID](cgdataprovider/typeid.md)
  Returns the Core Foundation type identifier for data providers.
### Instance Properties
- [var info: UnsafeMutableRawPointer?](cgdataprovider/info.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [Quartz 2D Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066)
- [class CGDataConsumer](cgdataconsumer.md)
  An abstraction for data-writing tasks that eliminates the need to manage a raw memory buffer.
- [class CGShading](cgshading.md)
  A definition for a smooth transition between colors, controlled by a custom function you provide, for drawing radial and axial gradient fills.
- [class CGGradient](cggradient.md)
  A definition for a smooth transition between colors for drawing radial and axial gradient fills.
- [class CGFunction](cgfunction.md)
  A general facility for defining and using callback functions.
- [class CGPattern](cgpattern.md)
  A 2D pattern to be used for drawing graphics paths.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataprovider)*