# copyBytes(to:from:)

**Framework**: Dispatch  
**Kind**: method

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+
- Swift ?+

## Declaration

```swift
func copyBytes(to pointer: UnsafeMutablePointer<UInt8>, from range: Range<DispatchData.Index>)
```

## See Also

- [func append(DispatchData)](dispatchdata/append(_:)-3bvdr.md)
- [func append<SourceType>(UnsafeBufferPointer<SourceType>)](dispatchdata/append(_:)-9sgkq.md)
- [func append(UnsafeRawBufferPointer)](dispatchdata/append(_:)-1m94x.md)
- [func append(UnsafePointer<UInt8>, count: Int)](dispatchdata/append(_:count:).md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, count: Int)](dispatchdata/copybytes(to:count:)-4ffyj.md)
- [func copyBytes(to: UnsafeMutableRawBufferPointer, count: Int)](dispatchdata/copybytes(to:count:)-3j0qx.md)
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, from: Range<DispatchData.Index>?) -> Int](dispatchdata/copybytes(to:from:)-7zz4y.md)
- [func copyBytes(to: UnsafeMutableRawBufferPointer, from: Range<DispatchData.Index>)](dispatchdata/copybytes(to:from:)-60yai.md)
- [func enumerateBytes((UnsafeBufferPointer<UInt8>, Int, inout Bool) -> Void)](dispatchdata/enumeratebytes(_:).md)
- [func makeIterator() -> DispatchData.Iterator](dispatchdata/makeiterator.md)
- [func region(location: Int) -> (data: DispatchData, offset: Int)](dispatchdata/region(location:).md)
- [func subdata(in: Range<DispatchData.Index>) -> DispatchData](dispatchdata/subdata(in:).md)
- [func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result](dispatchdata/withunsafebytes(body:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/copybytes(to:from:)-6ztcb)*