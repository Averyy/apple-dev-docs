# add(to:forMode:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Registers the display link with a run loop.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+
- macOS 14.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func add(to runloop: RunLoop, forMode mode: RunLoop.Mode)
```

```objc
- (void) addToRunLoop:(NSRunLoop *) runloop forMode:(NSRunLoopMode) mode;
```

## Discussion

You can associate a display link with multiple input modes. While the run loop is executing in a mode you specify, the display link notifies the target when the system requires new frames.

You can specify a custom mode or use one of the modes listed in [`RunLoop`](../../Foundation/runloop.md).

The run loop retains the display link. To remove the display link from all run loops, call [`invalidate()`](./invalidate%28%29.md).

## Parameters

- `runloop`: The run loop to associate with the display link.
- `mode`: The mode in which to add the display link to the run loop.

## See Also

### Scheduling a Display Link to Send Notifications
- [func remove(from: RunLoop, forMode: RunLoop.Mode)](./remove%28from,formode%29.md)
  Removes the display link from the run loop for the given mode.
- [func invalidate()](./invalidate%28%29.md)
  Removes the display link from all run loop modes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cadisplaylink/add(to:formode:))*