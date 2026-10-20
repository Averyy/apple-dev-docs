# dataPointer

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

A pointer to the multiarray’s underlying memory.

**Availability**:
- iOS 11.0+ - Deprecated in 27.2
- iPadOS 11.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.13+ - Deprecated in 27.2
- tvOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 4.0+ - Deprecated in 27.2

> **Deprecated**: Use getBytesWithHandler or getMutableBytesWithHandler instead. For Swift, use withUnsafeBytes or withUnsafeMutableBytes.

## Declaration

```swift
var dataPointer: UnsafeMutableRawPointer { get }
```

```objc
@property (nonatomic, readonly) void * dataPointer;
```

## See Also

### Accessing a multiarray’s elements
- [subscript(_:)](./subscript%28_%29.md)
- [var pixelBuffer: CVPixelBuffer?](./pixelbuffer.md)
  A reference to the multiarray’s underlying pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/datapointer)*