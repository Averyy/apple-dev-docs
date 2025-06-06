# instanceCount

**Framework**: Core Animation  
**Kind**: property

The number of copies to create, including the source layers.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var instanceCount: Int { get set }
```

#### Discussion

Default value is `1`, no extra copies are created.

## See Also

- [Core Animation Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
- [var instanceDelay: CFTimeInterval](careplicatorlayer/instancedelay.md)
  Specifies the delay, in seconds, between replicated copies. Animatable.
- [var instanceTransform: CATransform3D](careplicatorlayer/instancetransform.md)
  The transform matrix applied to the previous instance to produce the current instance. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/careplicatorlayer/instancecount)*