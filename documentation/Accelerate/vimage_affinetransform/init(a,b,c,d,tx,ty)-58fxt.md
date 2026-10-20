# init(a:b:c:d:tx:ty:)

**Framework**: Accelerate  
**Kind**: init  
**Role**: Initializer

Returns a new affine transform.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
init(a: Float, b: Float, c: Float, d: Float, tx: Float, ty: Float)
```

## Parameters

- `a`: The entry at position `[1,1]` in the matrix.
- `b`: The entry at position `[1,2]` in the matrix.
- `c`: The entry at position `[2,1]` in the matrix.
- `d`: The entry at position `[2,2]` in the matrix.
- `tx`: The entry at position `[3,1]` in the matrix.
- `ty`: The entry at position `[3,2]` in the matrix.

## See Also

### Initializers
- [init()](./init%28%29.md)
- [init(a: CGFloat, b: CGFloat, c: CGFloat, d: CGFloat, tx: CGFloat, ty: CGFloat)](./init%28a,b,c,d,tx,ty%29-6b4yl.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage_affinetransform/init(a:b:c:d:tx:ty:)-58fxt)*