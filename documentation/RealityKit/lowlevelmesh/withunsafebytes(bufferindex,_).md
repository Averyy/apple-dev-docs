# withUnsafeBytes(bufferIndex:_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Reads a Metal vertex buffer synchronously on the CPU.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
func withUnsafeBytes(bufferIndex: Int, _ callback: (UnsafeRawBufferPointer) -> Void)
```

#### Discussion

The buffer is only valid for the lifetime of the callback.

## See Also

### Accessing mesh data on the CPU with Swift
- [func withUnsafeMutableBytes(bufferIndex: Int, (UnsafeMutableRawBufferPointer) -> Void)](./withunsafemutablebytes%28bufferindex,_%29.md)
  Updates a Metal vertex buffer synchronously on the CPU.
- [func withUnsafeIndices((UnsafeRawBufferPointer) -> Void)](./withunsafeindices%28_%29.md)
  Reads the index buffer synchronously on the CPU.
- [func withUnsafeMutableIndices((UnsafeMutableRawBufferPointer) -> Void)](./withunsafemutableindices%28_%29.md)
  Updates the index buffer synchronously on the CPU.
- [func replaceUnsafeMutableBytes(bufferIndex: Int, (UnsafeMutableRawBufferPointer) -> Void)](./replaceunsafemutablebytes%28bufferindex,_%29.md)
  Replaces a Metal vertex buffer synchronously on the CPU.
- [func replaceUnsafeMutableIndices((UnsafeMutableRawBufferPointer) -> Void)](./replaceunsafemutableindices%28_%29.md)
  Replaces the index buffer synchronously on the CPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/withunsafebytes(bufferindex:_:))*