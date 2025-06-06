# init(_:using:bufferCapacity:writingTo:)

**Framework**: Compression  
**Kind**: init

Creates an output filter that can be used to compress or decompress data.

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
init(_ operation: FilterOperation, using algorithm: Algorithm, bufferCapacity: Int = 65536, writingTo writeFunc: @escaping (Data?) throws -> Void) throws
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/compression/outputfilter/init(_:using:buffercapacity:writingto:))*