# logs

**Framework**: Metal  
**Kind**: property

The messages the command buffer records as the GPU runs its commands.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+

## Declaration

```swift
var logs: MTLLogContainer { get }
```

#### Discussion

The value of this property is valid only after the command buffer finishes executing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/logs-518l2)*