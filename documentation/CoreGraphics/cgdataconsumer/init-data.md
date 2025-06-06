# init(data:)

**Framework**: Core Graphics  
**Kind**: init

Creates a data consumer that writes to a CFData object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init?(data: CFMutableData)
```

#### Return Value

A new data consumer object. In Objective-C, you’re responsible for releasing this object using [`CGDataConsumerRelease`](cgdataconsumerrelease.md).

#### Discussion

You can use this function when you need to represent Core Graphics data as a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) type. For example, you might create a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) object that you then copy to the pasteboard.

## Parameters

- `data`: The CFData object to write to.

## See Also

- [init?(info: UnsafeMutableRawPointer?, cbks: UnsafePointer<CGDataConsumerCallbacks>)](cgdataconsumer/init(info:cbks:).md)
  Creates a data consumer that uses callback functions to write data.
- [init?(url: CFURL)](cgdataconsumer/init(url:).md)
  Creates a data consumer that writes data to a location specified by a URL.
- [struct CGDataConsumerCallbacks](cgdataconsumercallbacks.md)
  A structure that contains pointers to callback functions that manage the copying of data for a data consumer.
- [typealias CGDataConsumerPutBytesCallback](cgdataconsumerputbytescallback.md)
  Copies data from a Core Graphics-supplied buffer into a data consumer.
- [typealias CGDataConsumerReleaseInfoCallback](cgdataconsumerreleaseinfocallback.md)
  Releases any private data or resources associated with the data consumer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgdataconsumer/init(data:))*