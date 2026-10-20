# offset

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The byte offset of the data within the Metal buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var offset: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger offset;
```

## See Also

### Metal Buffer Properties
- [var buffer: any MTLBuffer](./buffer.md)
  The Metal buffer backing all vertex and index data.
- [var length: Int](./length.md)
  The logical size of the Metal buffer, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer/offset)*