# withMutableElements(_:)

**Framework**: RealityKit  
**Kind**: method

Provides mutable access to the per-vertex data within a callback.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func withMutableElements<Result>(_ callback: @_lifetime(0: copy 0) (inout MutableSpan<ElementType>) -> Result) -> Result
```

#### Return Value

The value returned by `callback`.

#### Discussion

The provided span is only valid for the lifetime of the callback.

## Parameters

- `callback`: A closure that receives a mutable span over the per-vertex data.

## See Also

- [var vertexCount: Int](perclothvertexdata/vertexcount.md)
  The number of vertices this structure holds data for.
- [func withElements<Result>((Span<ElementType>) -> Result) -> Result](perclothvertexdata/withelements(_:).md)
  Provides read-only access to the per-vertex data within a callback.
- [var mutableElements: MutableSpan<ElementType>](perclothvertexdata/mutableelements.md)
  A mutable view of the per-vertex data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/perclothvertexdata/withmutableelements(_:))*