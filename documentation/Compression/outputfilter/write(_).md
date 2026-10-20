# write(_:)

**Framework**: Compression  
**Kind**: method  
**Role**: Instance Method

Writes data to the output filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
func write<D>(_ data: D?) throws where D : DataProtocol
```

## See Also

### Instance Methods
- [func finalize() throws](./finalize%28%29.md)
  Finalizes the stream by flushing all the remaining data in the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/outputfilter/write(_:))*