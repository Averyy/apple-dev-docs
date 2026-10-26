# pixelBuffer

**Framework**: Core ML  
**Kind**: property  
**Role**: Instance Property

A reference to the multiarray’s underlying pixel buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var pixelBuffer: CVPixelBuffer? { get }
```

```objc
@property (nonatomic, readonly, nullable) CVPixelBufferRef pixelBuffer;
```

## See Also

### Accessing a multiarray’s elements
- [subscript(_:)](./subscript%28_%29.md)
- [var dataPointer: UnsafeMutableRawPointer](./datapointer.md)
  A pointer to the multiarray’s underlying memory.
- [- setObject:atIndexedSubscript:](./setobject_atindexedsubscript_.md)
  Assigns a number to the multiarray’s element at the location that the linear offset defines.
- [- setObject:forKeyedSubscript:](./setobject_forkeyedsubscript_.md)
  Assigns a number to the multiarray’s element at the location that the number array defines.
- [- getBytesWithHandler:](./getbyteswithhandler_.md)
  Get the underlying buffer pointer to read.
- [- getMutableBytesWithHandler:](./getmutablebyteswithhandler_.md)
  Get the underlying buffer pointer to mutate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreml/mlmultiarray/pixelbuffer)*