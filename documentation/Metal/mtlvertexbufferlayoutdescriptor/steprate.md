# stepRate

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The interval at which the vertex and its attributes are presented to the vertex function.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var stepRate: Int { get set }
```

```objc
@property (nonatomic, assign) NSUInteger stepRate;
```

#### Discussion

The default value is `1`. The `stepRate` value, in conjunction with the [`stepFunction`](./stepfunction.md) property, determines how often the function fetches new attribute data. The `stepRate` property is generally used when `stepFunction` is [`MTLVertexStepFunction.perInstance`](../mtlvertexstepfunction/perinstance.md). If `stepRate` is equal to `1`, new attribute data is fetched for every instance; if `stepRate` is equal to `2`, new attribute data is fetched for every two instances, and so forth.

## See Also

### Organizing the vertex buffer layout
- [var stepFunction: MTLVertexStepFunction](./stepfunction.md)
  The circumstances under which the vertex and its attributes are presented to the vertex function.
- [var stride: Int](./stride.md)
  The number of bytes between the first byte of two consecutive vertices in a buffer.
- [enum MTLVertexStepFunction](../mtlvertexstepfunction.md)
  The frequency with which the vertex function or post-tessellation vertex function fetches attribute data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlvertexbufferlayoutdescriptor/steprate)*