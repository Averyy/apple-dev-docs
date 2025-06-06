# tryCancel()

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Submits a request to abandon a command buffer the queue is currently running.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func tryCancel()
```

#### Discussion

Check the command buffer’s [`status`](mtliocommandbuffer/status.md) property after it completes, either after [`waitUntilCompleted()`](mtliocommandbuffer/waituntilcompleted().md) or in one of your completion handlers (see [`addCompletedHandler(_:)`](mtliocommandbuffer/addcompletedhandler(_:).md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/trycancel())*