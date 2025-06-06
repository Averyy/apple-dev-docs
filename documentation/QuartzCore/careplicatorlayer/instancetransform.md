# instanceTransform

**Framework**: Core Animation  
**Kind**: property

The transform matrix applied to the previous instance to produce the current instance. Animatable.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var instanceTransform: CATransform3D { get set }
```

#### Discussion

This transform matrix is applied to instance `k-1` to produce instance `k`. The matrix is applied relative to the center of this layer.

Defaults to the identity matrix.

## See Also

- [var instanceCount: Int](careplicatorlayer/instancecount.md)
  The number of copies to create, including the source layers.
- [var instanceDelay: CFTimeInterval](careplicatorlayer/instancedelay.md)
  Specifies the delay, in seconds, between replicated copies. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/careplicatorlayer/instancetransform)*