# memoryOwner

**Framework**: RealityKit  
**Kind**: property

An optional task identity token used to associate GPU memory allocations with a specific process for memory accounting purposes.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var memoryOwner: task_id_token_t? { get set }
```

## See Also

- [var device: any MTLDevice](lowlevelrendercontextstandalone/configuration/device.md)
  The Metal device to use for all rendering operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/configuration/memoryowner)*