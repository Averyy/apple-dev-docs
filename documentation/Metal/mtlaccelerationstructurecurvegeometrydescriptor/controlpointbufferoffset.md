# controlPointBufferOffset

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The offset, in bytes, to the control point data in the buffer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var controlPointBufferOffset: Int { get set }
```

```objc
@property (nonatomic) NSUInteger controlPointBufferOffset;
```

## Discussion

The offset needs to be a multiple of the format element size you configure with the [`controlPointFormat`](./controlpointformat.md) property. You also need to align the offset to the platform’s buffer alignment requirement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructurecurvegeometrydescriptor/controlpointbufferoffset)*