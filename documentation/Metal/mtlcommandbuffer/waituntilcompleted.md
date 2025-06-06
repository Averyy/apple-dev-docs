# waitUntilCompleted()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Blocks the current thread until the GPU finishes executing the command buffer and all of its completion handlers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func waitUntilCompleted()
```

## See Also

- [func waitUntilScheduled()](mtlcommandbuffer/waituntilscheduled.md)
  Blocks the current thread until the command queue schedules the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/waituntilcompleted())*