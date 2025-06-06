# init(forReadingWith:)

**Framework**: Foundation  
**Kind**: init

Initializes an archiver to decode data from the specified location.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(forReadingWith data: Data)
```

#### Return Value

An [`NSKeyedUnarchiver`](nskeyedunarchiver.md) object initialized for for decoding `data`.

#### Discussion

When you finish decoding data, you should invoke [`finishDecoding()`](nskeyedunarchiver/finishdecoding().md).

This method throws an exception if `data` is not a valid archive.

## Parameters

- `data`: An archive previously encoded by  .

## See Also

- [Archives and Serializations Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Archiving/Archiving.html#//apple_ref/doc/uid/10000047i)
- [init(forReadingFrom: Data) throws](nskeyedunarchiver/init(forreadingfrom:).md)
  Initializes an archiver to decode data from the specified location.
- [init()](nskeyedunarchiver/init.md)
  Initializes an archiver to decode data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nskeyedunarchiver/init(forreadingwith:))*