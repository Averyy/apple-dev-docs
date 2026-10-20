# waitUntilCompleted()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Blocks the current thread until the GPU finishes executing the command buffer and all of its completion handlers.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func waitUntilCompleted()
```

```objc
- (void) waitUntilCompleted;
```

## See Also

### Waiting for state changes
- [func waitUntilScheduled()](./waituntilscheduled%28%29.md)
  Blocks the current thread until the command queue schedules the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommandbuffer/waituntilcompleted())*