# fill(_:offset:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Writes the specified data into the buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func fill(_ data: Data, offset: Int)
```

```objc
- (void) fillData:(NSData *) data offset:(NSUInteger) offset;
```

#### Discussion

If the length of the specified data (plus the `offset` parameter, if nonzero) is greater than the buffer’s [`length`](./length.md) property, this method writes data only up to the end of the buffer.

## Parameters

- `data`: The data to be copied into the buffer.
- `offset`: The offset, in bytes, from the start of the buffer at which to write data.

## See Also

### Working with Data in a Buffer
- [func map() -> MDLMeshBufferMap](./map%28%29.md)
  Provides direct, read-only access to the buffer’s contents.
- [var length: Int](./length.md)
  The data size of the buffer, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbuffer/fill(_:offset:))*