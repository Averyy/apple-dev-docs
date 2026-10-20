# copyBytes(to:from:)

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

## Declaration

```swift
func copyBytes<DestinationType>(to buffer: UnsafeMutableBufferPointer<DestinationType>, from range: Range<DispatchData.Index>? = nil) -> Int
```

## See Also

### Copying Bytes
- [func copyBytes(to: UnsafeMutableRawBufferPointer, count: Int)](./copybytes%28to,count%29-3j0qx.md)
- [func copyBytes(to: UnsafeMutableRawBufferPointer, from: Range<DispatchData.Index>)](./copybytes%28to,from%29-60yai.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatchdata/copybytes(to:from:)-7zz4y)*