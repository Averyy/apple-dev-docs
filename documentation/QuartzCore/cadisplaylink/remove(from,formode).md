# remove(from:forMode:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Removes the display link from the run loop for the given mode.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- macOS 14.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func remove(from runloop: RunLoop, forMode mode: RunLoop.Mode)
```

```objc
- (void) removeFromRunLoop:(NSRunLoop *) runloop forMode:(NSRunLoopMode) mode;
```

#### Discussion

The run loop releases the display link if it’s no longer associated with any run modes.

## Parameters

- `runloop`: The run loop you associate with the display link.
- `mode`: The run loop mode in which the display link is running.

## See Also

### Scheduling a Display Link to Send Notifications
- [func add(to: RunLoop, forMode: RunLoop.Mode)](./add%28to,formode%29.md)
  Registers the display link with a run loop.
- [func invalidate()](./invalidate%28%29.md)
  Removes the display link from all run loop modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cadisplaylink/remove(from:formode:))*