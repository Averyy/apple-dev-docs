# mutableElements

**Framework**: RealityKit  
**Kind**: property

A mutable view of the per-vertex data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var mutableElements: MutableSpan<ElementType> { mutating get }
```

#### Discussion

The span’s lifetime is tied to `self`.

## See Also

- [var vertexCount: Int](perclothvertexdata/vertexcount.md)
  The number of vertices this structure holds data for.
- [func withElements<Result>((Span<ElementType>) -> Result) -> Result](perclothvertexdata/withelements(_:).md)
  Provides read-only access to the per-vertex data within a callback.
- [func withMutableElements<Result>((inout MutableSpan<ElementType>) -> Result) -> Result](perclothvertexdata/withmutableelements(_:).md)
  Provides mutable access to the per-vertex data within a callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/perclothvertexdata/mutableelements)*