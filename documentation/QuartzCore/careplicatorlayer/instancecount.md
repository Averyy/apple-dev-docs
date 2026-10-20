# instanceCount

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property NSInteger instanceCount;
```

#### Discussion

Default value is `1`, no extra copies are created.

## See Also

### Related Documentation
- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)
### Setting Instance Display Properties
- [var instanceDelay: CFTimeInterval](./instancedelay.md)
  Specifies the delay, in seconds, between replicated copies. Animatable.
- [var instanceTransform: CATransform3D](./instancetransform.md)
  The transform matrix applied to the previous instance to produce the current instance. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/careplicatorlayer/instancecount)*