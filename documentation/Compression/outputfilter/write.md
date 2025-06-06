# write(_:)

**Framework**: Compression  
**Kind**: method

Writes data to the output filter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func write<D>(_ data: D?) throws where D : DataProtocol
```

## See Also

- [func finalize() throws](outputfilter/finalize.md)
  Finalizes the stream by flushing all the remaining data in the stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/outputfilter/write(_:))*