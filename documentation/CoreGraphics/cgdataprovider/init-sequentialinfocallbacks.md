# init(sequentialInfo:callbacks:)

**Framework**: Core Graphics  
**Kind**: init

Creates a sequential-access data provider.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(sequentialInfo info: UnsafeMutableRawPointer?, callbacks: UnsafePointer<CGDataProviderSequentialCallbacks>)
```

#### Return Value

A new data provider. In Objective-C, you’re responsible for releasing this object using [`CGDataProviderRelease`](cgdataproviderrelease.md).

#### Discussion

You use this function to create a sequential-access data provider that uses callback functions to read data from your program in a single block.

## Parameters

- `info`: A pointer to data of any type or  . When Core Graphics calls the functions specified in the   parameter, it sends each of the functions this pointer.
- `callbacks`: A pointer to a   structure that specifies the callback functions you implement to handle the data provider’s basic memory management.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataprovider/init(sequentialinfo:callbacks:))*