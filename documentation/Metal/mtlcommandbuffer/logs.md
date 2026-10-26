# logs

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

The messages the command buffer records as the GPU runs its commands.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (readonly) id<MTLLogContainer> logs;
```

#### Discussion

The value of this property is valid only after the command buffer finishes executing.

## Default Implementations

### MTLCommandBuffer Implementations
- [var logs: MTLLogContainer](./logs-518l2.md)
  The messages the command buffer records as the GPU runs its commands.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/logs)*