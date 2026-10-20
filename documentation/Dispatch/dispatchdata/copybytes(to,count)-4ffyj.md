# copyBytes(to:count:)

**Framework**: Dispatch  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS
- Swift - Deprecated in 4.0

> **Deprecated**: Use copyBytes(to: UnsafeMutableRawBufferPointer, count: Int) instead

## Declaration

```swift
func copyBytes(to pointer: UnsafeMutablePointer<UInt8>, count: Int)
```

## See Also

### Combining Sequence Elements
- [func append(DispatchData)](./append%28_%29-3bvdr.md)
- [func append<SourceType>(UnsafeBufferPointer<SourceType>)](./append%28_%29-9sgkq.md)
- [func append(UnsafeRawBufferPointer)](./append%28_%29-1m94x.md)
- [func append(UnsafePointer<UInt8>, count: Int)](./append%28_,count%29.md)
- [func copyBytes(to: UnsafeMutableRawBufferPointer, count: Int)](./copybytes%28to,count%29-3j0qx.md)
- [func copyBytes<DestinationType>(to: UnsafeMutableBufferPointer<DestinationType>, from: Range<DispatchData.Index>?) -> Int](./copybytes%28to,from%29-7zz4y.md)
- [func copyBytes(to: UnsafeMutablePointer<UInt8>, from: Range<DispatchData.Index>)](./copybytes%28to,from%29-6ztcb.md)
- [func copyBytes(to: UnsafeMutableRawBufferPointer, from: Range<DispatchData.Index>)](./copybytes%28to,from%29-60yai.md)
- [func enumerateBytes((UnsafeBufferPointer<UInt8>, Int, inout Bool) -> Void)](./enumeratebytes%28_%29.md)
- [func makeIterator() -> DispatchData.Iterator](./makeiterator%28%29.md)
- [func region(location: Int) -> (data: DispatchData, offset: Int)](./region%28location%29.md)
- [func subdata(in: Range<DispatchData.Index>) -> DispatchData](./subdata%28in%29.md)
- [func withUnsafeBytes<Result, ContentType>(body: (UnsafePointer<ContentType>) throws -> Result) rethrows -> Result](./withunsafebytes%28body%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/copybytes(to:count:)-4ffyj)*