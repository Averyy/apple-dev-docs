# addBarrier()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Encodes a barrier into the command buffer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func addBarrier()
```

#### Discussion

The method encodes a barrier that starts any subsequent commands only after all the previously encoded commands have completed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/addbarrier())*