# instanceCount

**Framework**: RealityKit  
**Kind**: property

The number of active instances to draw.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final var instanceCount: Int { get set }
```

#### Discussion

Defaults to `0` after creation. Set this to the number of transforms written before passing the buffer to a mesh instance.

## See Also

- [var instanceCapacity: Int](lowlevelinstancetransformresource/instancecapacity.md)
  The maximum number of instances the buffer holds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelinstancetransformresource/instancecount)*