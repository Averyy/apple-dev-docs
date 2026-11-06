# scale

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A scale factor for the local coordinate space the reference object defines.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+

## Declaration

```swift
var scale: simd_float3 { get }
```

```objc
@property (nonatomic, readonly) simd_float3 scale;
```

## Discussion

Multiplying the [`extent`](./extent.md) by this scale results in the physical size of the object in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arreferenceobject/scale)*