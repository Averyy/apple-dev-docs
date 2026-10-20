# label

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A label for the geometry structure, suitable for debugging.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var label: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * label;
```

## See Also

### Specifying base geometry properties
- [var intersectionFunctionTableOffset: Int](./intersectionfunctiontableoffset.md)
  An index into the intersection table for determining which intersection function Metal calls when it intersects a ray with the acceleration structure.
- [var opaque: Bool](./opaque.md)
  A Boolean value that determines whether the geometry data in the acceleration structure needs to skip triangle-intersection tests.
- [var allowDuplicateIntersectionFunctionInvocation: Bool](./allowduplicateintersectionfunctioninvocation.md)
  A Boolean value that indicates whether Metal calls the ray-intersection test more than once per primitive on the structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuregeometrydescriptor/label)*