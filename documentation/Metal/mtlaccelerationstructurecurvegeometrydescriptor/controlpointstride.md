# controlPointStride

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The stride, in bytes, between control points in the buffer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var controlPointStride: Int { get set }
```

```objc
@property (nonatomic) NSUInteger controlPointStride;
```

#### Discussion

The stride needs to be a multiple of the format element size you configure with the [`controlPointFormat`](./controlpointformat.md) property, and at least the format’s size. The default value is `0`, which indicates that the control point elements in the buffer have zero bytes of padding between them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/controlpointstride)*