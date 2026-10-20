# length

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The data size of the buffer, in bytes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var length: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger length;
```

## See Also

### Working with Data in a Buffer
- [func fill(Data, offset: Int)](./fill%28_,offset%29.md)
  Writes the specified data into the buffer.
- [func map() -> MDLMeshBufferMap](./map%28%29.md)
  Provides direct, read-only access to the buffer’s contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbuffer/length)*