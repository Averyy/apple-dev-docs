# tryCancel()

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (void) tryCancel;
```

## Discussion

Check the command buffer’s [`status`](./status.md) property after it completes, either after [`waitUntilCompleted()`](./waituntilcompleted%28%29.md) or in one of your completion handlers (see [`addCompletedHandler(_:)`](./addcompletedhandler%28_%29.md)).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtliocommandbuffer/trycancel())*