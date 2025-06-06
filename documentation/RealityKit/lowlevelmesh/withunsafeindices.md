# withUnsafeIndices(_:)

**Framework**: RealityKit  
**Kind**: method

Reads the index buffer synchronously on the CPU.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
@MainActor
func withUnsafeIndices(_ callback: (UnsafeRawBufferPointer) -> Void)
```

#### Discussion

The buffer is only valid for the lifetime of the callback.

## See Also

- [func withUnsafeBytes(bufferIndex: Int, (UnsafeRawBufferPointer) -> Void)](lowlevelmesh/withunsafebytes(bufferindex:_:).md)
  Reads a Metal vertex buffer synchronously on the CPU.
- [func withUnsafeMutableBytes(bufferIndex: Int, (UnsafeMutableRawBufferPointer) -> Void)](lowlevelmesh/withunsafemutablebytes(bufferindex:_:).md)
  Updates a Metal vertex buffer synchronously on the CPU.
- [func withUnsafeMutableIndices((UnsafeMutableRawBufferPointer) -> Void)](lowlevelmesh/withunsafemutableindices(_:).md)
  Updates the index buffer synchronously on the CPU.
- [func replaceUnsafeMutableBytes(bufferIndex: Int, (UnsafeMutableRawBufferPointer) -> Void)](lowlevelmesh/replaceunsafemutablebytes(bufferindex:_:).md)
  Replaces a Metal vertex buffer synchronously on the CPU.
- [func replaceUnsafeMutableIndices((UnsafeMutableRawBufferPointer) -> Void)](lowlevelmesh/replaceunsafemutableindices(_:).md)
  Replaces the index buffer synchronously on the CPU.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/withunsafeindices(_:))*