# contentionRelief

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A contention relief strategy the compiler applies to the pipeline.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var contentionRelief: MTLContentionRelief { get set }
```

```objc
@property (nonatomic, readwrite) MTLContentionRelief contentionRelief;
```

## Discussion

The contention relief strategy applies to all pipeline functions except for functions you compile separately which retain the contention relief they were compiled with.

This property sets the contention relief only for functions with a `contention_relief` attribute equal to `default`, which includes functions that don’t specify the attribute. Functions you write with the `automatic` or `none` attribute ignore this property.

The default value is [`MTLContentionRelief.automatic`](../mtlcontentionrelief/automatic.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computepipelinedescriptor/contentionrelief)*