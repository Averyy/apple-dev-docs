# memoryOwner

**Framework**: RealityKit  
**Kind**: property  
**Role**: Instance Property

An optional task identity token used to associate GPU memory allocations with a specific process for memory accounting purposes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var memoryOwner: task_id_token_t? { get set }
```

## See Also

### Configuring the renderer
- [var device: any MTLDevice](./device.md)
  The Metal device to use for all rendering operations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelrendercontextstandalone/configuration/memoryowner)*