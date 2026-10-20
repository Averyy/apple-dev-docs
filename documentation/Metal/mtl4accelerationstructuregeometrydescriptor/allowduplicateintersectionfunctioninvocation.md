# allowDuplicateIntersectionFunctionInvocation

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A boolean value that indicates whether the ray-tracing system in Metal allows the invocation of intersection functions more than once per ray-primitive intersection.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var allowDuplicateIntersectionFunctionInvocation: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowDuplicateIntersectionFunctionInvocation;
```

#### Discussion

The property’s default value is [`true`](../../Swift/true.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4accelerationstructuregeometrydescriptor/allowduplicateintersectionfunctioninvocation)*