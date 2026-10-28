# instanceCount

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

The number of active instances to draw.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final var instanceCount: Int { get set }
```

## Discussion

Defaults to `0` after creation. Set this to the number of transforms written before passing the buffer to a mesh instance.

## See Also

### Inspecting instance counts
- [var instanceCapacity: Int](./instancecapacity.md)
  The maximum number of instances the buffer holds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancetransformresource/instancecount)*