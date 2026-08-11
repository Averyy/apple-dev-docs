# withElements(_:)

**Framework**: RealityKit  
**Kind**: method

Provides read-only access to the per-vertex data within a callback.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func withElements<Result>(_ callback: (Span<ElementType>) -> Result) -> Result
```

#### Return Value

The value returned by `callback`.

#### Discussion

The provided span is only valid for the lifetime of the callback.

## Parameters

- `callback`: A closure that receives a span over the per-vertex data.

## See Also

- [var vertexCount: Int](perclothvertexdata/vertexcount.md)
  The number of vertices this structure holds data for.
- [func withMutableElements<Result>((inout MutableSpan<ElementType>) -> Result) -> Result](perclothvertexdata/withmutableelements(_:).md)
  Provides mutable access to the per-vertex data within a callback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/perclothvertexdata/withelements(_:))*